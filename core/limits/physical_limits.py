class PhysicalLimitError(Exception):
    pass


def enforce_physical_limits(sim_config: dict):
    """
    Enforces physical sanity limits on simulation parameters.
    Raises PhysicalLimitError if values are unsafe or unphysical.
    """

    bc = sim_config.get("boundary_conditions", {})
    inlet = bc.get("inlet", {})

    # ----------------------------------
    # Velocity limits (air / general CFD)
    # ----------------------------------
    velocity = inlet.get("velocity")
    if velocity:
        v = velocity.get("value", 0)

        if v < 0:
            raise PhysicalLimitError("Velocity cannot be negative")

        if v > 150:
            raise PhysicalLimitError(
                f"Velocity {v} m/s exceeds safe incompressible CFD limit (150 m/s)"
            )

    # ----------------------------------
    # Temperature limits
    # ----------------------------------
    temperature = inlet.get("temperature")
    if temperature:
        T = temperature.get("value", 300)

        if T < 200:
            raise PhysicalLimitError(
                f"Temperature {T} K is below realistic engineering limits"
            )

        if T > 1500:
            raise PhysicalLimitError(
                f"Temperature {T} K exceeds solver-safe thermal limits"
            )

    # ----------------------------------
    # CHT material limits
    # ----------------------------------
    if sim_config.get("context_analysis", {}).get("physics_domain") == "CHT":
        materials = sim_config.get("materials", {})
        solid = materials.get("solid", {})

        k = solid.get("thermal_conductivity")
        if k is not None:
            if k <= 0:
                raise PhysicalLimitError("Thermal conductivity must be positive")

            if k > 1000:
                raise PhysicalLimitError(
                    f"Thermal conductivity {k} W/mK is unphysically high"
                )

    return True
