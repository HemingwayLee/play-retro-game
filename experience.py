import argparse
import retro
import cv2
import numpy as np
from collections import deque

STACK_SIZE = 4
RESIZE_FACTOR = 2
PRETRAIN_LENGTH = 2

class Memory():
    def __init__(self):
        self.buffer = deque(maxlen=PRETRAIN_LENGTH)
    
    def add(self, experience):
        self.buffer.append(experience)
    
    def sample(self, batch_size):
        index = np.random.choice(np.arange(len(self.buffer)), size=batch_size, replace=False)
        return [self.buffer[i] for i in index]

    def save(self, rows, cols):
        img = np.array([each[0] for each in self.buffer], dtype=np.float32)
        print(img)
        print(img.shape)

        for i in range(len(img)):
            for j in range(len(img[i])):
                cv2.imwrite(f"{i}_{j}.png", img[i][j])

def preprocess(frame, is_gray=True, is_resized=True, is_normalized=False):
    ret_img = frame
    
    if is_gray:
        ret_img = cv2.cvtColor(ret_img, cv2.COLOR_BGR2GRAY)
    
    if is_resized:
        ret_img = cv2.resize(ret_img, (int(ret_img.shape[1]/RESIZE_FACTOR), int(ret_img.shape[0]/RESIZE_FACTOR)), interpolation=cv2.INTER_AREA)
    
    if is_normalized:
        ret_img = cv2.normalize(ret_img, None, alpha=-1, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        
    return ret_img

def stack_frames(stacked_frames, observation, is_new_episode, shape):
    frame = preprocess(observation)
    
    if is_new_episode:
        stacked_frames = deque([np.zeros(shape, dtype=np.int) for i in range(STACK_SIZE)], maxlen=STACK_SIZE)
        stacked_frames.append(frame)
        stacked_frames.append(frame)
        stacked_frames.append(frame)
        stacked_frames.append(frame)
    else:
        # Append frame to deque, automatically removes the oldest frame
        stacked_frames.append(frame)

    stacked_state = np.stack(stacked_frames, axis=0) # axis=2
    return stacked_state, stacked_frames

def run(game_name):
    env = retro.make(game=game_name)
    print(f"The size of our frame is: {env.observation_space}")
    
    state = env.reset()
    rows, cols = int(state.shape[0]/RESIZE_FACTOR), int(state.shape[1]/RESIZE_FACTOR)
    print(f"rows: {rows}, cols: {cols}")
    
    stacked_frames = deque([np.zeros((rows, cols), dtype=np.int) for i in range(STACK_SIZE)], maxlen=STACK_SIZE)
    stacked_state, stacked_frames = stack_frames(stacked_frames, state, True, (rows, cols))
    
    memory = Memory()
    while True:
        action = env.action_space.sample()
        print(env.get_action_meaning(action))

        next_state, reward, done, info = env.step(action)
        env.render()

        next_stacked_state, stacked_frames = stack_frames(stacked_frames, next_state, False, (rows, cols))
        memory.add([stacked_state, action, reward, next_stacked_state, done])
        stacked_state = next_stacked_state
        
        if done:
            break

    env.close()
    memory.save(rows, cols)

def main():
    parser = argparse.ArgumentParser(description='Image preprocessing and experience replay')
    parser.add_argument('-g', '--game', help='Please put the name of supported game (e.g., Airstriker-Genesis, Breakout-Atari2600, ...)', required=True)

    args = vars(parser.parse_args())
    run(args["game"])

if __name__ == "__main__":
    main()
