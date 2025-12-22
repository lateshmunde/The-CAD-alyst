#Branch - AISelector
# MyAISelector - Fusion 360 AI Selection Assistant

**MyAISelector** is a Fusion 360 Add-in that uses Artificial Intelligence (LLMs) to automate geometry selection. Instead of manually clicking hundreds of faces or bodies, you can simply type a natural language prompt like *"Select all the bolts"* or *"Select the heat sink fins"*, and the tool will automatically highlight the correct geometry and create a Selection Set for you.

## 🚀 Current Status & Features

* **Natural Language Processing:** Successfully interprets plain English prompts to understand user intent.
* **AI-Powered Backend:** Robust connection between Fusion 360 and an external Python environment (running LLMs like Groq) to analyze geometry names and metadata.
* **Accurate Identification:** The AI correctly identifies the specific Entity Tokens (IDs) for requested parts (e.g., correctly finding the "Cube" in a list of parts).
* **🚧 Under Development:**
    * **Visual Highlighting:** Automatic highlighting of identified bodies in the Fusion 360 viewport is currently being implemented.
    * **Selection Set Creation:** Automatic formation of persistent "Selection Set" folders in the browser is planned for the next release.

## 🛠️ Prerequisites

1.  **Autodesk Fusion 360** (Installed and running).
2.  **System Python 3.10+** (Installed on Windows/Mac).
3.  **External AI Libraries:** Your external `app.py` environment must be set up with necessary libraries (e.g., `groq`, `dotenv`).

## 📂 Installation

1.  **Locate Add-Ins Folder:**
    * Navigate to: `%AppData%\Autodesk\Autodesk Fusion 360\API\AddIns\` (Windows)
    * *Or:* `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/` (Mac)
2.  **Create Folder:** Create a new folder named `MyAISelector`.
3.  **Copy Files:** Place `MyAISelector.py` and `MyAISelector.manifest` into this folder.
4.  **Configure Paths:** Open `MyAISelector.py` and update the configuration section:
    ```python
    PYTHON_PATH = r"C:\Path\To\Your\System\Python\python.exe"
    APP_PATH = r"C:\Path\To\Your\Project\app.py"
    ```

## 🖥️ Usage

1.  Open Autodesk Fusion 360.
2.  Go to the **Utilities** tab -> **Scripts and Add-Ins** (Shift + S).
3.  Click the **Add-Ins** tab and find `MyAISelector`.
4.  Click **Run**.
5.  A dialog box will appear. Type your request (e.g., *"Select the cube"*).
6.  The AI will process your request, and the items will be selected in the viewport.

## 🔧 Troubleshooting

* **"No response file found":** Ensure your `PYTHON_PATH` is correct and points to the python executable that has your libraries installed.
* **"Invalid Argument Entity":** This usually happens with proxy objects. This version includes a specific fix using `createForAssemblyContext` to resolve this.
