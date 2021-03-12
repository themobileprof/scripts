# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/git.py

import subprocess
import time

class Git:
    def __init__(self,pwd):
        self.pwd = pwd
        
        # Pretests to ensure system is git ready
        # 1. Ensure git is installed
        self.git_inst = True if subprocess.call(['which', 'git']) == 0 else False

        # 2. Ensure github cli is installed
        self.gh_inst = True if subprocess.call(['which', 'gh']) == 0 else False

        # 3. Ensure git is pre configured
        self.git_config_name = True if subprocess.call(['git', 'config', 'user.name']) == 0 else False

        self.git_config_email = True if subprocess.call(['git', 'config', 'user.email']) == 0 else False



    # Install git
    def git_inst(self):
        print("Installing Git...")
        print("ensure you are logged in as an admin user")
        time.sleep(2)
        return True if subprocess.call(['apt', 'install', '-y', 'git']) == 0 else return False

    # Configure git
    def git_config(self, config):
        print("Configuring git and github...")
        time.sleep(1)''
        subprocess.call(['git', 'config', '--global', config])


    # Install github cli
    def gh_inst(self):
        print("Installing Github CLI...")
        print("ensure you are logged in as an admin user")
        time.sleep(2)
        return True if subprocess.call(['apt', 'install', '-y', 'gh']) == 0 else return False

    # Configure github cli
    def gh_config(self):
        print("Configuring Github CLI...")
        print("Please ensure you copy the number below before pressing <Enter>, you'll past the number in the website that will open")
        time.sleep(4)
        subprocess.call(['gh', 'auth', 'login', '-w'])


    # Initialize a directory for git
    def git_init(self):
        print("Please ensure you are INSIDE the directory you want to add to git. ")
        print("You are currently inside " + self.pwd)
        time.sleep(2)
        print("Do you want to continue?")
        start = input("Yes/No: ")

        if start.lower() == 'yes' or start.lower() == 'y':
            # Start git init
            print("Git is initializing in this directory")
            git_init = subprocess.run(["git","init"])
            
            if git_init == 0:
                return True
            else:
                return False
        else:
            return False


    # Stage files for git
    def git_add(self):
        sleep 1


    def git_config(self):
        pass

    def git_commit(self):
        pass

    def git_push(self):
        pass

    def git_pull(self):
        pass
    
    def git_merge(self):
        pass

    def git_reset(self):
        pass

class Github:
    def __init__():
        pass

