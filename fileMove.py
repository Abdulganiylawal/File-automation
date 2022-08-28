import os
import shutil

# creating a file using python
directory = "{}"
parentDirectory = "/Users/lawalabdulganiy/Downloads"

sourceFolder = "/Users/lawalabdulganiy/Downloads"
destinationFolder = "/Users/lawalabdulganiy/Downloads"

myFiles = {'pdf': 'Pdf File', 'png': 'Picture File', 'svg': 'Svg file',
           'jpeg': 'Picture File', 'pkt': 'PacketTracer File', 'dmg': 'Application File', 'mp4': 'Video File', 'docx': 'word Files', 'ppt': 'powerpoint File', 'xlsx': 'Excel FIles', 'pptx': 'powerpoint File', 'zip': 'Zipped Files', '7z': 'Zipped Files', }


def File_Move(myFiles):
    for fileName in os.listdir(sourceFolder):
        for el in myFiles.keys():
            if fileName.endswith(el):
                source = os.path.join(sourceFolder, fileName)
                destination = os.path.join(
                    destinationFolder, myFiles[el])
                shutil.move(source, destination)
                print(f"{fileName} has moved")


for el in myFiles.keys():
    path = os.path.join(parentDirectory, directory.format(myFiles[el]))
    print(path)
    if os.path.exists(path):
        File_Move(myFiles)
        continue
    os.mkdir(path)
    File_Move(myFiles)
