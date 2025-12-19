class SimConfigValidationError(Exception):
    pass


def validate_sim_config(config: dict):
    """
    Validates AI-generated simulation configuration.
    Raises exception if critical fields are missing.
    """

    # ---- Top-level keys ----
    required_top_keys = [
        "context_analysis",
        "boundary_conditions",
        "solver_settings"
    ]

    for key in required_top_keys:
        if key not in config:
            raise SimConfigValidationError(f"Missing top-level key: {key}")

    # ---- Context analysis ----
    context = config["context_analysis"]
    if "physics_domain" not in context:
        raise SimConfigValidationError("Missing physics_domain")

    # ---- Boundary conditions ----
    bc = config["boundary_conditions"]

    if "inlet" not in bc:
        raise SimConfigValidationError("Missing inlet boundary condition")

    inlet = bc["inlet"]

    if "velocity" in inlet:
        if "value" not in inlet["velocity"]:
            raise SimConfigValidationError("Velocity value missing")

    if "temperature" in inlet:
        if "value" not in inlet["temperature"]:
            raise SimConfigValidationError("Temperature value missing")

    # ---- Solver settings ----
    solver = config["solver_settings"]
    if "time_stepping" not in solver:
        raise SimConfigValidationError("Missing time_stepping in solver_settings")

    # ---- CHT-specific validation ----
    if context.get("physics_domain") == "CHT":
        materials = config.get("materials", {})

        if "solid" not in materials:
            raise SimConfigValidationError("CHT requires solid material definition")

        if "fluid" not in materials:
            raise SimConfigValidationError("CHT requires fluid material definition")

    return True

