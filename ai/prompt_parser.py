# ai/prompt_parser.py
import os
import json
from dotenv import load_dotenv
from groq import Groq
from ai.prompts import SYSTEM_INSTRUCTION

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def parse_prompt(user_prompt: str) -> dict:
    """
    Sends the prompt to Llama-3 to extract parameters contextually.
    """
    print(f"[AI] Analyzing prompt: '{user_prompt}'")

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Using 70b for better reasoning on 'context'
            messages=[
                {"role": "system", "content": SYSTEM_INSTRUCTION},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1, # Keep low for strict JSON adherence
            response_format={"type": "json_object"}
        )

        raw_text = completion.choices[0].message.content
        parsed_output = json.loads(raw_text)
        
        # Log the reasoning to console so user understands the AI's choice
        if "reasoning" in parsed_output:
            print(f"[AI] Inference Reasoning: {parsed_output['reasoning']}")

        return parsed_output

    except Exception as e:
        print(f"[AI] Error parsing prompt: {e}")
        return get_fallback_defaults()

def get_fallback_defaults():
    """Returns a safe default configuration if AI fails."""
    return {
        "subject": "unknown_vehicle",
        "intent": "cfd",
        "physics": {
            "velocity_inlet": {"value": 20, "unit": "m/s", "condition_type": "default"},
            "temperature": {"value": 300, "unit": "K"},
            "pressure": {"value": 101325, "unit": "Pa"}
        },
        "solver_settings": {
            "time_domain": "steady",
            "turbulence_model": "k-epsilon",
            "iterations": 500
        },
        "reasoning": "System failure fallback"
    }