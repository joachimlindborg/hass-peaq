from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from custom_components.peaqev.peaqservice.hub.hub import HomeAssistantHub
import logging

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import POWER_WATT

from custom_components.peaqev.sensors.sensorbase import PowerDevice

_LOGGER = logging.getLogger(__name__)


class PeaqPowerSensor(PowerDevice):
    device_class = SensorDeviceClass.POWER
    unit_of_measurement = POWER_WATT

    def __init__(self, hub: HomeAssistantHub, entry_id):
        name = f"{hub.hubname} {hub.sensors.power.total.name}"  # todo: composition
        super().__init__(hub, name, entry_id)
        self.hub = hub
        self._state = None
        self._attr_icon = "mdi:flash"

    @property
    def state(self) -> int:
        try:
            return int(self._state)
        except (ValueError, TypeError):
            _LOGGER.error("Could not parse state %s for powersensor", self._state)
            return 0

    async def async_update(self) -> None:
        self._state = self.hub.sensors.power.total.value  # todo: composition
