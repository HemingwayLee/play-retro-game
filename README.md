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

* Play the games
![boxing](https://user-images.githubusercontent.com/8428372/72200071-1aea9800-3488-11ea-9431-ead2006cc459.png)
![breakout](https://user-images.githubusercontent.com/8428372/72200072-1cb45b80-3488-11ea-8554-b21803f41c93.png)

# Reference  
https://retro.readthedocs.io/en/latest/getting_started.html


