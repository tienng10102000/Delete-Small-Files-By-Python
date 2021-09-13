import os, os.path
from random import randrange
import time
rootpics = "M:\\Pictures\\AngelinaJolie\\PitchPerfect"
rootvids = "M:\\Pictures\\AngelinaJolie\\VictoriaSecrect"

for rootpic, _, filepics in os.walk("M:\\Pictures\\AngelinaJolie\\PitchPerfect"):
    for pic in filepics:
        fullpathpics = os.path.join(rootpic, pic)
        try:
            if os.path.getsize(fullpathpics) < 45 * 1024:   #size = 1024 Byte *1024 Byte = 1KB * 45 Bye = 45KB
                print(fullpathpics)
                os.remove(fullpathpics)
        except WindowsError:
            print("Error")+fullpathpics

for rootvid, _, filevids in os.walk("M:\\Pictures\\AngelinaJolie\\VictoriaSecrect"):
    for vid in filevids:
        fullpathvids = os.path.join(rootvid,vid)
        try:
            if os.path.getsize(fullpathvids) < 2.21 * 1024 * 1024: #size = 1024 Byte *1024 Byte = 1KB * 1024 Bye = 1024 KB = 1MegaBite  
                print(fullpathvids)
                os.remove(fullpathvids)
        except WindowsError:
            print("ERROR")+fullpathvids

valuechangename1 = randrange(0,99999999)
valuechangename2 = randrange(0,99999999)
valuechangename3 = randrange(0,99999999)
print(valuechangename1)
print(valuechangename2)
print(valuechangename3)
time.sleep(5.5)