# from pprint import pprint
import platform
from pathlib import Path

from mido import Message  # not part of Pedalboard, but convenient!
from pedalboard import Pedalboard, Reverb, load_plugin
from pedalboard.io import AudioFile

system = platform.system()

# Load a VST3 or Audio Unit plugin from a known path on disk:
# instrument = load_plugin("./VSTs/Magical8BitPlug2.vst3")
plugin_target = "Serum2"
if system == "Darwin":
    vst_path = "/Library/Audio/Plug-Ins/VST3/{}.vst3".format(plugin_target)
elif system == "Windows":
    vst_path = r"C:\Program Files\Common Files\VST3\{0}.vst3\Contents\x86_64-win\{0}.vst3".format(
        plugin_target
    )

instrument = load_plugin(
    plugin_name="Serum 2",
    path_to_plugin_file=vst_path,
)

# ValueError: Plugin 'Serum 2 FX' expects audio as input, but was provided MIDI messages.
# effect = instrument = load_plugin(
#     plugin_name="Serum 2 FX",
#     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Serum2.vst3\\Contents\\x86_64-win\\Serum2.vst3",
# )

# pprint(effect.parameters.keys())
# dict_keys([
#   'sc_hpf_hz', 'input_lvl_db', 'sensitivity_db',
#   'ratio', 'attack_ms', 'release_ms', 'makeup_db',
#   'mix', 'output_lvl_db', 'sc_active',
#   'full_bandwidth', 'bypass', 'program',
# ])

# Set the "ratio" parameter to 15
# effect.ratio = 15

# Render some audio by passing MIDI to an instrument:
sample_rate = 44100
audio = instrument(
    [Message("note_on", note=60), Message("note_off", note=60, time=5)],
    duration=5,  # seconds
    sample_rate=sample_rate,
)

# Apply effects to this audio:
# effected = effect(audio, sample_rate)

# ...or put the effect into a chain with other plugins:
# board = Pedalboard([effect, Reverb()])
# ...and run that pedalboard with the same VST instance!
# effected = board(audio, sample_rate)


with AudioFile("midi_to_audio_test.wav", "w", sample_rate, audio.shape[0]) as f:
    f.write(audio)

# TODO: try this workflow next
# with AudioFile('audio_fx_plugin_test.wav', 'w', sample_rate, effected.shape[0]) as f:
#     f.write(effected)
