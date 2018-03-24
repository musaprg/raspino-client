#!/usr/bin/env python3

import subprocess
import serial
import sys

def main():
    #subprocess.run("echo \"Hello World\"", shell=True, check=True)
    ser = serial.Serial(
    port = "/dev/ttyUSB0",
    baudrate = 115200,
    )

    with open('./dst/kernel8.img', 'rb') as f:
        data = f.read()
    psize = str(len(data))
    ser.write(str()).encode('utf-8')) # send program byte size at first
    ser.write("\n".encode('utf-8'))
    ser.write(data) # next send program data
    while True:
        print(ser.read().decode('utf-8'))

    ser.close()

if __name__ == '__main__':
    main()
