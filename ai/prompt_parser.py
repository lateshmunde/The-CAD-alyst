# ai/prompt_parser.py
import os
import json
from dotenv import load_dotenv

try:
    from groq import Groq
except ImportError:
    Groq = None

from ai.prompts import SYSTEM_INSTRUCTION

load_dotenv()
_groq_api_key = os.getenv("GROQ_API_KEY")
client = None

if Groq is not None and _groq_api_key:
    try:
        client = Groq(api_key=_groq_api_key)
    except Exception:
        client = None

def parse_selection_request(user_prompt: str, model_context: list) -> dict:
    """
    Decides which items to select. 
    If Groq is active, it asks AI. 
    If Groq is MISSING, it uses simple text matching (Fallback).
    """
    print(f"[AI] Processing request: '{user_prompt}'")

    # --- OPTION 1: AI (Groq) ---
    if client:
        try:
            combined_prompt = (
                f"User Request: {user_prompt}\n\n"
                f"Available Geometry List:\n{json.dumps(model_context, indent=2)}"
            )
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM_INSTRUCTION},
                    {"role": "user", "content": combined_prompt}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            raw = completion.choices[0].message.content
            return json.loads(raw)
        except Exception as e:
            print(f"[AI] Error: {e}")
            # If AI fails, drop through to fallback

    # --- OPTION 2: FALLBACK (Simple String Match) ---
    print("[AI] Using local fallback (String Matching)...")
    return get_local_selection(user_prompt, model_context)


def get_local_selection(prompt, context_list):
    """
    A dumb but reliable search. 
    If prompt is 'Gear', it selects anything containing 'Gear'.
    """
    selected = []
    prompt_lower = prompt.lower()
    
    for name in context_list:
        # Simple Logic: exact match or substring match
        if prompt_lower in name.lower():
            selected.append(name)
            
    return {
        "selected_names": selected,
        "reasoning": f"Local fallback selected items containing '{prompt}'"
    }