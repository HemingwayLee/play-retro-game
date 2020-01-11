import argparse
import numpy as np
import retro
from random import randrange

def play_game_randomly(game_name):
    env = retro.make(game=game_name)
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        
        print(env.get_action_meaning(action))
        obs, reward, done, info = env.step(action)
        
        print(f"reward: {reward}")
        print(info)
        env.render()
        
        if done:
            break

    env.close()

def get_info(game_name):
    env = retro.make(game=game_name)
    print(f"The size of our frame is: {env.observation_space}")
    print(f"The action size is : {env.action_space.n}")

    possible_actions = np.array(np.identity(env.action_space.n,dtype=int).tolist())
    print(f"possible actions:\n{possible_actions}")

    print(f"action names:")
    for act in possible_actions:
        print(env.get_action_meaning(act))

def list_games():
    print(retro.data.list_games())

def run(args):
    if args["mode"] == 'list':
        list_games()
    elif args["mode"] == 'info':
        get_info(args["game"])
    else:
        play_game_randomly(args["game"])

def main():
    parser = argparse.ArgumentParser(description='Play and understand Retro games')
    parser.add_argument('-m', '--mode', choices=['list','run','info'], help='Please put a mode', required=True)
    parser.add_argument('-g', '--game', help='Please put the name of supported game (e.g., Airstriker-Genesis, Breakout-Atari2600, ...)')

    args = vars(parser.parse_args())

    print(args["mode"])

    if args["mode"] != 'list' and args["game"] == None:
        print("Please put the name of supported game (e.g., Airstriker-Genesis, Breakout-Atari2600, ...)")
    else: 
        run(args)

if __name__ == "__main__":
    main()

