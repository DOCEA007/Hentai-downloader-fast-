import os.path
from pathlib import Path
# calculate file size in KB, MB, GB
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0



for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        f_size = os.path.getsize(r'E:\\Hentai-downloader-fast-\\README.md')
        x = convert_bytes(f_size)
        print('file size is', x)