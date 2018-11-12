from zlib import crc32
import sys

def getCrc32(filename): # calculate crc32
    with open(filename, 'rb') as f:
        return crc32(f.read())
if len(sys.argv) < 2:
    print('You must enter the file')
    exit(1)
elif len(sys.argv) > 2:
    print('Only one file is permitted')
    exit(1)

filename = sys.argv[1]
print('{:8} {:x}'.format('crc32:', getCrc32(filename)))
