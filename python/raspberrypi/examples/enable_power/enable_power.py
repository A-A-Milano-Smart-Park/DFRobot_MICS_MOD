# -*- coding:utf-8 -*-
""" 
  @file enable_power.py
  @brief Enable the power, and the information is printed on the serial port.
  @n step: we must first determine the i2c device address, will dial the code switch A0, A1 (MICS_ADDRESS_0 for [0 0]), (MICS_ADDRESS_1 for [1 0]), (MICS_ADDRESS_2 for [0 1]), (MICS_ADDRESS_3 for [1 1]).
  @n       Then wait for the calibration to succeed.
  @n       The calibration time is approximately three minutes.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author      [ZhixinLiu](zhixin.liu@dfrobot.com)
  version  V1.2
  date  2021-06-18
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_MicsSensor
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from DFRobot_MICS import *

CALIBRATION_TIME = 0x03            # calibration time
I2C_BUS          = 0x01            # default use I2C1
'''
   # The first  parameter is to select i2c0 or i2c1
   # The second parameter is the i2c device address
   # The default address for i2c is MICS_ADDRESS_0
   # MICS_ADDRESS_0                 = 0x75
   # MICS_ADDRESS_1                 = 0x76
   # MICS_ADDRESS_2                 = 0x77
   # MICS_ADDRESS_3                 = 0x78
'''
mics = DFRobot_MICS_I2C (I2C_BUS ,MICS_ADDRESS_0)

def loop():
  '''
    # Gets the power mode of the sensor
    # The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    # The data obtained in sleep mode is wrong
  '''
  if mics.get_power_mode() == SLEEP_MODE:
    mics.wakeup_mode()
    print "sleep mode,   wake up sensor success!"
  else:
    mics.sleep_mode()
    print "wake up mode, sleep sensor success!"
  time.sleep(3)

if __name__ == "__main__":
  while True:
    loop()