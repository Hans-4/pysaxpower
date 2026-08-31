class SunSpecRegister(object):

    #-----------------------
    # SunSpec / Device info
    #-----------------------
    SunSpecID_1      = 40000
    SunSpecID_2      = 40001
    SunSpecModelID   = 40002
    Length           = 40003
    Manufacturer_1   = 40004
    Manufacturer_2   = 40005
    Manufacturer_3   = 40006
    Manufacturer_4   = 40007
    DeviceModel_1    = 40008
    DeviceModel_2    = 40009
    DeviceModel_3    = 40010
    VersionMaster    = 40011
    VersionGateway   = 40012
    SerialNumber_High= 40013
    SerialNumber_Low = 40014


    # Sunspec 103
    Model_Identifier_103    = 40015
    Model_Length_32         = 40016

    # AC Current (Storage)
    AC_Current_Sum_Storage   = 40017
    AC_Current_Storage_A     = 40018
    AC_Current_Storage_B     = 40019
    AC_Current_Storage_C     = 40020
    AC_Current_Scalefactor   = 40021

    # Voltage (Storage)
    Voltage_Storage_L1_L2    = 40022
    Voltage_Storage_L2_L3    = 40023
    Voltage_Storage_L3_L1    = 40024
    Voltage_Storage_A        = 40025
    Voltage_Storage_B        = 40026
    Voltage_Storage_C        = 40027
    Voltage_Scalefactor      = 40028

    # Power (Storage)
    ActivePower_Storage_Sum  = 40029
    ActivePower_Scalefactor  = 40030

    #------------------------------
    # Frequency
    #------------------------------
    GridFrequency           = 40031
    Frequency_Scalefactor   = 40032

    #--------------------------------
    # Apparent Power (Storage)
    #--------------------------------
    ApparentPower_Storage_Sum = 40033
    ApparentPower_Scalefactor = 40034

    #--------------------------------
    # Reactive Power (Storage)
    #--------------------------------
    ReactivePower_Storage_Sum = 40035
    ReactivePower_Scalefactor = 40036

    #-------------------------------
    # Power Factor (Storage)
    #-------------------------------
    PowerFactor_Storage_Sum  = 40037
    PowerFactor_Scalefactor  = 40038

    #------------------------------
    # Temperature
    #-------------------------------
    MaxCellTemperature       = 40041
    Temperature_Scalefactor  = 40042

    #--------------
    # Status
    #--------------
    State   = 40043
    Event   = 40044

    #------------------------------
    # PV Power (ADW200 only)
    #------------------------------
    PV_Power                = 40045
    PV_Power_Scalefactor    = 40046

    #------------------------------
    # Sunspec
    #------------------------------
    Sunspec_Model_ID_123    = 40047
    Sunspec_Lenght_7        = 40048

    #------------------------------
    # Control
    #------------------------------
    PowerTarget             = 40049
    PowerTargetTimeout      = 40050
    ControlMode             = 40051
    PowerTargetScalefactor  = 40052
    MaxPowerReference       = 40053

    #--------------------------
    # Sunspec
    #--------------------------
    Sunspec_Model_ID    = 40054
    Sunspec_Lenght      = 40055

    #--------------------------------------
    # AC Current (Grid)
    #--------------------------------------
    AC_Current_Sum_Grid             = 40056
    AC_Current_Grid_L1              = 40057
    AC_Current_Grid_L2              = 40058
    AC_Current_Grid_L3              = 40059
    AC_Current_Scalefactor_Grid     = 40060

    #----------------------------------
    # Voltage (Grid)
    #----------------------------------
    AverageVoltage_Grid_L_N     = 40061
    GridVoltage_L1              = 40062
    GridVoltage_L2              = 40063
    GridVoltage_L3              = 40064
    AverageVoltage_Grid_L_L     = 40065
    GridVoltage_L1_L2           = 40066
    GridVoltage_L2_L3           = 40067
    GridVoltage_L1_L3           = 40068
    Voltage_Scalefactor_Grid    = 40069

    #----------------------------------
    # Frequency (Grid)
    #----------------------------------
    GridFrequency_203           = 40070
    Frequency_Scalefactor_Grid  = 40071

    #--------------------------------------
    # Active Power (Grid)
    #--------------------------------------
    ActiveGridPower             = 40072
    ActiveGridPower_L1          = 40073
    ActiveGridPower_L2          = 40074
    ActiveGridPower_L3          = 40075
    ActiveGridPower_Scalefactor = 40076

    #--------------------------------------
    # Apparent Power (Grid)
    #--------------------------------------
    ApparentPower_Sum_Grid          = 40077
    ApparentPower_Grid_L1           = 40078
    ApparentPower_Grid_L2           = 40079
    ApparentPower_Grid_L3           = 40080
    ApparentPower_Scalefactor_Grid  = 40081

    #--------------------------------------
    # Reactive Power (Grid)
    #--------------------------------------
    ReactivePower_Sum_Grid          = 40082
    ReactivePower_Grid_L1           = 40083
    ReactivePower_Grid_L2           = 40084
    ReactivePower_Grid_L3           = 40085
    ReactivePower_Scalefactor_Grid  = 40086

    #--------------------------------------
    # Power Factor (Grid)
    #--------------------------------------
    PowerFactor_Sum_Grid            = 40087
    PowerFactor_Grid_L1             = 40088
    PowerFactor_Grid_L2             = 40089
    PowerFactor_Grid_L3             = 40090
    PowerFactor_Scalefactor_Grid    = 40091

    #--------------------------------------
    # Sunspec
    #--------------------------------------
    Sunspec_ModelId_Base_Model      = 40095
    Sunspec_Length                  = 40096

    #----------------------------------
    # Battery System
    #----------------------------------
    BatterySystemCapacity       = 40097
    AvailableChargePower        = 40098
    AvailableDischargePower     = 40099
    MaxSoC                      = 40100
    MinSoC                      = 40101
    CurrentSoC                  = 40102
    DepthOfDischarge            = 40103

    #------------------------------
    # Battery Status
    #------------------------------
    BatteryChargingStatus   = 40106
    BatteryEvent            = 40108
    AverageCellVoltage      = 40109

    #------------------------------------------
    # Scalefactors (Battery)
    #------------------------------------------
    Capacity_Scalefactor                = 40110
    ChargeDischargePower_Scalefactor    = 40111
    SoC_Scalefactor                     = 40112
    CellVoltage_Scalefactor             = 40114

    #--------------------
    # Reserve Registers
    #--------------------
    Reserve_40039 = 40039
    Reserve_40040 = 40040
    Reserve_40092 = 40092
    Reserve_40093 = 40093
    Reserve_40094 = 40094
    Reserve_40104 = 40104
    Reserve_40105 = 40105
    Reserve_40107 = 40107
    Reserve_40113 = 40113
