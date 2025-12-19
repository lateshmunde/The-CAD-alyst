# app.py
import sys
from core.orchestrator import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nUsage: python app.py \"<your simulation scenario>\"")
        print("Example: python app.py \"High speed aerodynamics of a formula 1 car\"\n")
        sys.exit(1)

    user_prompt = sys.argv[1]
    run(user_prompt)
