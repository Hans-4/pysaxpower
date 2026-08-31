from pymodbus.client import ModbusTcpClient
from pysaxpower.sunspec.register import SunSpecRegister
from pysaxpower.sunspec.scalefactors import SunSpecScaleFactors

class PowerHomePlus:
    def __init__(
        self,
        ip: str,
        port: int =502,
        timeout: int =10
    ):
        self.client = ModbusTcpClient(
            host=ip,
            port=port,
            timeout=timeout
        )

        self.registers = SunSpecRegister()
        self.scalefactor = SunSpecScaleFactors()

        self.connect()


    def write_registers(self, values: dict[int, int | float]):

        for address, value in values.items():
            write_value = self.check_for_specific_datatype(address, value)

            self.client.write_register(address=address, value=write_value, device_id=100)


    def check_for_specific_datatype(self, address: int, value: int | float) -> int:
        if address == 40049:
            return self.apply_power_setpoint_offset(value)

        else:
            return int(value)


    @staticmethod
    def apply_power_setpoint_offset(raw: int | float) -> int:
        value = int(raw * 100)
        return 65536 + value if value < 0 else value


    @staticmethod
    def encode_int16(raw: int) -> int:
        return raw - 65536 if raw > 32767 else raw


    def get_raw_values(self, registers: dict[str, int]) -> dict[str, int] | None:
        """
        Enter a dictionary of register values and names and get the raw int16 values
        """
        values = {}
        for name, register in registers.items():
            raw_values = self.client.read_holding_registers(register, count=1, device_id=100)

            if raw_values.isError():
                pass
            else:
                values[name] = raw_values.registers[0]

        return values


    def get_formatted_values(self, registers: dict[str, int]) -> dict[str, int]:

        formatted_values = {}
        for name, register in registers.items():

            int16_value = self.client.read_holding_registers(
                register, count=1, device_id=100
            )
            value = self.encode_int16(
                int16_value.registers[0]
            )

            scale_factor_register = self.scalefactor.search_scale_factor(
                register
            )

            if scale_factor_register is not None:
                scale_factor = self.client.read_holding_registers(
                    scale_factor_register, count=1, device_id=100
                )

                formatted_scale_factor = self.encode_int16(scale_factor.registers[0])

                formatted_value = (value * 10 ** (formatted_scale_factor))
                formatted_values[name] = formatted_value

            else:
                formatted_values[name] = value

        return formatted_values


    def connect(self):
        self.client.connect()

    def close(self):
        self.client.close()
