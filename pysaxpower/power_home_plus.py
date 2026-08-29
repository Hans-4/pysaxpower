from pymodbus.client import ModbusTcpClient

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

        self.connect()

    @staticmethod
    def apply_offset(value: int):
        offset = 16384
        return value - offset

    def write_register(self, value):
        self.client.write_register(address=41, value=value, device_id=64)

    def read_register(self):
        """
        46: battery charge level
        47: battery power
        48: battery grid power
        """
        addresses = [46, 47, 48]

        results = []

        for i in range(len(addresses)):
            value = self.client.read_holding_registers(address=addresses[i], count=1, device_id=64)

            if not value.isError():
                decoded_value = value.registers[0]
                results.append(decoded_value)
            else:
                print(f"Error reading register {addresses[i]} from Sax Power Home Plus Battery")
                results.append(None)

        return results

    def get_raw_values(self):
        values = self.read_register()
        return values

    def get_formatted_values(self):
        values = self.read_register()

        formatted_values = []

        for value in values:
            if value > 100:
                formatted_value = self.apply_offset(value)
                formatted_values.append(formatted_value)
            else:
                formatted_values.append(value)

        return formatted_values


    def connect(self):
        self.client.connect()

    def close(self):
        self.client.close()
