# core/orchestrator.py
from ai.prompt_parser import parse_prompt
import json
import os
from datetime import datetime

def run(user_prompt: str):
    print("------------------------------------------------")
    print("[CORE] Orchestrator Initialized")
    
    # 1. Get Intelligent Parameters
    simulation_config = parse_prompt(user_prompt)

    # 2. Prepare Output Directory
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # 3. Generate Filename
    # We include the subject in the filename for easier sorting
    subject = simulation_config.get("subject", "general").replace(" ", "_")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{output_dir}/sim_{subject}_{timestamp}.json"

    # 4. Save Configuration
    with open(filename, "w") as f:
        json.dump(simulation_config, f, indent=2)

    print("------------------------------------------------")
    print(f"[CORE] Configuration Generated: {filename}")
    print(f"[CORE] Subject: {simulation_config.get('subject')}")
    print(f"[CORE] Velocity: {simulation_config['physics']['velocity_inlet']['value']} {simulation_config['physics']['velocity_inlet']['unit']}")
    print(f"[CORE] Solver: {simulation_config['solver_settings']['turbulence_model']}")
    print("------------------------------------------------")
