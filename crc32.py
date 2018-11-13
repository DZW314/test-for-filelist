from zlib import crc32
import sys
import glob
import logging
def getCrc32(filename): # calculate crc32
    with open(filename, 'rb') as f:
        return crc32(f.read())

#log setting
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='info.log', level=logging.DEBUG, format=LOG_FORMAT)

# if len(sys.argv) < 2:
#     print('You must enter the file')
#     exit(1)
# elif len(sys.argv) > 2:
#     print('Only one file is permitted')
#     exit(1)

#filename = sys.argv[1]
#search all files and store in an array
logging.info("Start search all files in Packages.")
listFile = []
listuxz = glob.glob("./*/*.uxz")
listbin = glob.glob("./*/*.bin")
listtgz = glob.glob("./*/*.tgz")
listexe = glob.glob("./*/*.exe")
listFile.extend(listuxz)
listFile.extend(listbin)
listFile.extend(listtgz)
listFile.extend(listexe)
logging.info("Finish searching.")
#list sort
logging.info("Sorting the list...")
sortFile = sorted(listFile)
for n in sortFile:
    logging.info(n)
#for n in list:
#    print('{:s} {:8} {:x}'.format( n,' crc32: ', getCrc32(n)))

# result =  'crc32.txt'
# f = open ('./' + result,'w')
# for n in list:
#     str = n;
#     crc = format(getCrc32(n), 'x')
#     print('{:s} {:8} {:x}'.format( n,' crc32: ', getCrc32(n)))
#     f.write(str + ' page_crc32: ' + crc + '\n')
# f.close()
