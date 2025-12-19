from fusion.cfd_setup import setup_cfd
from fusion.thermal_setup import setup_thermal
from fusion.cht_setup import setup_cht


def dispatch_to_fusion(sim_config: dict) -> dict:
    domain = sim_config["context_analysis"]["physics_domain"]

    print(f"[FUSION] Dispatching setup for domain: {domain}")

    if domain == "CFD":
        return setup_cfd(sim_config)

    elif domain == "Thermal":
        return setup_thermal(sim_config)

    elif domain == "CHT":
        return setup_cht(sim_config)

    else:
        print("[FUSION] Unsupported domain for PoC")
        return {"status": "unsupported_domain"}
