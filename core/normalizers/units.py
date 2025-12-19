def normalize_sim_config(sim_config: dict) -> dict:
    """
    Normalize all units in sim_config to SI units.
    Modifies and returns the same dict.
    """

    bc = sim_config.get("boundary_conditions", {})
    inlet = bc.get("inlet", {})

    # -----------------------------
    # Velocity normalization
    # -----------------------------
    velocity = inlet.get("velocity")
    if velocity:
        value = velocity.get("value")
        unit = velocity.get("unit", "m/s")

        if unit == "km/h":
            velocity["value"] = value / 3.6
            velocity["unit"] = "m/s"

        elif unit == "mph":
            velocity["value"] = value * 0.44704
            velocity["unit"] = "m/s"

    # -----------------------------
    # Temperature normalization
    # -----------------------------
    temperature = inlet.get("temperature")
    if temperature:
        value = temperature.get("value")
        unit = temperature.get("unit", "K")

        if unit in ["C", "°C", "celsius"]:
            temperature["value"] = value + 273.15
            temperature["unit"] = "K"

        elif unit in ["F", "°F", "fahrenheit"]:
            temperature["value"] = (value - 32) * 5 / 9 + 273.15
            temperature["unit"] = "K"

    return sim_config
