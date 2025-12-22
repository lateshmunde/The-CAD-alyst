The-CAD-alyst
│
├── ai
│   ├── prompts.py
│   └── prompt_parser.py
│
├── core
│   ├── orchestrator.py
│   │
│   ├── limits
│   │   └── physical_limits.py
│   │
│   ├── normalizers
│   │   └── units.py
│   │
│   └── validators
│
├── fusion
│   ├── adapter.py
│   ├── fusion_client.py
│   ├── cfd_setup.py
│   ├── cht_setup.py
│   ├── thermal_setup.py
│   │
│   └── api
│       ├── boundary_setup.py
│       └── simulation_runner.py
│
├── app.py
└── debug_gemini.py





````md
# Branch - BoundarySetup

CADalyst BoundarySetup – Fusion 360 AI-Driven Simulation Boundary Automation

BoundarySetup is a Fusion 360–focused PoC branch that enables **automatic simulation boundary condition setup** using natural language prompts.  
Instead of manually configuring CFD boundaries (velocity inlets, pressure outlets, temperatures), users can simply describe the simulation in plain English, and the system safely converts it into validated, physics-aware boundary conditions applied directly inside Fusion 360.

This branch **does NOT run simulations**.  
Its responsibility is **only to interpret prompts and correctly set up boundary conditions** on named faces.

---

## 🚀 Current Status & Features

### ✅ Implemented
- **Natural Language Prompt Parsing**
  - Converts prompts like  
    *“Run airflow at 50 m/s from inlet, outlet at pressure”*  
    into structured CFD boundary data.
- **Strict CFD Normalization**
  - AI output is normalized into a **Fusion-safe CFD config** (velocity, pressure only).
- **Unit Normalization**
  - Automatically converts km/h, mph, °C, °F → SI units.
- **Physical Safety Limits**
  - Prevents unsafe values (e.g. >150 m/s airflow, unrealistic temperatures).


### 🚧 In Progress / Planned
- Applies boundaries to named faces.
- Boundary conditions will be applied through Fusion’s API hooks.
- Persistent Simulation Study Creation.
- Multi-boundary support (multiple inlets/outlets).
- Expanded boundary types (heat flux, wall temperature).
- Better UI hints for unnamed or ambiguous faces.

---

## 🧠 Architecture Overview (BoundarySetup Scope)

```text
User Prompt (Fusion UI)
        ↓
AI Prompt Parser (LLM)
        ↓
Normalized CFD Config
        ↓
Validation & Physical Limits
        ↓
Fusion Boundary Dispatcher
        ↓
Named Face Mapping
        ↓
Boundary Conditions Applied
````

---

## 🛠️ Prerequisites

* **Autodesk Fusion 360** (installed & running)
* **System Python 3.10+**
* **Internet Access** (for LLM API during parsing)
* **Named Faces in CAD**

  * Faces must be named (e.g. `Inlet`, `Outlet`)
  * This is mandatory for BoundarySetup to work correctly

---

## 🖥️ Usage and Setup

Supported through Command Line only. 

1. **`python -m venv venv`**
   Creates a new isolated Python virtual environment named `venv`.

2. **`venv\Scripts\activate`**
   Activates the virtual environment so installed packages apply only to this project.

3. **`pip install openai requests python-dotenv`**
   Installs the OpenAI SDK, HTTP request library, and dotenv support for loading environment variables.

4. **`python -m pip install groq`**
   Installs the Groq Python client to interact with Groq-hosted LLM APIs.

5. **`make .env file with grokAPI key`**
   Stores the Groq API key securely as an environment variable instead of hard-coding it.

6. **`python app.py "Test wind flow at 150 m/s around a vehicle"`**
   Runs the Python application and passes a simulation prompt as a command-line argument.

---

## 🎯 Branch Philosophy (BoundarySetup)

* **Safety First** – No unsafe simulations.
* **No Hidden Magic** – AI suggests, validators decide.
* **PoC-Focused** – Minimal, robust, explainable.

---

## ✅ What This Branch Proves

* Natural language → **correct CFD boundaries**
* AI can assist **without making engineering decisions**
* Fusion 360 automation is feasible, safe, and scalable

---

**Branch:** `BoundarySetup`
**Purpose:** AI-assisted boundary condition setup (PoC)
**Next Step:** Full simulation study creation & solver execution in fusion.

```
```


