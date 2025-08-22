# Automated Deployment Script (Python + Nginx)

This repository contains an Automated Deployment Script written in Python3.  
The script pulls the latest code from a GitHub repository and deploys it to an Nginx server.

---

## Prerequisites
1. Install **Nginx** on your server.
2. Install **Python 3**.
3. Have a GitHub repository with your website or application code.

---

## Setup

1. Navigate to the Nginx default root directory:

```bash
cd /var/www/html
Initialize Git and link it to your repository:

bash
Copy
Edit
sudo git init
sudo git remote add origin <your-git-repo-url>
sudo git pull origin main
Replace <your-git-repo-url> with your repository URL.

If you face a Git safe directory error, run:

bash
Copy
Edit
sudo git config --global --add safe.directory /var/www/html
Deployment Script
In any location, create a file named deploy.py.

Copy the Python deployment script into deploy.py.

Run the script:

bash
Copy
Edit
sudo python3 deploy.py
