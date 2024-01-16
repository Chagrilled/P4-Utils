# Mr Brocoli's save file compression script - I've not cleaned it up it at all
import zlib
import shutil
import glob
import os

file = r"C:\Users\mrbro\AppData\Roaming\Ryujinx\bis\user\save\0000000000000003\amongus\A\single.sav"
with open(file, "rb") as f:
    f = f.read()
    with open(file.replace("amongus\\", "0\\"), "wb") as w:
        joemama = []
        for i, _ in enumerate(f):
            if i > len(f)-5:
                break
            if f[i] == 0xC1 and f[i+1] == 0x83 and f[i+2] == 0x2A and f[i+3] == 0x9E:
                joemama.append(i+4)
        joemama.append(len(f)+4)
        for i in range(len(joemama)-1):
            x = zlib.compress(f[joemama[i]:joemama[i+1]-4])
            print(len(x))
            w.write(bytearray([0xC1, 0x83, 0x2A, 0x9E, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]))
            w.write(bytearray([len(x)&0xff, len(x)>>8&0xff]))
            w.write(bytearray([0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]))
            w.write(bytearray([len(x)&0xff, len(x)>>8&0xff]))
            w.write(bytearray([0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]))
            w.write(x)

