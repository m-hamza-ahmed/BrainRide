import bluetooth, subprocess
import pdb

deviceName = 'BRAINSENSE 17'
deviceAddress = '00:18:E4:36:5C:EC'
port = 1
devicePassword = "1234"
deviceFound = False

while True:
    nearbyDevices = bluetooth.discover_devices(duration=4,lookup_names=True, flush_cache=True, lookup_class=False)
    if len(nearbyDevices) > 0:
        for device in nearbyDevices:
            if device[1] == deviceName:
                print ("Found device!\nConnecting...")
                deviceFound = True
                break
    if deviceFound == True:
        break
    else:
        print ("Not found. Trying again...")

# kill any "bluetooth-agent" process that is already running
subprocess.call("sudo killall bluetooth-agent", shell=True)
print ("All similar processes killed...")

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + devicePassword + " &",shell=True)
print ("Bluetooth agent started...")

# Now, connect in the same way as always with PyBlueZ
try:
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((deviceAddress,port))
except bluetooth.btcommon.BluetoothError as err:
    print (err)
    exit()
print ("Bluetooth agent connected to device...")
print(s.recv(1))

