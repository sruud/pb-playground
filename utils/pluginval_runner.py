import platform
import subprocess
from pathlib import Path

system = platform.system()

if system == "Darwin":
    PLUGINVAL_BINARY = Path("pluginval/pluginval.app/Contents/MacOS/pluginval")

elif system == "Windows":
    PLUGINVAL_BINARY = Path(
        r"C:\ProgramData\chocolatey\lib\pluginval\tools\pluginval.exe"
    )

current_file_path = Path(__file__).resolve()
root_path = current_file_path.parents[1]
log_output = root_path.joinpath(root_path, "pluginval/bin")


# TODO: Add strictness level and timeout
def run_pluginval(plugin_path: str) -> subprocess.CompletedProcess:
    cmd = [
        str(PLUGINVAL_BINARY),
        "--validate-in-process",
        "--output-dir",
        str(log_output),
        str(plugin_path),
    ]

    result = subprocess.run(cmd)
    return result


# Working examples
# run_pluginval("/Library/Audio/Plug-Ins/VST3/SimpleEQ.vst3")
# run_pluginval("C:\Program Files\VstPlugins\SimpleEq.vst3")
