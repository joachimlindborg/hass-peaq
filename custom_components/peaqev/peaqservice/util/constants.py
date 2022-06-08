import peaqevcore.Constants as core
from peaqevcore.Models import (
    CAUTIONHOURTYPE_SUAVE,
    CAUTIONHOURTYPE_INTERMEDIATE,
    CAUTIONHOURTYPE_AGGRESSIVE,
    CAUTIONHOURTYPE as core_CAUTIONHOURTYPE
)

#todo: these shouldn't all be here.
LOCALES = core.LOCALES
LOCALE_SE_GOTHENBURG = core.LOCALE_SE_GOTHENBURG
LOCALE_SE_KARLSTAD = core.LOCALE_SE_KARLSTAD
LOCALE_SE_KRISTINEHAMN = core.LOCALE_SE_KRISTINEHAMN
LOCALE_SE_NACKA_NORMAL = core.LOCALE_SE_NACKA_NORMAL
LOCALE_SE_PARTILLE = core.LOCALE_SE_PARTILLE
LOCALE_DEFAULT = core.LOCALE_DEFAULT
LOCALE_SE_SALA = core.LOCALE_SE_SALA
LOCALE_SE_MALUNG_SALEN = core.LOCALE_SE_MALUNG_SALEN
LOCALE_SE_SKOVDE = core.LOCALE_SE_SKOVDE
LOCALE_SE_SOLLENTUNA = core.LOCALE_SE_SOLLENTUNA
LOCALE_BE_VREG = core.LOCALE_BE_VREG
LOCALE_SE_BJERKE_ENERGI = core.LOCALE_SE_BJERKE_ENERGI
LOCALE_NO_GLITRE_ENERGI = core.LOCALE_NO_GLITRE_ENERGI
LOCALE_NO_AGDER_ENERGI = core.LOCALE_NO_AGDER_ENERGI
LOCALE_NO_LNETT = core.LOCALE_NO_LNETT
LOCALE_NO_TENSIO = core.LOCALE_NO_TENSIO
LOCALE_SE_LINDE_ENERGI = core.LOCALE_SE_LINDE_ENERGI
QUERYTYPE_BASICMAX = core.QUERYTYPE_BASICMAX
QUERYTYPE_AVERAGEOFTHREEDAYS = core.QUERYTYPE_AVERAGEOFTHREEDAYS
QUERYTYPE_AVERAGEOFTHREEHOURS = core.QUERYTYPE_AVERAGEOFTHREEHOURS
QUERYTYPE_AVERAGEOFTHREEDAYS_MIN = core.QUERYTYPE_AVERAGEOFTHREEDAYS_MIN
QUERYTYPE_AVERAGEOFTHREEHOURS_MIN = core.QUERYTYPE_AVERAGEOFTHREEHOURS_MIN
QUERYTYPE_AVERAGEOFFIVEDAYS = core.QUERYTYPE_AVERAGEOFFIVEDAYS
QUERYTYPE_AVERAGEOFFIVEDAYS_MIN = core.QUERYTYPE_AVERAGEOFFIVEDAYS_MIN
QUERYTYPE_HIGHLOAD = core.QUERYTYPE_HIGHLOAD
QUERYTYPE_AVERAGEOFTHREEHOURS_MON_FRI_07_19 = core.QUERYTYPE_AVERAGEOFTHREEHOURS_MON_FRI_07_19
QUERYTYPE_AVERAGEOFTHREEHOURS_MON_FRI_07_19_MIN = core.QUERYTYPE_AVERAGEOFTHREEHOURS_MON_FRI_07_19_MIN
QUERYTYPE_MAX_NOV_MAR_MON_FRI_06_22 = core.QUERYTYPE_MAX_NOV_MAR_MON_FRI_06_22
QUERYTYPE_BASICMAX_MON_FRI_07_17_DEC_MAR_ELSE_REGULAR = core.QUERYTYPE_BASICMAX_MON_FRI_07_17_DEC_MAR_ELSE_REGULAR
QUERYTYPE_SOLLENTUNA = core.QUERYTYPE_SOLLENTUNA
QUERYTYPE_SOLLENTUNA_MIN = core.QUERYTYPE_SOLLENTUNA_MIN
QUARTER_HOURLY = core.QUARTER_HOURLY
HOURLY = core.HOURLY


