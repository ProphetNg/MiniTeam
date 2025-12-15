import os
import subprocess
from typing import Optional

def read_file(path: str, offset: int = 0, limit: Optional[int] = None, **kwargs) -> str:
    """
    Read the content of a file.
    
    Args:
        path: The absolute or relative path to the file.
        offset: The start line number (0-indexed).
        limit: The number of lines to read.
    
    Returns:
        The content of the file or an error message.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        if limit is None:
            return "".join(lines[offset:])
        else:
            return "".join(lines[offset:offset+limit])
            
    except Exception as e:
        return f"Error reading file {path}: {str(e)}"

def write_file(path: str, content: str) -> str:
    """
    Write content to a file. Overwrites if exists, creates if not.
    
    Args:
        path: The path to the file.
        content: The text content to write.
    
    Returns:
        Success message or error message.
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file {path}: {str(e)}"

def run_command(command: str) -> str:
    """
    Execute a shell command.
    
    Args:
        command: The command to run.
    
    Returns:
        Standard output and standard error combined.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True,
            timeout=120  # 2 minute timeout safety
        )
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except subprocess.TimeoutExpired:
        return "Error: Command timed out."
    except Exception as e:
        return f"Error executing command: {str(e)}"
