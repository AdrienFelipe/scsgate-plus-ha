"""Initialisation du composant SCSGate Plus."""
from homeassistant.core import HomeAssistant

DOMAIN = "scsgate_plus"

async def async_setup(hass: HomeAssistant, config: dict):
    # Rien de particulier, le setup de la plateforme light se fait via light.py
    return True
