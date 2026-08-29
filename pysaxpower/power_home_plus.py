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
                if i > 0:
                    decoded_value = self.apply_offset(value.registers[0])
                    results.append(decoded_value)
                else:
                    results.append(value.registers[0])
            else:
                print(f"Error reading register {addresses[i]} from Sax Power Home Plus Battery")
                results.append(None)

        return results

    def connect(self):
        self.client.connect()

    def close(self):
        self.client.close()
