import logging

from homeassistant.core import HomeAssistant
from peaqevcore.hub.hub_options import HubOptions
from peaqevcore.models.chargerstates import CHARGERSTATES
from peaqevcore.models.chargertype.calltype import CallType
from peaqevcore.models.chargertype.calltype_enum import CallTypes
from peaqevcore.models.chargertype.servicecalls_dto import ServiceCallsDTO
from peaqevcore.models.chargertype.servicecalls_options import ServiceCallsOptions
from peaqevcore.services.chargertype.chargertype_base import ChargerBase

from custom_components.peaqev.peaqservice.util.constants import (
    SMARTOUTLET
)

_LOGGER = logging.getLogger(__name__)


class SmartOutlet(ChargerBase):
    def __init__(self, hass: HomeAssistant, huboptions: HubOptions):
        self._hass = hass
        self.entities.powerswitch = huboptions.charger.powerswitch
        self.entities.powermeter = huboptions.charger.powermeter
        self.options.charger_is_outlet = True
        self.options.powerswitch_controls_charging = True
        self.chargerstates[CHARGERSTATES.Idle] = ["idle"]
        self.chargerstates[CHARGERSTATES.Connected] = ["connected"]
        self.chargerstates[CHARGERSTATES.Charging] = ["charging"]
        self._hass.async_add_executor_job(self._validate_setup())

        self._set_servicecalls(
            domain=self.domain_name,
            model=ServiceCallsDTO(
                on=self.call_on,
                off=self.call_off
            ),
            options=self.servicecalls_options
        )

    @property
    def domain_name(self) -> str:
        """declare the domain name as stated in HA"""
        return SMARTOUTLET

    @property
    def native_chargerstates(self) -> list:
        """declare a list of the native-charger states available for the type."""
        return ["idle", "connected", "charging"]

    @property
    def call_on(self) -> CallType:
        return CallType(CallTypes.ON.value, {})

    @property
    def call_off(self) -> CallType:
        return CallType(CallTypes.OFF.value, {})

    @property
    def servicecalls_options(self) -> ServiceCallsOptions:
        return ServiceCallsOptions(
            allowupdatecurrent=False,
            update_current_on_termination=False,
            switch_controls_charger=True
        )

    def _validate_setup(self):
        def check_states(entity: str, type_format: type) -> bool:
            try:
                s = self._hass.states.get(entity)
                if s is not None:
                    if isinstance(s.state, type_format):
                        return True
            except:
                _LOGGER.error(f"Unable to validate outlet-sensor: {entity}")
                return False

        return all(
            [check_states(
                self.entities.powerswitch, str),
                check_states(self.entities.powermeter, float)
            ]
        )
