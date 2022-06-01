import os
import os.path
from pathlib import Path
from shutil import copyfile

fileExtension = ".md"
files = []
buildDir = "model_zoo"

intel = {"name":"intel","dir":"openvino/open_model_zoo/models/intel/","pre":"omz_models_","pre_name":"intel_","parent":"index.md"}
public = {"name":"public","dir":"openvino/open_model_zoo/models/public/","pre":"omz_models_","pre_name":"public_","parent":"index.md"}
demos = {"name":"demos","dir":"openvino/open_model_zoo/demos/","pre":"omz_demos_","pre_name":"","parent":"README.md"}
adapter = {"name":"adapter","dir":"openvino/open_model_zoo/demos/common/python/openvino/model_zoo/model_api/adapters/","pre":"omz_model_api_","pre_name":"","parent":"ovms_adapter.md"}
modelContent = [intel,public,demos,adapter]

tocs = {}

def getZoos():
    for thing in modelContent:
        tocs[thing["name"]]=[]
        for d in os.listdir(thing["dir"]):
            modelPath = os.path.join(thing["dir"],d)
            if os.path.isdir(modelPath):
                if thing["name"] == "demos":
                    for d2 in os.listdir(modelPath):
                        childPath = os.path.join(modelPath,d2)
                        if os.path.isdir(childPath):
                            getreadme(childPath,tocs[thing["name"]],thing["pre"]+thing["pre_name"]+d+"_"+d2)
                else:
                    getreadme(modelPath,tocs[thing["name"]],thing["pre"]+thing["pre_name"]+d)
            else:
                if d.endswith(".md"):
                    if d == thing["parent"]:
                        fname = "index.md"
                    else:
                        fname = d
                    filePath = os.path.join(thing["dir"],d)
                    finalPath = os.path.join(buildDir,thing["pre"]+thing["pre_name"]+fname)
                    if os.path.isfile(filePath):
                        #copyfile(filePath,finalPath)
                        print(filePath)
                        if d != thing["parent"]:
                            tocs[thing["name"]].append(finalPath)

def getreadme(sourcepath,toc,filename):
    readmePath = os.path.join(sourcepath,"README.md")
    if os.path.isfile(readmePath):
        finalPath = os.path.join(buildDir,filename + ".md")
        #copyfile(readmePath,finalPath)
        print(readmePath)
        toc.append(finalPath)



def appendTocs():
    for toc in tocs:
        if len(tocs[toc]) > 0:
            rst = "\n\n```{toc-tree}\n---\nhidden: True\n---\n"
            for item in tocs[toc]:
                rst  += item + "\n"
            rst += "```"
            #print(rst)
            the_thing = {}
            for thing in modelContent:
                if thing["name"] == toc:
                    the_thing = thing
            parentFile = os.path.join(buildDir,the_thing["pre"] + the_thing["pre_name"] + "index.md")
            #print("parent file: " + parentFile)
            #with open(parentFile,'a') as f:


Path(buildDir).mkdir(parents=True, exist_ok=True)
getZoos()
appendTocs()