from pymodbus.client import ModbusTcpClient

class PowerHomePlusBasic:
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

        self.connect()

    @staticmethod
    def apply_offset(value: int):
        offset = 16384
        return value - offset

    def get_values(self, addresses: dict[str, int]) -> dict[str, int]:

        results = {}

        for name, value in addresses.items():
            raw_value = self.client.read_holding_registers(address=value, count=1, device_id=64)

            if not raw_value.isError():
                if value != 45 and value != 46:
                    decoded_value = self.apply_offset(raw_value.registers[0])
                    results[name] = decoded_value
                else:
                    results[name] = raw_value.registers[0]
            else:
                print(f"Error reading {name}: {value} from Sax Power Home Plus Battery")
                results[name] = None

        return results


    def get_raw_values(self, addresses: dict[str, int]) -> dict[str, int]:
        results = {}

        for name, value in addresses.items():
            raw_value = self.client.read_holding_registers(address=value, count=1, device_id=64)

            if not raw_value.isError():
                results[name] = raw_value.registers[0]
            else:
                print(f"Error reading {name}: {value} from Sax Power Home Plus Battery")
                results[name] = None

        return results


    def connect(self):
        self.client.connect()

    def close(self):
        self.client.close()
