import os
import os.path
from pathlib import Path
from shutil import copyfile

fileExtension = ".ipynb"
files = []
buildDir = "notebooks"
targetDIR = "openvino_notebooks"


def getFiles():
    Path(buildDir).mkdir(parents=True, exist_ok=True)
    for dirpath, dirnames, filenames in os.walk(targetDIR):
        for filename in [f for f in filenames if f.endswith(fileExtension)]:
                filepath = os.path.join(dirpath,filename)
                newFilePath = os.path.join(buildDir,filename)
                print(newFilePath)
                copyfile(filepath,newFilePath)

getFiles()