# hello-retro
## Installation

```
virtualenv venv
source venv/
source venv/bin/activate
pip3 install -r requirements.txt 
```

## Play games manually
```
python3 -m retro.examples.interactive --game Airstriker-Genesis
```

* When we play `Airstriker-Genesis`, press `x` to shot
* By default, only `Airstriker-Genesis` installed

## Install other ROMs
* Download [ROMs](http://www.atarimania.com/rom_collection_archive_atari_2600_roms.html)
* Uncompress ROMs
* Import
```
python3 -m retro.import /path/to/your/ROMs/directory/
```

* Run the installed games (e.g., Breakout-Atari2600, Boxing-Atari2600, ...)
```
python3 -m retro.examples.interactive --game Breakout-Atari2600
```

* Play the games in interactive mode
![breakout](https://user-images.githubusercontent.com/8428372/76697190-619e7d80-66d7-11ea-9ade-58755fe15609.png)
![pong](https://user-images.githubusercontent.com/8428372/76697193-6400d780-66d7-11ea-9dd0-59d6f0193cbb.png)

## List all supported games
```
python3 hello.py -m list
```

### Get information about the game
```
python3 hello.py -m info -g Pong-Atari2600
```

Following information will be printed:
```
The size of our frame is: Box(210, 160, 3)
The action size is : 8
possible actions:
[[1 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]
 [0 0 0 0 1 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 1]]
action names:
['BUTTON']
[]
[]
[]
['UP']
['DOWN']
['LEFT']
['RIGHT']
```

### Run the game with random actions to see the reward 
```
python3 hello.py -m run -g Pong-Atari2600
```

# Reference  
https://retro.readthedocs.io/en/latest/getting_started.html


