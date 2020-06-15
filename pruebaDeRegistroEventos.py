import logging
import pyfirmata2

DELAY = 10
PORT = pyfirmata2.Arduino.AUTODETECT

board = pyfirmata2.Arduino(PORT)

board.samplingOn(10000)
analog0 = board.analog[0]
analog1 = board.analog[1]

analog0.enable_reporting()
analog1.enable_reporting()

# initialize the log settings
logging.basicConfig(format='%(asctime)s'+'|'+'%(message)s', filename='app.log',level=logging.INFO)

try:
    while True:
        logging.info('Nivel de Luz Actual: ' + str(analog0.read()))
        logging.info('Sensor de humedad' + str(analog1.read()))
        board.pass_time(DELAY)
except IOError as e:
    logging.error('Error occurred ' + str(e))