CURRENTS_ONEPHASE_1_16 = {
    3600: 16,
    3150: 14,
    2700: 12,
    2250: 10,
    1800: 8,
    1350: 6
} #moved to core
CURRENTS_THREEPHASE_1_16 = {
    11000: 16,
    9625: 14,
    8250: 12,
    6875: 10,
    5500: 8,
    4100: 6
} #moved to core
CURRENTS_ONEPHASE_1_32 = {
    7200: 32,
    6750: 30,
    6300: 28,
    5850: 26,
    5400: 24,
    4950: 22,
    4500: 20,
    4050: 18,
    3600: 16,
    3150: 14,
    2700: 12,
    2250: 10,
    1800: 8,
    1350: 6
} #moved to core
CURRENTS_THREEPHASE_1_32 = {
    22000: 32,
    20625: 30,
    19250: 28,
    17875: 26,
    16500: 24,
    15125: 22,
    13750: 20,
    12375: 18,
    11000: 16,
    9625: 14,
    8250: 12,
    6875: 10,
    5500: 8,
    4100: 6
} #moved to core


"""CHARGERTYPES"""
CHARGERTYPE_CHARGEAMPS = "Chargeamps"
CHARGERTYPE_EASEE = "Easee"
CHARGERTYPE_GAROWALLBOX = "Garo Wallbox"

"""Lookup types for config flow"""
CHARGERTYPES = [
    CHARGERTYPE_CHARGEAMPS,
    CHARGERTYPE_EASEE,
    #CHARGERTYPE_GAROWALLBOX
    ]

"""NAMING CONSTANTS"""
PEAQCONTROLLER = "Peaq controller"
CHARGERCONTROLLER = "Charger controller"
MONEY = "Money"
HOURCONTROLLER = "Hour controller"
PREDICTION = "Prediction"
TOTALPOWER = "Total power"
HOUSEPOWER = "House power"
ALLOWEDCURRENT = "Allowed current"
CONSUMPTION_INTEGRAL_NAME = "Energy excluding car"
CONSUMPTION_TOTAL_NAME = "Energy including car"
CHARGERENABLED = "Charger enabled"
CHARGERDONE = "Charger done"
AVERAGECONSUMPTION = "Average consumption"
THRESHOLD = "Threshold"
SQLSENSOR_BASENAME = "Monthly max peak"
SQLSENSOR_AVERAGEOFTHREE = "Average of three"
SQLSENSOR_AVERAGEOFTHREE_MIN = "Min of three"
SQLSENSOR_HIGHLOAD = "High load"

"""Sql sensor helpers"""
SQLSENSOR_STATISTICS_TABLE = "statistics"
SQLSENSOR_STATISTICS_META_TABLE = "statistics_meta"

"""Chargertype helpers"""
UPDATECURRENT = "updatecurrent"
PARAMS = "params"
CHARGER = "charger"
CHARGERID = "chargerid"
CURRENT = "current"
DOMAIN = "domain"
NAME = "name"
ON = "on"
OFF = "off"
RESUME = "resume"
PAUSE = "pause"

"""States for the Hours-object"""
NON_HOUR = "Charging stopped"
CAUTION_HOUR = "Charging-permittance degraded"
CHARGING_PERMITTED = "Charging permitted"

CAUTIONHOURTYPE_NAMES =[
    CAUTIONHOURTYPE_SUAVE,
    CAUTIONHOURTYPE_INTERMEDIATE,
    CAUTIONHOURTYPE_AGGRESSIVE
]

CAUTIONHOURTYPE_DICT = core_CAUTIONHOURTYPE

TYPEREGULAR = "Regular (requires power sensor)"
TYPELITE = "Lite"

INSTALLATIONTYPES = [
    TYPEREGULAR,
    TYPELITE
]
