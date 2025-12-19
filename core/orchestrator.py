from ai.prompt_parser import parse_prompt

def run(user_prompt: str):
    print("[CORE] Starting orchestration")
    parsed_input = parse_prompt(user_prompt)
    print("[CORE] Orchestration finished")
    return parsed_input
