import zlib
import shutil
import glob
import os

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(os.getcwd() + "\\0")

for file in full_file_paths:
    if ".sav" in file:
        joemama = []
        with open(file, "rb") as f:
            f = f.read()
            os.makedirs(os.path.dirname(file.replace("0\\", "amongus\\")), exist_ok=True)
            with open(file.replace("0\\", "amongus\\"), "wb") as w:
                for i, _ in enumerate(f):
                    if i > len(f)-5:
                        break
                    if f[i] == 0xC1 and f[i+1] == 0x83 and f[i+2] == 0x2A and f[i+3] == 0x9E:
                        x = zlib.decompress(f[i+48:])
                        w.write(bytearray([0xC1, 0x83, 0x2A, 0x9E]))
                        w.write(x)
            
            
    #with open(, "rb") as f:
    #        f = f.read()
    #        x = zlib.compress(f)
    #        with open(s + "-glumb.sav", "wb") as w:
    #            w.write(joemama)
    #            w.write(x)

