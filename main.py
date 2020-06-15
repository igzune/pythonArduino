import pyfirmata2

DELAY = 1
PORT = pyfirmata2.Arduino.AUTODETECT

board = pyfirmata2.Arduino(PORT)

board.samplingOn(100)
analog0 = board.analog[0]
analog1 = board.analog[1]

analog0.enable_reporting()
analog1.enable_reporting()

while True:
    print('Nivel de Luz Actual: ' + str(analog0.read()))
    print('Sensor de humedad' + str(analog1.read()))
    board.pass_time(DELAY)
