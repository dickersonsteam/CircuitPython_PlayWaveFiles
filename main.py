from digitalio import DigitalInOut, Direction, Pull
import audioio
import board


# make the 2 input buttons
buttonA = DigitalInOut(board.D0)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN


buttonB = DigitalInOut(board.D1)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN

# if you have more buttons, simply copy the three lines above and set the board.D0
# to an available pin like board.D11

# The two files assigned to buttons A & B
# if you have more files, add their names here
audiofiles = ["rimshot.wav", "laugh.wav"]


def play_file(filename):
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
    while a.playing:
        pass
    print("finished")


while True:
    if buttonA.value:
        play_file(audiofiles[0])
    if buttonB.value:
        play_file(audiofiles[1])
