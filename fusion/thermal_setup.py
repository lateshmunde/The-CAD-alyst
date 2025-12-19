def setup_thermal(sim_config: dict) -> dict:
    inlet = sim_config["boundary_conditions"]["inlet"]

    temperature = inlet.get("temperature", {}).get("value", 300)

    fusion_payload = {
        "analysis_type": "Thermal",
        "boundary_conditions": {
            "target_temperature_k": temperature
        },
        "models": {
            "conduction": True,
            "radiation": False
        }
    }

    print("[FUSION] Thermal setup prepared")

    return fusion_payload
