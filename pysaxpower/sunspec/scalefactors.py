from pysaxpower.sunspec.register import SunSpecRegister


class SunSpecScaleFactors(object):
    """Ordnet einer Registeradresse die Adresse des zugehoerigen sunsf-Registers zu.

    Rueckgabe ist die ADRESSE des Scalefaktor-Registers, nicht dessen Wert.
    None bedeutet: fuer dieses Register existiert laut Dokumentation kein
    Scalefaktor (Well-Known-Werte, Enums, Timeouts, sunsf-Register selbst).
    """

    def __init__(self):
        self.register = SunSpecRegister()

    def search_scale_factor(self, address: int) -> int | None:
        r = self.register

        # ------------------------------------------------------------------
        # Modell 103 - Speicherelektronik (40015 - 40046)
        # ------------------------------------------------------------------
        if 40017 <= address <= 40020:                  # AC Strom Speicher Summe/A/B/C
            return r.AC_Current_Scalefactor            # 40021, SF = -2
        elif 40022 <= address <= 40027:                # Spannung Speicher L-L und A/B/C
            return r.Voltage_Scalefactor               # 40028, SF = -1
        elif address == 40029:                         # Wirkleistung Speicher Summe
            return r.ActivePower_Scalefactor           # 40030, SF = 0
        elif address == 40031:                         # Netzfrequenz (Speicher)
            return r.Frequency_Scalefactor             # 40032, SF = -2
        elif address == 40033:                         # Scheinleistung Speicher Summe
            return r.ApparentPower_Scalefactor         # 40034, SF = 0
        elif address == 40035:                         # Blindleistung Speicher Summe
            return r.ReactivePower_Scalefactor         # 40036, SF = 0
        elif address == 40037:                         # Leistungsfaktor Speicher Summe
            return r.PowerFactor_Scalefactor           # 40038, SF = -3
        elif address == 40041:                         # Maximale Zelltemperatur
            return r.Temperature_Scalefactor           # 40042, SF = 0
        elif address == 40045:                         # PV-Leistung (nur mit ADW200)
            return r.PV_Power_Scalefactor              # 40046, SF = 1

        # ------------------------------------------------------------------
        # Modell 123 - Immediate Controls (40047 - 40053)
        # ------------------------------------------------------------------
        elif address == 40049:                         # Leistungsvorgabe prozentual
            return r.PowerTargetScalefactor            # 40052, SF = -2
        # 40050 Timeout (s), 40051 Steuermodus (Enum),
        # 40053 Referenzwert Maximalleistung (W, Well-Known) -> kein SF

        # ------------------------------------------------------------------
        # Modell 203 - WYE Connect 3Ph Meter ABC / ADW200 (40054 - 40094)
        # ------------------------------------------------------------------
        elif 40056 <= address <= 40059:                # AC Strom Netz Summe/L1/L2/L3
            return r.AC_Current_Scalefactor_Grid       # 40060, SF = -1
        elif 40061 <= address <= 40068:                # Netzspannungen L-N und L-L
            return r.Voltage_Scalefactor_Grid          # 40069, SF = -1
        elif address == 40070:                         # Netzfrequenz
            return r.Frequency_Scalefactor_Grid        # 40071, SF = -2
        elif 40072 <= address <= 40075:                # Wirkleistung Netz Summe/L1/L2/L3
            return r.ActiveGridPower_Scalefactor       # 40076, SF = 1
        elif 40077 <= address <= 40080:                # Scheinleistung Netz Summe/L1/L2/L3
            return r.ApparentPower_Scalefactor_Grid    # 40081, SF = 1
        elif 40082 <= address <= 40085:                # Blindleistung Netz Summe/L1/L2/L3
            return r.ReactivePower_Scalefactor_Grid    # 40086, SF = 1
        elif 40087 <= address <= 40090:                # Leistungsfaktor Netz Summe/L1/L2/L3
            return r.PowerFactor_Scalefactor_Grid      # 40091, SF = -3

        # ------------------------------------------------------------------
        # Modell 802 - Battery Base Model (40095 - 40114)
        # ------------------------------------------------------------------
        elif address == 40097:                         # Kapazitaet Speichersystem (Wh)
            return r.Capacity_Scalefactor              # 40110, SF = 0
        elif 40098 <= address <= 40099:                # Verf. Lade-/Entladeleistung (W)
            return r.ChargeDischargePower_Scalefactor  # 40111, SF = 0
        elif 40100 <= address <= 40102:                # Max/Min/Aktueller SoC (%)
            return r.SoC_Scalefactor                   # 40112, SF = 0
        elif address == 40109:                         # Durchschnittliche Zellspannung (mV)
            return r.CellVoltage_Scalefactor           # 40114, SF = 0

        # 40103 Entladetiefe (%): in der Dokumentation ist KEIN Scalefaktor
        # zugeordnet. Kandidat waere 40113 (Reserve, int16 sunsf, Wert 0),
        # das an der Position von DoD_SF im SunSpec-Modell 802 steht.
        # Bewusst nicht geraten -> None.

        # 40000-40016, 40039/40040, 40043/40044, 40092-40094, 40104-40108,
        # sowie alle sunsf-Register selbst haben keinen Scalefaktor.
        else:
            return None