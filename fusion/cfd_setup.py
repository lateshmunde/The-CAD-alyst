def setup_cfd(sim_config: dict) -> dict:
    inlet = sim_config["boundary_conditions"]["inlet"]

    velocity = inlet.get("velocity", {}).get("value", 0)
    temperature = inlet.get("temperature", {}).get("value", 300)

    fusion_payload = {
        "analysis_type": "CFD",
        "boundary_conditions": {
            "velocity_inlet_mps": velocity,
            "inlet_temperature_k": temperature
        },
        "models": {
            "turbulence": "k-epsilon",
            "energy_equation": True
        }
    }

    print("[FUSION] CFD setup prepared")

    return fusion_payload
