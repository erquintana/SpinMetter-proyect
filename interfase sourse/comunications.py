import serial
import time
import math
import sys
import glob


class comunications:
    def __init__(self):
        print("Preparing to save recived data from Serial port")
        COMport = self.serial_ports()
        bautrate = 19200

        arduino = serial.Serial(COMport, bautrate)
        arduino.flush()
        arduino.close()

        arduino.open()
        time.sleep(1)

        f = open("activity_data.csv", "w")
        print("Ready for data recording...")
        print("...\n...\n...")
        values0 = ","
        while (values0.split()[0] != " FINISHED"):
            values0 = arduino.readline().decode('utf-8')
            f = open("activity_data.csv", "a")
            f.write(values0)

        print("Data recording is done, worked perfect!")
        f.close()
        arduino.close()
        sys.exit(0)

    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = ''
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result = port
            except (OSError, serial.SerialException):
                pass
        return result


myCom = comunications()
