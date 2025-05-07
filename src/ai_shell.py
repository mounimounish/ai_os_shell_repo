import subprocess
import shlex
import os
import time
import logging
import uuid

class AIDrivenShell:
    def __init__(self):
        self.session_active = False
        self.command_history = []
        self.log_file = "ai_os.log"
        self.output_store = {}
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def start_session(self):
        self.session_active = True
        logging.info(f"[{time.ctime()}] Terminal session started.")
        print("🔓 Terminal session started.")

    def validate_command(self, command):
        dangerous = ['rm -rf', ':(){ :|: & };:', 'shutdown', 'reboot']
        for d in dangerous:
            if d in command:
                raise PermissionError(f"⛔ Dangerous command blocked: {command}")
        return True

    def preprocess_command(self, command):
        # Placeholder for natural language → command transformation
        return command

    def execute_command(self, command):
        if not self.session_active:
            raise RuntimeError("❌ Terminal session not started.")
        
        try:
            self.validate_command(command)
            command = self.preprocess_command(command)
            result = subprocess.run(shlex.split(command), capture_output=True, text=True)
            self.log_command(command)
            self.store_output(command, result.stdout, result.stderr)
            self.enhance_post_execution(command, result.stdout, result.stderr)
            return result.stdout, result.stderr
        except Exception as e:
            logging.error(f"[{time.ctime()}] Error: {str(e)}")
            print(f"⚠️ Error: {str(e)}")
            return None, str(e)

    def log_command(self, command):
        self.command_history.append(command)
        logging.info(f"[{time.ctime()}] Executed: {command}")

    def store_output(self, command, stdout, stderr):
        """Save command output persistently"""
        cmd_id = str(uuid.uuid4())
        self.output_store[cmd_id] = {
            "command": command,
            "stdout": stdout,
            "stderr": stderr,
            "timestamp": time.ctime()
        }

    def enhance_post_execution(self, command, stdout, stderr):
        """Enhance results with tagging, analysis, AI feedback"""
        print("🔍 Enhancing post-execution:")
        
        # Semantic Tagging (placeholder)
        if "ping" in command or "curl" in command:
            tag = "network"
        elif "ls" in command or "cat" in command:
            tag = "filesystem"
        else:
            tag = "general"
        
        print(f"🧾 Tagged as: {tag}")
        logging.info(f"Tagged '{command}' as: {tag}")

        # Placeholder for system state capture
        print("🛠️ Capturing system state changes... [mocked]")

        # Optional: AI-powered feedback or rollback suggestion
        if "error" in stderr.lower():
            print("🧠 AI Feedback: That command had issues, want to retry differently?")
        elif stdout:
            print("🧠 AI Feedback: Command ran successfully.")

    def interpret_output(self, stdout, stderr):
        if stderr:
            print("❗ An error occurred. Maybe retry with different parameters?")
        elif "Permission denied" in stdout:
            print("🔐 You might need sudo privileges.")
        else:
            print("✅ Output looks good!")

    def suggest_next_command(self):
        print("🤖 Suggesting next command based on previous context...")

    def summarize_session(self):
        print("📝 Session Summary:")
        for i, cmd in enumerate(self.command_history, 1):
            print(f"{i}. {cmd}")
        print("📦 Output history stored for AI training or review.")

    def close_session(self):
        self.session_active = False
        logging.info(f"[{time.ctime()}] Terminal session closed.")
        print("🔒 Terminal session closed.")

    def get_command_history(self):
        return self.command_history
