import os
import json
from typing import List, Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv
from tools import read_file, write_file, run_command

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

class Agent:
    def __init__(self, name: str = "MiniAgent", system_prompt: str = None, model: str = None, tools: Dict[str, Any] = None):
        self.name = name
        self.api_key = os.getenv("ZHIPUAI_API_KEY")
        self.base_url = os.getenv("ZHIPUAI_BASE_URL")
        self.model = model if model else os.getenv("ZHIPUAI_MODEL", "glm-4-air")
        
        if not self.api_key:
            raise ValueError("ZHIPUAI_API_KEY not found in .env")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        default_prompt = "You are MiniAgent, a helpful coding assistant. You can read/write files and execute commands. \n\nIMPORTANT: FILE MANAGEMENT RULES\n1. You are consistent and organized.\n2. All your work must be done inside the 'workspace/' directory.\n3. For each new distinct project or task, you MUST create a new folder inside 'workspace/' with a meaningful name (e.g., 'workspace/personal_website', 'workspace/calculator_app').\n4. Always verify file content before modifying it.\n5. When running commands, ensure you understand the side effects.\n\nCRITICAL TOOL USAGE RULES:\n- You are an autonomous agent with file system access.\n- If the user asks you to write code, create a file, or build a project, you MUST use the `write_file` tool to save it to disk.\n- DO NOT just print the code in your response.\n- DO NOT write python code to call the tools (e.g., do not write `write_file(...)` in the chat). You must generate the actual tool call object.\n- EXECUTE the function for every file you generate."

        self.messages: List[Dict[str, Any]] = [
            {"role": "system", "content": system_prompt if system_prompt else default_prompt}
        ]
        
        # If tools are provided, use them. Otherwise use default IO tools.
        if tools is not None:
             self.available_tools = tools
        else:
             self.available_tools = {
                "read_file": read_file,
                "write_file": write_file,
                "run_command": run_command
            }
        
        # Generate tools schema from available_tools
        self.tools_schema = self._generate_tools_schema()

    def _generate_tools_schema(self):
        # We need to dynamically generate the schema based on available_tools
        # For simplicity, we can hardcode the schema for known tools or use a helper
        # Since the original code hardcoded it, we will keep the hardcoded schema for default tools,
        # and assume custom tools will be handled or added manually.
        # Ideally, we should inspect the functions to generate schema, but to save time refactoring:
        
        # If using standard tools, return standard schema
        if set(self.available_tools.keys()) == {"read_file", "write_file", "run_command"}:
             return [
            {
                "type": "function",
                "function": {
                    "name": "read_file",
                    "description": "Read the content of a file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {"type": "string", "description": "The path to the file"}
                        },
                        "required": ["path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "write_file",
                    "description": "Write content to a file. Creates directories if needed.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {"type": "string", "description": "The path to the file"},
                            "content": {"type": "string", "description": "The content to write"}
                        },
                        "required": ["path", "content"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "run_command",
                    "description": "Run a shell command",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "command": {"type": "string", "description": "The command to run"}
                        },
                        "required": ["command"]
                    }
                }
            }
        ]
        return [] # Placeholder for custom tools schema logic if needed

    def chat(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})
        
        while True:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=self.tools_schema,
                tool_choice="auto"
            )
            
            message = response.choices[0].message
            self.messages.append(message)
            
            if not message.tool_calls:
                return message.content
            
            # Handle tool calls
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                if function_name in self.available_tools:
                    # In a real app, you might want to print prompt here for dangerous actions
                    func = self.available_tools[function_name]
                    result = str(func(**function_args))
                    
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
                    
                    # Reflection Logic: If tool returned an error, force analysis
                    if result.startswith("Error") or "Error:" in result[:20]:
                        self.messages.append({
                            "role": "system",
                            "content": "The previous tool execution failed. Please analyze the error message above, explain why it happened, and then attempt a different approach to solve the problem."
                        })
                else:
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": f"Error: Tool {function_name} not found"
                    })
