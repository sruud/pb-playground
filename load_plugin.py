import platform

from pedalboard import load_plugin

system = platform.system()

if system == "Darwin":
    # VST3
    # PFM - SimpleEQ project vst3
    # plugin = load_plugin(path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/SimpleEQ.vst3")

    # Loading a specific plugin from a multi-plugin package like Xfer Records

    # Serum 2
    # plugin = load_plugin(plugin_name="Serum 2", path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Serum2.vst3")

    # Serum 2 FX
    # plugin = load_plugin(plugin_name="Serum 2 FX", path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Serum2.vst3")

    # Antares
    plugin = load_plugin(
        path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Auto-Key.vst3"
    )

    # Components
    # plugin = load_plugin(path_to_plugin_file="/Library/Audio/Plug-Ins/Components/ARIA Player AU.component")

elif system == "Windows":
    # TODO: refactor w/ from pathlib import Path
    # Antares
    plugin = load_plugin(
        path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Auto-Key.vst3",
    )

    # Custom Location
    # plugin = load_plugin(
    #     path_to_plugin_file="C:\\Program Files\\VstPlugins\\SimpleEq.vst3",
    # )

    # plugin = load_plugin(
    #     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\ARIA Player.vst3\\Contents\\x86_64-win\\ARIA Player.vst3",
    # )

    # Loading a specific plugin from a multi-plugin package like Xfer Records

    # Serum 2
    # plugin = load_plugin(
    #     plugin_name="Serum 2",
    #     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Serum2.vst3\\Contents\\x86_64-win\\Serum2.vst3",
    # )

    # Serum 2 FX
    # plugin = load_plugin(
    #     plugin_name="Serum 2 FX",
    #     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Serum2.vst3\\Contents\\x86_64-win\\Serum2.vst3",
    # )

else:
    raise NotImplementedError("Unsupported platform")

plugin.show_editor()

# TODO: capture screenshot of window
# pyautogui pygetwindow

# macOS Accessibility Inspector doesn't seem to allow me to inspect the window of the Python process
# Menu bar name is Pedalboard
