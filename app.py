# app.py
import sys
import json
import os
from ai.prompt_parser import parse_selection_request

# Files for data exchange between Fusion 360 and this Python script
CONTEXT_FILE = 'fusion_context.json'
RESPONSE_FILE = 'fusion_response.json'

def run():
    # 1. Check if the context file exists (Fusion should have created it)
    if not os.path.exists(CONTEXT_FILE):
        print(f"[Error] {CONTEXT_FILE} not found. Run this from Fusion 360 first.")
        sys.exit(1)

    # 2. Load the data sent from Fusion
    try:
        with open(CONTEXT_FILE, 'r') as f:
            data = json.load(f)
            user_prompt = data.get("prompt", "")
            # We assume Fusion sends a list of objects like: {"name": "Bolt:1", "token": "xyz"}
            # We extract just the names for the AI to read
            full_entities = data.get("entities", [])
            entity_names = [e["name"] for e in full_entities]
    except Exception as e:
        print(f"[Error] Failed to read context: {e}")
        sys.exit(1)

    if not user_prompt:
        print("[Error] No prompt provided in context file.")
        sys.exit(1)

    # 3. Call the AI
    result = parse_selection_request(user_prompt, entity_names)
    
    # 4. Map the AI's selected names back to Entity Tokens
    # The AI returns names, but Fusion needs 'Tokens' (IDs) to select them.
    selected_names = set(result.get("selected_names", []))
    
    selected_tokens = []
    for entity in full_entities:
        if entity["name"] in selected_names:
            selected_tokens.append(entity["token"])

    # 5. Write the response for Fusion to read
    response_data = {
        "tokens": selected_tokens,
        "reasoning": result.get("reasoning", "")
    }

    with open(RESPONSE_FILE, 'w') as f:
        json.dump(response_data, f, indent=2)
    
    print(f"[Success] Found {len(selected_tokens)} items. Response written.")

if __name__ == "__main__":
    run()