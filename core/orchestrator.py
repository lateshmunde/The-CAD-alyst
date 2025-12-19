# core/orchestrator.py
from ai.prompt_parser import parse_prompt
import json
import os
from datetime import datetime

def run(user_prompt: str):
    print("\n" + "="*50)
    print("[CORE] Orchestrator Initialized")
    
    # 1. Get AI Response
    sim_config = parse_prompt(user_prompt)

    # 2. Safe Extraction (Uses .get to avoid KeyError)
    context = sim_config.get("context_analysis", {})
    subject = context.get("subject_identified", "general_simulation")
    domain = context.get("physics_domain", "Unknown")
    
    # 3. Create Output Directory and Filename
    os.makedirs("outputs", exist_ok=True)
    clean_subject = str(subject).lower().replace(" ", "_")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"outputs/sim_{clean_subject}_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(sim_config, f, indent=2)

    # 4. Smart Console Summary (Prints only what is relevant)
    print("-" * 50)
    print(f"[CORE] Configuration Saved: {filename}")
    print(f"[CORE] Subject Identified: {subject}")
    print(f"[CORE] Domain Detected: {domain}")

    # Display relevant parameters based on domain
    bc = sim_config.get("boundary_conditions", {})
    inlet = bc.get("inlet", {})

    if domain in ["CFD", "CHT"]:
        vel = inlet.get("velocity", {}).get("value", "N/A")
        unit = inlet.get("velocity", {}).get("unit", "m/s")
        print(f"[CORE] Flow Velocity: {vel} {unit}")

    if domain in ["Thermal", "CHT", "Structural"]:
        temp = inlet.get("temperature", {}).get("value", "N/A")
        print(f"[CORE] Target Temperature: {temp} K")

    if "Structural" in domain:
        print(f"[CORE] Analysis Type: Thermal Stress / Deformation")

    print(f"[CORE] AI Reasoning: {sim_config.get('inference_reasoning', 'Logic applied.')}")
    print("="*50 + "\n")
