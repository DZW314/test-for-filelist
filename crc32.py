from zlib import crc32
import sys
import glob
def getCrc32(filename): # calculate crc32
    with open(filename, 'rb') as f:
        return crc32(f.read())
# if len(sys.argv) < 2:
#     print('You must enter the file')
#     exit(1)
# elif len(sys.argv) > 2:
#     print('Only one file is permitted')
#     exit(1)

#filename = sys.argv[1]
list = []
listuxz = glob.glob("./*.uxz")
listbin = glob.glob("./*.bin")
listtgz = glob.glob("./*.tgz")
listexe = glob.glob("./*.exe")
list.extend(listuxz)
list.extend(listbin)
list.extend(listtgz)
list.extend(listexe)
for n in list:
    print(n)

#print('{:8} {:x}'.format('crc32:', getCrc32(filename)))
