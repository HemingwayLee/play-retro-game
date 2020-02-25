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
![breakout](https://user-images.githubusercontent.com/8428372/75220475-dc642f00-57e2-11ea-8845-9761061092d6.png)
![boxing](https://user-images.githubusercontent.com/8428372/75220483-e0904c80-57e2-11ea-9f4c-c7583e8ca5fd.png)


# Reference  
https://retro.readthedocs.io/en/latest/getting_started.html


