import platform
from pprint import pprint

from pedalboard import Chorus, Compressor, Delay, Gain, Pedalboard, Phaser, Reverb
from pedalboard.io import AudioStream

system = platform.system()

# Find Available I/O
print("Inputs:")
pprint(AudioStream.input_device_names)
print("======================================")
print("Outputs:")
pprint(AudioStream.output_device_names)

# My defaults
if system == "Darwin":
    input_device_name = "External Microphone"  # iRig 2 Error -> allow_feedback=True
    output_device_name = "JBL GO 2"  # Works on Bluetooth
    # output_device_name = "MacBook Pro Speakers"
    # output_device_name = "Loopback Audio"
elif system == "Windows":
    input_device_name = "Line 1/2 (M-Audio Fast Track Ul"
    output_device_name = "Speakers (M-Audio Fast Track Ultra)"
    # output_device_name ="Speakers (JBL GO 2 Stereo)"  # Works on Bluetooth
else:
    input_device_name = None
    output_device_name = None

print(
    "\nCurrent I/O:\n"
    "Input:  {}\n"
    "Output: {}\n".format(input_device_name, output_device_name)
)


# Open up an audio stream:
with AudioStream(input_device_name, output_device_name) as stream:
    # Audio is now streaming through this pedalboard and out of your speakers!
    # Reminds me of The Warmth - Make Yourself - Incubus - Mike Einziger sound
    # Works well w/ harmonics or EBow
    stream.plugins = Pedalboard(
        [
            Compressor(threshold_db=-50, ratio=25),
            Gain(gain_db=30),
            Chorus(),
            Phaser(),
            # TODO: Find this
            # Convolution("./guitar_amp.wav", 1.0),
            Delay(delay_seconds=0.5, feedback=0.1, mix=0.5),
            # Reverb(room_size=0.25),
            Reverb(room_size=0.75),
        ]
    )
    input("Press enter to stop streaming...")

# The live AudioStream is now closed, and audio has stopped.
