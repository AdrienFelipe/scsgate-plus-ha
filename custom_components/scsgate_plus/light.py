import logging
from homeassistant.components.light import LightEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.area_registry import AreaRegistry
from homeassistant.const import CONF_PLATFORM

from .const import DOMAIN, CONF_SCS_ID
import scsgate.scsgate.tasks

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up SCSGate Plus lights depuis la configuration YAML."""
    scs_id = config.get(CONF_SCS_ID)
    if scs_id is None:
        _LOGGER.error("scs_id is required")
        return
    
    task = scsgate.scsgate.tasks.ToggleStatusTask(scs_id, False)
    light = SCSGatePlusLight(hass, task, scs_id)
    async_add_entities([light], True)

class SCSGatePlusLight(LightEntity):
    def __init__(self, hass, task, scs_id):
        self._hass = hass
        self._task = task
        self._scs_id = scs_id
        self._name = f"SCS Light {scs_id}"
        self._is_on = False

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"scsgate_plus_light_{self._scs_id}"

    @property
    def is_on(self):
        return self._is_on

    async def async_turn_on(self, **kwargs):
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self._is_on = False
        self.async_write_ha_state()

    # Possibilité de renommer via UI et assigner une Area via les menus d’HA.
    # Pas besoin de code spécifique pour le rename ou l'Area, HA gère cela via le UI.
    # Si vous voulez démontrer le rename, ce sera juste via l'UI.
