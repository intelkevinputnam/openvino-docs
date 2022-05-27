import os
import os.path
from pathlib import Path
from shutil import copyfile

fileExtension = ".md"
files = []
buildDir = "model_zoo"

intelModelPath = "open_model_zoo/models/intel/"
publiModelPath = "open_model_zoo/models/public/"
model_prefix = "omz_models_model_"
demoPath = "open_model_zoo/demos/"
adapterPath = "open_model_zoo/demos/common/python/openvino/model_zoo/model_api/adapters/"

def getIntelModels():
    # source = os.path.join(intelModelPath,"index.md")
    # target = os.path.join(buildDir,"omz_models_group_intel.md")
    # copyfile(source,target)
    # source = os.path.join(intelModelPath,"device_support.md")
    # target = os.path.join(buildDir,"omz_models_intel_device_support.md")
    # copyfile(source,target)
    for d in os.listdir(intelModelPath):
        modelPath = os.path.join(intelModelPath,d)
        if os.path.isdir(modelPath):
            readmePath = os.path.join(intelModelPath,"README.md")
            finalPath = os.path.join(buildDir,model_prefix+d+".md")
            # copyfile(readmePath,finalPath)
            print(finalPath)

    


def getFiles():
    Path(buildDir).mkdir(parents=True, exist_ok=True)
    for dirpath, dirnames, filenames in os.walk(targetDIR):
        for filename in [f for f in filenames if f.endswith(fileExtension)]:
                filepath = os.path.join(dirpath,filename)
                print(filepath)
                newFilePath = os.path.join(buildDir,filename)
                #copyfile(filepath,newFilePath)

getIntelModels()