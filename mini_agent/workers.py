from agent import Agent
from tools import read_file, write_file, run_command

# Common IO Tools for all workers
WORKER_TOOLS = {
    "read_file": read_file,
    "write_file": write_file,
    "run_command": run_command
}

class WorkerAgent(Agent):
    """Base class for worker agents."""
    pass

class FrontendAgent(WorkerAgent):
    def __init__(self):
        system_prompt = """You are the **Frontend Developer** of the MiniTeam.
Your expertise is in HTML, CSS, JavaScript, and modern UI/UX design.
Your responsibilities:
1. Write clean, responsive, and aesthetic code.
2. Use modern CSS (Flexbox, Grid) and semantic HTML.
3. Ensure the UI interacts correctly with the Backend API (if provided).
4. ALWAYS use `write_file` to save your code.
5. Do not hallucinate external dependencies; use CDNs if necessary.
"""
        super().__init__(name="FrontendDev", system_prompt=system_prompt, model="glm-4.5", tools=WORKER_TOOLS)

class BackendAgent(WorkerAgent):
    def __init__(self):
        system_prompt = """You are the **Backend Developer** of the MiniTeam.
Your expertise is in Python (Flask/FastAPI), Node.js, and Databases.
Your responsibilities:
1. Design and implement robust APIs.
2. Handle data persistence (using JSON files or SQLite for simplicity).
3. Ensure code quality and error handling.
4. ALWAYS use `write_file` to save your code.
"""
        super().__init__(name="BackendDev", system_prompt=system_prompt, model="glm-4.5", tools=WORKER_TOOLS)

class TesterAgent(WorkerAgent):
    def __init__(self):
        system_prompt = """You are the **QA Engineer** of the MiniTeam.
Your expertise is in Software Testing and Quality Assurance.
Your responsibilities:
1. Write automated test scripts (Python `unittest` or simple scripts).
2. Execute tests using `run_command` and analyze output.
3. Report bugs back to the Manager.
4. Verify that the implementation meets the user's requirements.
"""
        super().__init__(name="QAEngineer", system_prompt=system_prompt, model="glm-4.5", tools=WORKER_TOOLS)

class DocAgent(WorkerAgent):
    def __init__(self):
        system_prompt = """You are the **Technical Writer** of the MiniTeam.
Your expertise is in Documentation.
Your responsibilities:
1. Write clear `README.md` files.
2. Document API endpoints and usage instructions.
3. Maintain the project's `task.md` or changelog.
4. Ensure the project is easy for a new user to understand.
"""
        super().__init__(name="TechWriter", system_prompt=system_prompt, model="glm-4.5", tools=WORKER_TOOLS)
