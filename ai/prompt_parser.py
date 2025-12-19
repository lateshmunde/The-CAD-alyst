# ai/prompt_parser.py

def parse_prompt(user_prompt: str) -> dict:
    """
    Dummy prompt parser (POC Phase-1).
    Later this will call OpenAI.
    """

    print("[AI] Received user prompt:", user_prompt)

    # Hardcoded output for now
    parsed_output = {
        "simulation_type": "external_flow",
        "velocity": 50,
        "velocity_unit": "m/s",
        "medium": "air",
        "solver": "steady"
    }

    print("[AI] Parsed simulation input:", parsed_output)

    return parsed_output
