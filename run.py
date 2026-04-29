import sys
import subprocess
from pathlib import Path
import os

if os.environ.get("RUNNING_EXE"):
    sys.exit()
os.environ["RUNNING_EXE"] = "1"

APP = Path(__file__).parent / "app" / "app.py"

print("Launching Streamlit...")

cmd = [
    sys.executable,
    "-m",
    "streamlit",
    "run",
    str(APP),
    "--server.headless=true",
    "--server.runOnSave=false",
    "--server.fileWatcherType=none",
    "--server.port=8501"
]

proc = subprocess.Popen(cmd)

input("Streamlit lanzado. Si se cierra aquí, hay error.")