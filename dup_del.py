import os.path
from os import remove
from pathlib import Path
# calculate file size in KB, MB, GB
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

directory = Path(__file__).parent.resolve()
file_sizes = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        f_size = os.path.getsize(f)
        x = convert_bytes(f_size)
        print('file size is', x)
        if x in file_sizes:
            print(f'file \"{filename}\" is most likely a duplicate')
            remove(f)
            continue
        file_sizes.append(x) 


