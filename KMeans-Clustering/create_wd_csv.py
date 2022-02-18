"""
    This file contains the code for creating N number of Wireless Devices.
    Author: Papu Sethi
    Date: 16 Jan 2022
"""

import random

my_file = open("wireless_devices.csv", "a")

header = "WD_NAME,X_LOC,Y_LOC\n"
my_file.write(header)

for number in range(1, 51):
    x = str(random.randint(0, 100))
    y = str(random.randint(0, 100))
    wd_name = "WD" + str(number)
    entry = wd_name + "," + x + "," + y + "\n"
    my_file.write(entry)

my_file.close()
