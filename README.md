
# Music Mat

This is a simple project that allows playing samples by walking on a DDR type dance mat, or any USB joypad.
The goal was to make a musical toy for kids, each "zone" of the mat plays a different sound.
The project is documented on my [hackaday page](https://hackaday.io/project/171913-music-mat)

## Requirements

- A [DanceDanceRevolution](https://www.igdb.com/games/dance-dance-revolution) or [StepMania](https://www.stepmania.com) compatible mat.
- A Linux PC with python3


## Install

```
apt install pip3
apt install libasound2-dev
pip3 install simpleaudio
pip3 install evdev
```

Rename your sound samples as {1,2,3,4,5,6,7,8,9}.wav and copy them in ./sounds


## Usage

```
./musicmat.py [<DDR mat input device path>] 
```

Will start the script, reading from the specified input device. If no device is specified, then the script will pick the first one it finds in /dev/.
It will run until you press Ctrl-C.



# TODO

As SimpleAudio doesn't seem to work properly on the Pi, it could be rewritten using pygame so it would run on Raspberry Pi and Windows as well.
