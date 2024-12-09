import pytest
from homeassistant.setup import async_setup_component

@pytest.mark.asyncio
async def test_scsgate_plus_light(hass, caplog):
    # Charger le composant light avec notre plateforme scsgate_plus
    config = {
        "light": {
            "platform": "scsgate_plus",
            "scs_id": "12"
        }
    }

    assert await async_setup_component(hass, "light", config)
    await hass.async_block_till_done()

    # Vérifier que l'entité a été créée
    entity_id = "light.scs_light_12"
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.name == "SCS Light 12"
    assert state.state == "off"

    # Simuler l'allumage
    await hass.services.async_call("light", "turn_on", {"entity_id": entity_id}, blocking=True)
    state = hass.states.get(entity_id)
    assert state.state == "on"
    assert "turn_on_light called for 12" in caplog.text

    # Simuler l'extinction
    await hass.services.async_call("light", "turn_off", {"entity_id": entity_id}, blocking=True)
    state = hass.states.get(entity_id)
    assert state.state == "off"
    assert "turn_off_light called for 12" in caplog.text
