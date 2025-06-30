import ipdb
# from pedalboard import Convolution, Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser
from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser
from pedalboard.io import AudioStream

# Open up an audio stream:
with AudioStream(
  # input_device_name="Apogee Jam+",  # Guitar interface
  # input_device_name="M-Audio Fast Track Ultra",  # audio interface
  input_device_name="External Microphone", # iRig 2
  # output_device_name="MacBook Pro Speakers",
  output_device_name="JBL GO 2", # JBL GO 2 - Works on Bluetooth
  allow_feedback=True
) as stream:
  # Audio is now streaming through this pedalboard and out of your speakers!
  # TODO: Dial in The Warmth - Make Yourself Incubus - Mike Einziger sound
  # Works well w/ harmonics or EBow
  stream.plugins = Pedalboard([
      Compressor(threshold_db=-50, ratio=25),
      Gain(gain_db=30),
      Chorus(),
      Phaser(),
      # TODO: add from pedalboard repo
      # Convolution("./guitar_amp.wav", 1.0),
      Delay(delay_seconds=0.5, feedback=0.1, mix= 0.5),
      # Reverb(room_size=0.25),
      Reverb(room_size=0.75),
  ])
  input("Press enter to stop streaming...")

# The live AudioStream is now closed, and audio has stopped.

# Notes

# RuntimeError: The audio input device passed to AudioStream looks like a microphone, 
# and the output device looks like a speaker. This setup may cause feedback.
# To create an AudioStream anyways, pass `allow_feedback=True` to the AudioStream constructor.

# Try Windows
# MME/DirectX -> Realtek Digital Output (Realtek High Definition Audio) DX
# JackRouter
# ASIO4ALL v2
# M-Audio Fast Track Ultra ASIO"
# Is MIDI supported?
# Ableton Push
