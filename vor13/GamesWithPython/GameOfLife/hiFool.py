import sys
import time

import os

for i in ["Hi", "You", "Fool\n"]:
	sys.stdout.write("\r" + i)
	sys.stdout.flush()
	time.sleep(1)



for i in range(6):
	sys.stdout.write(str(i))
	sys.stdout.flush()
	time.sleep(0.5)
	sys.stdout.write("\r\r")

for i in range(15):
	sys.stdout.write(str(i)+'\n')


time.sleep(2)

for i in range(10):
	sys.stdout.write('\r')
	sys.stdout.write('\b')

time.sleep(1)

sys.stdout.write('bla' * 20)
sys.stdout.write('\n')

time.sleep(1)

os.system('cls')






