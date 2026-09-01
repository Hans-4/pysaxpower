# PySaxPower

**Python package to read and write data from/to SAX Power Home Plus batteries.**

---

## Overview

Here’s a more polished and concise version of your text with improved clarity, flow, and grammar:

---

With **PySaxPower**, you can read Modbus registers from **SAX Power Home Plus** batteries. 
The package is divided into two protocol implementations: **SunSpec** and **Basic**. 
The **Basic** protocol supports read-only operations. 
View the [Manual](https://sax-power.net/download/Handbuch_SAX_Home_Plus_7,7_EN.pdf) for more information.

> **Note:**
> Due to a firmware bug in SAX devices, **only the SunSpec protocol supports writing to registers**.
> To use this feature, ensure your battery has at least **Master V61** and **Gateway V54** firmware versions. If not, you may need to update your firmware or contact **Customer Support**.

---

## Supported Devices


| **Device**                        | **Documentation**                                                                |
| --------------------------------- |----------------------------------------------------------------------------------|
| Power Home Plus 5.8 kWh / 7.7 kWh | [Product page](https://sax-power.net/download/Handbuch_SAX_Home_Plus_7,7_EN.pdf) |


---

## Installation

```bash
pip install PySaxPower
```

---

## Usage

### Sunspec

#### Read register
```python
from pysaxpower import PowerHomePlusSunspec
from pysaxpower import SunSpecRegister

device = PowerHomePlusSunspec("192.168.178.60")

register = SunSpecRegister()

read_values = {
    "Soc": register.CurrentSoC,
    "Battery Power": register.ActivePower_Storage_Sum,
    "Grid Power": register.ActiveGridPower,
}

values = device.get_formatted_values(read_values)
```

#### Write register
```python
from pysaxpower import PowerHomePlusSunspec
from pysaxpower import SunSpecRegister

device = PowerHomePlusSunspec("192.168.178.60")

register = SunSpecRegister()

write_values = {
    register.ControlMode: 1
}

device.write_registers(write_values)
```

---

### Basic
```python
from pysaxpower import PowerHomePlusBasic
from pysaxpower import BasicRegister

device = PowerHomePlusBasic("192.168.178.60")

register = BasicRegister

read_values = {
    "Operating Mode": register.OperatingMode,
    "Soc": register.SOC,
    "Battery Power": register.ActivePower,
    "Grid Power": register.GridPower,
}

values = device.get_values(read_values)
print(values)

device.close()
```