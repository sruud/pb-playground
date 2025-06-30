from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile
from pathlib import Path

# This is a temporary quick start script for experimentation
# Will be moved to src/examples/ in a later cleanup

# Make a Pedalboard object, containing multiple audio plugins:
board = Pedalboard([Chorus(), Reverb(room_size=1.0)])

# macOS
# say -o hello_world.aiff "Hello, World"
# convert to .wav with ffmpeg
# ffmpeg -y -i hello_world.aiff hello_world.wav

# TODO: either use this as a demo file in the root (clean comments)
# or update and create src/examples/ folder

# audio_path = Path(__file__).parents[2] / "audio_assets" / "hello_world.wav"
audio_path = Path("audio_assets") / "hello_world.wav"

# Open an audio file for reading, just like a regular file:
# with AudioFile('some-file.wav') as f:

with AudioFile(str(audio_path)) as f:
  
  # Open an audio file to write to:
  # with AudioFile('output.wav', 'w', f.samplerate, f.num_channels) as o:
  with AudioFile('hello_world_reverb.wav', 'w', f.samplerate, f.num_channels) as o:
  
    # Read one second of audio at a time, until the file is empty:
    while f.tell() < f.frames:
      chunk = f.read(f.samplerate)
      
      # Run the audio through our pedalboard:
      effected = board(chunk, f.samplerate, reset=False)
      
      # Write the output to our output file:
      o.write(effected)
