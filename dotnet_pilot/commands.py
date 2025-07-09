import subprocess
import threading
from tkinter import messagebox

def run_command(command, working_directory, append_output_func):
    if not command or not command.strip():
        messagebox.showwarning("Warning", "Please enter a command or fill required fields.")
        return
    
    if not working_directory or not working_directory.strip():
        messagebox.showwarning("Warning", "Working directory is required.")
        return
        
    append_output_func(f"\n> {command}\n")
    
    def execute():
        try:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=working_directory,
                bufsize=1,
                universal_newlines=True
            )
            
            stdout, stderr = process.communicate(timeout=300)
            
            if stdout:
                append_output_func(stdout)
            if stderr:
                append_output_func(f"ERROR: {stderr}")
                
            if process.returncode == 0:
                append_output_func("[SUCCESS] Command completed successfully!\n")
            else:
                append_output_func(f"[ERROR] Command failed with exit code: {process.returncode}\n")
                
        except subprocess.TimeoutExpired:
            process.kill()
            append_output_func("[ERROR] Command timed out after 5 minutes\n")
        except FileNotFoundError:
            append_output_func("[ERROR] Command not found or working directory doesn't exist\n")
        except Exception as e:
            append_output_func(f"[ERROR] Error executing command: {str(e)}\n")
    
    # Run command in separate thread to prevent GUI freezing
    threading.Thread(target=execute, daemon=True).start()
