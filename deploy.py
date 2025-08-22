import subprocess
import os

# Nginx web root as project directory
PROJECT_DIR = "/var/www/html"
SERVICE_NAME = "nginx"

def run_command(command):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)

def deploy():
    print("Starting Deployment...")

    # Go to project folder
    os.chdir(PROJECT_DIR)

    # Pull latest code
    print("Pulling latest code from Git...")
    run_command("sudo git pull origin main")

    # Restart nginx
    print(f"Restarting service: {SERVICE_NAME}")
    run_command(f"sudo systemctl restart {SERVICE_NAME}")

    print("Deployment Complete!")

if __name__ == "__main__":
    deploy()
