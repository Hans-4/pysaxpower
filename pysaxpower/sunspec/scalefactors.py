from pysaxpower.sunspec.register import SunSpecRegister


class SunSpecScaleFactors(object):

    def __init__(self):
        self.register = SunSpecRegister()

    def search_scale_factor(self, address: int) -> int | None:
        r = self.register

        if 40017 <= address <= 40020:
            return r.AC_Current_Scalefactor
        elif 40022 <= address <= 40027:
            return r.Voltage_Scalefactor
        elif address == 40029:
            return r.ActivePower_Scalefactor
        elif address == 40031:
            return r.Frequency_Scalefactor
        elif address == 40033:
            return r.ApparentPower_Scalefactor
        elif address == 40035:
            return r.ReactivePower_Scalefactor
        elif address == 40037:
            return r.PowerFactor_Scalefactor
        elif address == 40041:
            return r.Temperature_Scalefactor
        elif address == 40045:
            return r.PV_Power_Scalefactor
        elif address == 40049:
            return r.PowerTargetScalefactor
        elif 40056 <= address <= 40059:
            return r.AC_Current_Scalefactor_Grid
        elif 40061 <= address <= 40068:
            return r.Voltage_Scalefactor_Grid
        elif address == 40070:
            return r.Frequency_Scalefactor_Grid
        elif 40072 <= address <= 40075:
            return r.ActiveGridPower_Scalefactor
        elif 40077 <= address <= 40080:
            return r.ApparentPower_Scalefactor_Grid
        elif 40082 <= address <= 40085:
            return r.ReactivePower_Scalefactor_Grid
        elif 40087 <= address <= 40090:
            return r.PowerFactor_Scalefactor_Grid
        elif address == 40097:
            return r.Capacity_Scalefactor
        elif 40098 <= address <= 40099:
            return r.ChargeDischargePower_Scalefactor
        elif 40100 <= address <= 40102:
            return r.SoC_Scalefactor
        elif address == 40109:
            return r.CellVoltage_Scalefactor
        else:
            return None