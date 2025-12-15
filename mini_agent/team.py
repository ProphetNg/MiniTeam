from typing import Dict, Any, List
import json
from agent import Agent
from workers import FrontendAgent, BackendAgent, TesterAgent, DocAgent
from tools import read_file

class Manager(Agent):
    def __init__(self):
        # 1. Initialize Workers
        self.frontend = FrontendAgent()
        self.backend = BackendAgent()
        self.tester = TesterAgent()
        self.doc = DocAgent()
        
        # 2. Define Tools (Delegation)
        # We bind these methods to the tools map
        tools_map = {
            "assign_frontend_task": self.assign_frontend_task,
            "assign_backend_task": self.assign_backend_task,
            "assign_testing_task": self.assign_testing_task,
            "assign_doc_task": self.assign_doc_task,
            "read_file": read_file # Manager can read to inspect, but not write
        }
        
        # 3. System Prompt
        system_prompt = """You are the **Manager (Architect)** of the MiniTeam.
Your goal is to orchestrate a team of specialized AI agents to build complex software projects.

**Your Team:**
1. **FrontendDev**: Expert in HTML/CSS/JS.
2. **BackendDev**: Expert in Python/Node/API/DB.
3. **QAEngineer**: Expert in testing and verification.
4. **TechWriter**: Expert in documentation (README.md, etc.).

**Your Responsibilities:**
1. **Analyze** the user's request using Chain of Thought (CoT).
2. **Break down** the project into discrete steps.
3. **Delegate** tasks to the appropriate worker using the `assign_*_task` tools.
   - Be specific in your instructions to workers.
   - You can assign multiple tasks sequentially.
4. **Review** the results (you can use `read_file` to check files).
5. **Report** the final status to the user.

**Rules:**
- DO NOT write code yourself. Always delegate.
- DO NOT use `write_file` or `run_command` directly.
- If a worker fails, analyze why and give them new instructions.
"""
        # Initialize Base Agent
        super().__init__(name="Manager", system_prompt=system_prompt, model="glm-4.5", tools=tools_map)
        
        # 4. Manually Define Tools Schema (since generic generator is limited)
        self.tools_schema = [
            {
                "type": "function",
                "function": {
                    "name": "assign_frontend_task",
                    "description": "Delegate a task to the Frontend Developer (HTML/CSS/JS).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "instruction": {"type": "string", "description": "Detailed instruction for the frontend task."}
                        },
                        "required": ["instruction"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "assign_backend_task",
                    "description": "Delegate a task to the Backend Developer (Python/API/DB).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "instruction": {"type": "string", "description": "Detailed instruction for the backend task."}
                        },
                        "required": ["instruction"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "assign_testing_task",
                    "description": "Delegate a task to the QA Engineer (Writing and running tests).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "instruction": {"type": "string", "description": "Detailed instruction for the testing task."}
                        },
                        "required": ["instruction"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "assign_doc_task",
                    "description": "Delegate a task to the Technical Writer (Documentation).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "instruction": {"type": "string", "description": "Detailed instruction for the documentation task."}
                        },
                        "required": ["instruction"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "description": "Read the content of a file to inspect worker's output.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {"type": "string", "description": "Path to the file"}
                        },
                        "required": ["path"]
                    }
                }
            }
        ]

    # --- Tool Implementations ---
    def assign_frontend_task(self, instruction: str) -> str:
        return self._delegate("FrontendDev", self.frontend, instruction)

    def assign_backend_task(self, instruction: str) -> str:
        return self._delegate("BackendDev", self.backend, instruction)

    def assign_testing_task(self, instruction: str) -> str:
        return self._delegate("QAEngineer", self.tester, instruction)

    def assign_doc_task(self, instruction: str) -> str:
        return self._delegate("TechWriter", self.doc, instruction)

    def _delegate(self, role: str, agent: Agent, instruction: str) -> str:
        print(f"\n[Manager] -> Delegating to {role}...")
        response = agent.chat(instruction)
        print(f"[{role}] -> Task Complete.")
        return f"[{role} Report]: {response}"
