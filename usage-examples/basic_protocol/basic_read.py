from pysaxpower import BasicRegister, PowerHomePlusBasic


"""
Basic Protocol: Read SoC, Battery Power, Grid Power from PowerHomePlus.

Registers:
  SOC: State of Charge (%)
  ActivePower: Battery power (W)
  GridPower: Grid power (W)
"""

register = BasicRegister

read_values = {
    "Soc": register.SOC,
    "Battery Power": register.ActivePower,
    "Grid Power": register.GridPower,
}

with PowerHomePlusBasic("192.168.178.60") as device:

    values = device.get_values(read_values)
    print(values)

    device.close()