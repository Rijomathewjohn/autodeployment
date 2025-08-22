This is a repo for a Automated Deployment Script using python3.
Here the code is pulled from the github and run using nginx server.




First install nginx server and goto its file location, default is "/var/www/html". Then,
*must use "sudo" while doing this cmds else you can change the folder permissions.
_______________________________________________________
cd /var/www/html
sudo git init
sudo git remote add origin <your-git-repo-url>
sudo git pull origin main
_______________________________________________________
Here you must have create a repository and add its "your-git-repo-url" while you run your commands.
Then u may ran into a security issue which means says that the directory is not safe, then u can run this "sudo git config --global --add safe.directory /var/www/html"



So in any path you can add a new file named "deploy.py", also make sure python is installed.
In the deploy.py file add,
___________________________________________________________________________________________________
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
___________________________________________________________________________________________________



Then you can run the python deployment script using "sudo python3 deploy.py"
This pull latest code from github and release to nginx server.
