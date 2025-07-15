# from pprint import pprint
import platform

from mido import Message  # not part of Pedalboard, but convenient!
from pedalboard import Pedalboard, Reverb, load_plugin
from pedalboard.io import AudioFile

system = platform.system()

# Load a VST3 or Audio Unit plugin from a known path on disk:
# instrument = load_plugin("./VSTs/Magical8BitPlug2.vst3")
plugin_target = "Serum2"
if system == "Darwin":
    vst_path = "/Library/Audio/Plug-Ins/VST3/{}.vst3".format(plugin_target)
    vst_effect_path = "/Library/Audio/Plug-Ins/VST3/ValhallaSupermassive.vst3"
elif system == "Windows":
    vst_path = r"C:\Program Files\Common Files\VST3\{0}.vst3\Contents\x86_64-win\{0}.vst3".format(
        plugin_target
    )
    vst_effect_path = r"C:\Program Files\Common Files\VST3\ValhallaSupermassive.vst3"

instrument = load_plugin(
    plugin_name="Serum 2",
    path_to_plugin_file=vst_path,
)

# effect = load_plugin(
#     plugin_name="Serum 2 FX",
#     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Serum2.vst3\\Contents\\x86_64-win\\Serum2.vst3",
# )

# TODO: find best way to load preset - testing to see if this works first
# parameter_values= try mix 100 with high delay or something
# Note the default does produce an audible effect
effect = load_plugin(
    plugin_name="ValhallaSupermassive",
    path_to_plugin_file=vst_effect_path,
)

# pprint(effect.parameters.keys())
# dict_keys([
# 'mix',
# 'delaysync',
# 'delaynote',
# 'delay_ms',
# 'delaywarp',
# 'clear',
# 'feedback',
# 'density',
# 'width',
# 'lowcut',
# 'highcut',
# 'modrate',
# 'moddepth',
# 'mode',
# 'reserved1',
# 'reserved2',
# 'reserved3',
# 'reserved4',
# 'bypass']
# )


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
effected = effect(audio, sample_rate)

# ...or put the effect into a chain with other plugins:
# board = Pedalboard([effect, Reverb()])
# ...and run that pedalboard with the same VST instance!
# effected = board(audio, sample_rate)

# with AudioFile("midi_to_audio_test.wav", "w", sample_rate, audio.shape[0]) as f:
#     f.write(audio)

# TODO: try this workflow next
with AudioFile(
    "audio_effects_plugin_test.wav", "w", sample_rate, effected.shape[0]
) as f:
    f.write(effected)
