from ai.prompt_parser import parse_prompt
from fusion.adapter import dispatch_to_fusion
from core.normalizers.units import normalize_sim_config
from core.validators.sim_config_validator import (
    validate_sim_config,
    SimConfigValidationError
)
from core.limits.physical_limits import (
    enforce_physical_limits,
    PhysicalLimitError
)


import json
import os
from datetime import datetime


def run(user_prompt: str):
    print("\n" + "=" * 50)
    print("[CORE] Orchestrator Initialized")

    # --------------------------------------------------
    # STEP 1: Get AI Response
    # --------------------------------------------------
    sim_config = parse_prompt(user_prompt)

    # --------------------------------------------------
    # STEP 2: Validate AI Output
    # --------------------------------------------------
    try:
        validate_sim_config(sim_config)
        print("[CORE] AI output validated successfully")
    except SimConfigValidationError as e:
        print(f"[CORE] Validation failed: {e}")
        print("[CORE] Stopping pipeline to prevent unsafe execution")
        return
    
    # --------------------------------------------------
    # STEP 2.5: Normalize Units to SI
    # --------------------------------------------------
    sim_config = normalize_sim_config(sim_config)
    print("[CORE] Units normalized to SI")

   # --------------------------------------------------
   # STEP 2.75: Enforce Physical Limits
   # --------------------------------------------------
    try:
       enforce_physical_limits(sim_config)
       print("[CORE] Physical limits check passed")
    except PhysicalLimitError as e:
       print(f"[CORE] Physical limit violation: {e}")
       print("[CORE] Stopping pipeline to prevent unsafe simulation")
       return

    # --------------------------------------------------
    # STEP 3: Safe Extraction
    # --------------------------------------------------
    context = sim_config.get("context_analysis", {})
    subject = context.get("subject_identified", "general_simulation")
    domain = context.get("physics_domain", "Unknown")

    if domain == "Unknown":
        print("[CORE] Warning: Physics domain could not be confidently inferred")

    # --------------------------------------------------
    # STEP 3.5: Prepare Fusion Payload
    # --------------------------------------------------
    fusion_payload = dispatch_to_fusion(sim_config)
    print("[CORE] Fusion Payload Prepared")

    # --------------------------------------------------
    # STEP 4: Save Output Files
    # --------------------------------------------------
    os.makedirs("outputs", exist_ok=True)

    clean_subject = str(subject).lower().replace(" ", "_")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save AI configuration
    sim_filename = f"outputs/sim_{clean_subject}_{timestamp}.json"
    with open(sim_filename, "w") as f:
        json.dump(sim_config, f, indent=2)

    # Save Fusion payload
    fusion_filename = f"outputs/fusion_payload_{clean_subject}_{timestamp}.json"
    with open(fusion_filename, "w") as f:
        json.dump(fusion_payload, f, indent=2)

    # --------------------------------------------------
    # STEP 5: Console Summary
    # --------------------------------------------------
    print("-" * 50)
    print(f"[CORE] Simulation Config Saved : {sim_filename}")
    print(f"[CORE] Fusion Payload Saved   : {fusion_filename}")
    print(f"[CORE] Subject Identified     : {subject}")
    print(f"[CORE] Domain Detected        : {domain}")

    bc = sim_config.get("boundary_conditions", {})
    inlet = bc.get("inlet", {})

    if domain in ["CFD", "CHT"]:
        vel = inlet.get("velocity", {}).get("value", "N/A")
        unit = inlet.get("velocity", {}).get("unit", "m/s")
        print(f"[CORE] Flow Velocity          : {vel} {unit}")

    if domain in ["Thermal", "CHT", "Structural"]:
        temp = inlet.get("temperature", {}).get("value", "N/A")
        print(f"[CORE] Target Temperature    : {temp} K")

    if "Structural" in domain:
        print("[CORE] Analysis Type          : Thermal Stress / Deformation")

    print(f"[CORE] AI Reasoning           : {sim_config.get('inference_reasoning', 'Logic applied.')}")
    print("=" * 50 + "\n")
