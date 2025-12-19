# app.py

import sys
from core.orchestrator import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py \"your simulation prompt\"")
        sys.exit(1)

    user_prompt = sys.argv[1]
    run(user_prompt)

