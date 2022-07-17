import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
servo = board.get_pin('d:5:s')

while True:
  #servo.write(input())
  for i in range(0,180):
    servo.write(i)
    print(i)
    time.sleep(0.2)
  for i in range(180,-1, -1):
    servo.write(i)
    print(i)
    time.sleep(0.2)
