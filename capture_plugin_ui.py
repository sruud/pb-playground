import os
import platform
import time
from threading import Event, Thread

import pyautogui
import pygetwindow as gw
from pedalboard import load_plugin

system = platform.system()

if system == "Darwin":
    # VST3
    # PFM - SimpleEQ project vst3
    plugin = load_plugin(
        path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/SimpleEQ.vst3"
    )

    # Loading a specific plugin from a multi-plugin package like Xfer Records

    # Serum 2
    # plugin = load_plugin(plugin_name="Serum 2", path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Serum2.vst3")

    # Serum 2 FX
    # plugin = load_plugin(plugin_name="Serum 2 FX", path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Serum2.vst3")

    # Antares
    # plugin = load_plugin(
    #     path_to_plugin_file="/Library/Audio/Plug-Ins/VST3/Auto-Key.vst3"
    # )

    # Components
    # plugin = load_plugin(path_to_plugin_file="/Library/Audio/Plug-Ins/Components/ARIA Player AU.component")

elif system == "Windows":
    # TODO: refactor w/ from pathlib import Path
    # Antares
    # plugin = load_plugin(
    #     path_to_plugin_file="C:\\Program Files\\Common Files\\VST3\\Auto-Key.vst3",
    # )

    # Custom Location
    plugin = load_plugin(
        path_to_plugin_file="C:\\Program Files\\VstPlugins\\SimpleEq.vst3",
    )

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

# An example of how to programmatically close an editor window::
close_window_event = Event()


def other_thread():
    try:
        if system == "Darwin":
            # not implemented on macOS
            # app_window = gw.getWindowsWithTitle("Your Application Title")[0]
            time.sleep(2)
            os.system(
                "screencapture -l$(osascript -e 'tell app \"Python\" to id of window 0') plugin_target.png"
            )
        elif system == "Windows":
            time.sleep(3)
            app_window = gw.getWindowsAt(10, 10)[0]

    except IndexError:
        print(
            "Window not found. Please ensure the application is open and the title is correct."
        )
        exit()

    if system == "Windows":
        app_window.activate()

        # Get plugin window's coords
        left, top, width, height = (
            app_window.left,
            app_window.top,
            app_window.width,
            app_window.height,
        )

        screenshot_image = pyautogui.screenshot(
            region=(left + 15, top + 30, width - 23, height - 38)
        )

        screenshot_image.save("app_screenshot.png")

        print(f"Screenshot of '{app_window.title}' saved as 'app_screenshot.png'")

    close_window_event.set()


thread = Thread(target=other_thread)
thread.start()

# This will block until the other thread calls .set():
plugin.show_editor(close_window_event)
