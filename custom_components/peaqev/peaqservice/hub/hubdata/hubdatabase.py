from homeassistant.core import HomeAssistant

from custom_components.peaqev.peaqservice.charger.charger import Charger
from custom_components.peaqev.peaqservice.chargertypes.chargertypes import ChargerTypeData
from custom_components.peaqev.peaqservice.hub.hubdata.hubmember import CurrentPeak, HubMember, CarPowerSensor, \
    ChargerSwitch
from custom_components.peaqev.peaqservice.localetypes.locale import LocaleData


class HubDataBase:
    locale: LocaleData
    chargertype: ChargerTypeData
    currentpeak: CurrentPeak
    carpowersensor: CarPowerSensor
    chargerobject: HubMember
    chargerobject_switch: ChargerSwitch
    hass: HomeAssistant
    charger: Charger

    def create_hub_base_data(
            self,
            hass,
            config_inputs: dict,
            domain: str
    ):
        self.hass = hass

        self.locale = LocaleData(
            config_inputs["locale"],
            domain
        )
        self.chargertype = ChargerTypeData(
            hass,
            config_inputs["chargertype"],
            config_inputs["chargerid"]
        )
        self.currentpeak = CurrentPeak(
            data_type=float,
            listenerentity=self.locale.current_peak_entity,
            initval=0,
            startpeaks=config_inputs["startpeaks"]
        )
        self.carpowersensor = CarPowerSensor(
            data_type=int,
            listenerentity=self.chargertype.charger.powermeter,
            initval=0,
            powermeter_factor=self.chargertype.charger.powermeter_factor
        )
        self.chargerobject = HubMember(
            data_type=str,
            listenerentity=self.chargertype.charger.chargerentity
        )
        self.chargerobject_switch = ChargerSwitch(
            hass=hass,
            data_type=bool,
            listenerentity=self.chargertype.charger.powerswitch,
            initval=False,
            currentname=self.chargertype.charger.ampmeter,
            ampmeter_is_attribute=self.chargertype.charger.ampmeter_is_attribute
        )
        self.charger = Charger(
            self,
            hass,
            self.chargertype.charger.servicecalls
        )
