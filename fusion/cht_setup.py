def setup_cht(sim_config: dict) -> dict:
    inlet = sim_config["boundary_conditions"]["inlet"]
    materials = sim_config.get("materials", {})

    velocity = inlet.get("velocity", {}).get("value", 0)
    inlet_temp = inlet.get("temperature", {}).get("value", 300)

    solid_material = materials.get("solid", {}).get("name", "Aluminum")
    k_solid = materials.get("solid", {}).get("thermal_conductivity", 200)

    fusion_payload = {
        "analysis_type": "CHT",
        "fluid": {
            "velocity_inlet_mps": velocity,
            "inlet_temperature_k": inlet_temp
        },
        "solid": {
            "material": solid_material,
            "thermal_conductivity_w_mk": k_solid
        },
        "models": {
            "energy_equation": True,
            "turbulence": "k-epsilon",
            "conjugate_heat_transfer": True
        }
    }

    print("[FUSION] CHT setup prepared")

    return fusion_payload
