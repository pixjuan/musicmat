#! /usr/bin/python3

import simpleaudio as sa
import evdev
import sys


class MusicMat:
    """
    Read from a USB music mat or any joystick device and play music samples
    accordingly.
    """

    axis_name = ['x', 'y', 'z', 'X', 'Y', 'Z']

    button_map = {294: 1, 290: 2, 295: 3, 288: 4, 1: 5, 291: 6, 292: 7, 289: 8,
                  293: 9}

    def __init__(self, mat_dev=None):
        if mat_dev is None:
            devices = [evdev.InputDevice(path) for path in
                       evdev.list_devices()]
            self.device = devices[0]
            print("reading from " + str(self.device))
        else:
            try:
                self.device = evdev.InputDevice(mat_dev)
            except Exception as e:
                print("Not a valid input device path.")
                exit(1)
        self.samples = dict()
        self.playing = None
        self.load_sounds()

    def load_sounds(self):
        for i in range(1, 10):
            self.samples[i] = sa.WaveObject.from_wave_file(
                'sounds/' + str(i) + '.wav')

    def run_loop(self):
        """main loop, never return"""

        for event in self.device.read_loop():

            if event.type == evdev.ecodes.EV_ABS:
                print("axis %d value %d" % (event.code, event.value))
                print("event.value : " + str(event.value))
                if event.code == 1 and event.value == 255:
                    print('playing sample 5')
                    self.playing = self.samples[5].play()

            if event.type == evdev.ecodes.EV_KEY:
                if event.value == 1:
                    print("button %d pressed" % event.code)
                    if event.code in self.button_map:
                        print('playing %d' % self.button_map[event.code])
                        try:
                            self.playing = self.samples[
                                self.button_map[event.code]].play()
                        except Exception as ex:
                            template = "An exception of type {0} occured. "\
                                "Arguments:\n{1!r}"
                            message = template.format(type(ex).__name__,
                                                      ex.args)
                            print("can't play" + message)

                if event.value == 0:
                    print("button %d released" % event.code)


def main():
    if len(sys.argv) == 1:
        mat_dev = None
    elif len(sys.argv) == 2:
        mat_dev = sys.argv[1]

    dancemat = MusicMat(mat_dev)
    print('starting main loop')
    try:
        dancemat.run_loop()
    except KeyboardInterrupt:
        print("stopping...")


if __name__ == "__main__":
    main()
