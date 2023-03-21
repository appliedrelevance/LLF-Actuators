#                  - OpenPLC Python SubModule (PSM) -
# 
# PSM is the bridge connecting OpenPLC core to Python programs. PSM allows
# you to directly interface OpenPLC IO using Python and even write drivers 
# for expansion boards using just regular Python.
#
# PSM API is quite simple and just has a few functions. When writing your
# own programs, avoid touching on the "__main__" function as this regulates
# how PSM works on the PLC cycle. You can write your own hardware initialization
# code on hardware_init(), and your IO handling code on update_inputs() and
# update_outputs()
#
# To manipulate IOs, just use PSM calls psm.get_var([location name]) to read
# an OpenPLC location and psm.set_var([location name], [value]) to write to
# an OpenPLC location. For example:
#     psm.get_var("QX0.0")
# will read the value of %QX0.0. Also:
#     psm.set_var("IX0.0", True)
# will set %IX0.0 to true.
#
# Below you will find a simple example that uses PSM to switch OpenPLC's
# first digital input (%IX0.0) every second. Also, if the first digital
# output (%QX0.0) is true, PSM will display "QX0.0 is true" on OpenPLC's
# dashboard. Feel free to reuse this skeleton to write whatever you want.

#import all your libraries here
import psm
import time
import libioplus


def hardware_init():
    #Insert your hardware initialization code in here
    psm.start()

def update_inputs():
   #Read card stack level 0 inputs
   val = libioplus.getOpto(0)
   for i in range(8):
       var_state = False
       if val & (1 << i) != 0:
           var_state = True
       psm.set_var("IX0." + str(i), var_state)#move OPTO state to IX0.0 .. IX0.7
   for i in range(8):
       valAdc = libioplus.getAdcV(0, i+1)
       psm.set_var("IW" + str(i), int(1000 * valAdc)) #Update adc in value (mV) IW0 .. IW7 
   #Read card stack level 1 inputs
 #move OPTO state to IX1.0 .. IX1.7
  #Update adc in value (mV) IW8 .. IW15     
    
def update_outputs():
   # Update outputs for card stack level 0 
   val = 0
   for i in range(8):
       a = psm.get_var("QX0." + str(i))# relays QX0.0..QX0.7
       if a == True:
           val+= 1 << i
   libioplus.setRelays(0, val)
   for i in range(4):
       val = psm.get_var("QW" + str(i))# DAC value in mV QW0..QW3
       if val < 0:
           val = 0
       if val > 10000:
           val = 10000
       libioplus.setDacV(0, i+1, val/1000.0)
   # Update outputs for card stack level 1 
  



if __name__ == "__main__":
    hardware_init()
    while (not psm.should_quit()):
        update_inputs()
        update_outputs()
        time.sleep(0.1) #You can adjust the psm cycle time here
    psm.stop()
