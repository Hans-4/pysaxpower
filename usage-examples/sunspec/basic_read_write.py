import time

from pysaxpower import PowerHomePlusSunspec, SunSpecRegister


"""
SunSpec: Read SoC/Power values, write ControlMode (1) and PowerTarget (10%).
"""

device = PowerHomePlusSunspec("192.168.178.60") #Enter your ip

register = SunSpecRegister()

read_values = {
    "Soc": register.CurrentSoC,
    "Battery Power": register.ActivePower_Storage_Sum,
    "Grid Power": register.ActiveGridPower,
}

try:
    device.write_registers({register.ControlMode: 1}) #Set battery in control mode
    while True:
        values = device.get_formatted_values(read_values)

        print(values)

        device.write_registers({register.PowerTarget: 10}) #Power target 10% of reference power

        time.sleep(0.5)

except KeyboardInterrupt:
    device.close()