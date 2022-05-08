from custom_components.peaqev.sensors.sensorbase import SensorBase
from custom_components.peaqev.peaqservice.util.constants import CHARGERCONTROLLER
from datetime import datetime

class PeaqSensor(SensorBase):
    def __init__(self, hub, entry_id):
        name = f"{hub.hubname} {CHARGERCONTROLLER}"
        super().__init__(hub, name, entry_id)

        self._attr_name = name
        self._state = self._hub.chargecontroller.status.name
        self._nonhours = None
        self._cautionhours = None
        self._current_hour = None,
        self._price_aware = False,
        self._absolute_top_price = None
        self._currency = None
        self._cautionhour_type_string = None

    @property
    def state(self):
        return self._hub.chargecontroller.status.name

    @property
    def icon(self) -> str:
        ret = "mdi:electric-switch-closed"
        if self.state == "Idle":
            ret = "mdi:electric-switch"
        elif self.state == "Done":
            ret = "mdi:check"
        return ret

    def update(self) -> None:
        self._state = self._hub.chargecontroller.status.name
        self._nonhours = self._hub.hours.non_hours
        self._cautionhours = self._hub.hours.caution_hours
        self._current_hour = self._hub.hours.state
        self._price_aware = self._hub.hours.price_aware
        self._absolute_top_price = self._hub.hours.absolute_top_price if self._price_aware is True else "-"
        self._currency = self._hub.hours.currency if self._price_aware is True else ""
        self._cautionhour_type_string = self._hub.hours.cautionhour_type_string if self._price_aware is True else ""

    @property
    def extra_state_attributes(self) -> dict:
        dict = {
            "non_hours": self._nonhours,
            "caution_hours": self._cautionhours,
            "current_hour state": self._current_hour,
            "price aware": self._price_aware,
        }

        if self._price_aware is True:
            dict["absolute top price"] = f"{self._absolute_top_price} {self.currency}"
            dict["cautionhour_type"] = self._cautionhour_type_string
            dict["cautionhour_charge_permittance"] = self.set_dynamic_caution_hours_display()

        return dict

    def set_dynamic_caution_hours_display(self) -> str:
        if len(self._hub.hours.dynamic_caution_hours) > 0:
            if datetime.now().hour in self._hub.hours.dynamic_caution_hours.keys():
                ret = int(self._hub.hours.dynamic_caution_hours[datetime.now().hour] * 100)
                return f"{str(ret)}%"
        return "100%"
