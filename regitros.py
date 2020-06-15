import logging

try:
    logging.info('Trying to open the file')
    filePointer = open('appFile','r')
    try:
        logging.info('Trying to read the file content')
        content = filePointer.readline()
    finally:
        filePointer.close()
except IOError as e:
    logging.error('Error occurred ' + str(e))
