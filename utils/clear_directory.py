import shutil
from os import path
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1].resolve()  # converterApi root directory
TARGET_PATH = Path(ROOT, 'yolov5/runs/detect/exp')


def clear_detect_dir():
    if path.exists(TARGET_PATH):
        shutil.rmtree(TARGET_PATH)

        print("Directory removed: " + str(TARGET_PATH))
    else:
        print("Directory does not exists.")
