# PySaxPower

**A Python package for reading data from SAX Power Home Plus batteries.**

---

## Overview

With `PySaxPower` you can read the modbus register from the SAX Power Home Plus batteries.

> **Note:** Due to a firmware bug in SAX devices, **writing data to the battery is currently unsupported**. This limitation will be addressed in a future update once SAX resolves the issue. For more details, see the [EVCC GitHub discussion](https://github.com/evcc-io/evcc/discussions/22155).

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

```python
from pysaxpower import PowerHomePlus

device = PowerHomePlus("192.168.178.60")

level, power, grid_power = device.read_register()

print(f"Battery Level: {level}% | Power: {power}W | Grid Power: {grid_power}W")
```