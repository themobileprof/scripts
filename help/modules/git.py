# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/git.py

import subprocess
import time
import os
from . import misc

class Git:
    def __init__(self):
        # Get current directory
        self.pwd = misc.current_dir()

        # Pre-tests to ensure system is git ready
        # 1A. Ensure git is installed
        self.git_inst_var = True if subprocess.run(['which', 'git'], stdout=subprocess.DEVNULL).returncode == 0 else False

        # 2A. Ensure git user.name is configured
        config_name=subprocess.run(['git', 'config', 'user.name'], capture_output=True, text=True)
        self.config_name_var = True if config_name.returncode == 0 and config_name.stdout.strip() != "" else False

        # 2B. Ensure git user.email is configured
        config_email=subprocess.run(['git', 'config', 'user.email'], capture_output=True, text=True)
        self.config_email_var = True if config_email.returncode == 0 and config_email.stdout.strip() != "" else False





    # Install git
    def git_inst(self):
        print("Installing Git...")
        print("ensure you are logged in as an admin user")
        time.sleep(2)
        return True if subprocess.run(['apt', 'install', '-y', 'git']) == 0 else False






    # Configure git
    def git_conf(self, config, value=""):
        print("Configuring git ", config)
        time.sleep(1)
        subprocess.run(['git', 'config', '--global', config, value])







    # Initialize a directory for git
    def git_init(self):
        print("Please ensure you are INSIDE the directory you want to initialize on git. ")
        print("You are currently inside " + self.pwd)
        time.sleep(2)
        print("Do you want to continue?")
        start = input("Yes/No: ")

        if start.lower() == 'yes' or start.lower() == 'y':
            # Start git init
            print("Git is initializing in this directory")
            git_init = subprocess.run(["git","init"])
            
            if git_init.returncode == 0:
                return True
            else:
                return False
        else:
            return False







    # Stage files for git
    def git_add(self):
        return True if subprocess.run(['git', 'add', '-A'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False



    # Commit Staged files with a commit message
    def git_commit(self, description=""):
        if description == "":
            description = input("Label the changes you made: ")
        return True if subprocess.run(["git","commit","-m",description], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False


    
    # Git checkout for navigating branches and undoing changes
    def git_checkout(self, opt1, opt2=""):
        if opt2 == "":
            commands = ["git","checkout",opt1]
        else:
            commands = ["git","checkout",opt1,opt2]
        
        return True if subprocess.run(commands, cwd=git_root.strip(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False



    # Git Undo a project
    def git_stash(self):
        # Add files before stashing them
        self.git_add()

        # Stash changes
        stash = True if subprocess.run(["git","stash"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False
        if stash:
            return True if subprocess.run(["git","stash","clear"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False




    # Git push to Remote repo
    def git_push(self,local,option="",remote="origin"):
        return True if subprocess.run(["git","push",option,remote,local], stdout=subprocess.DEVNULL).returncode == 0 else False

    

    # git pull updates from remote
    def git_pull(self):
        return True if subprocess.run(["git","pull"], stdout=subprocess.DEVNULL).returncode == 0 else False
    

    # git merge branches
    def git_merge(self,branch):
        return True if subprocess.run(["git","merge",branch], stdout=subprocess.DEVNULL).returncode == 0 else False

    # Git list commit logs
    def git_logs(self):
        return subprocess.run(["git","log","--oneliner"], capture_output=True, text=True).stdout


    # Git reset to previous commits
    def git_reset(self):
        commit = input("Input the commit code you want to go back to: ")
        return True if subprocess.run(["git","reset","--hard",commit], stdout=subprocess.DEVNULL).returncode == 0 else False









class Github:
    def __init__(self):

        # Pretests to ensure system is github ready
        # 1. Ensure github cli is installed
        self.gh_inst_var = True if subprocess.run(['which', 'gh'], stdout=subprocess.DEVNULL).returncode == 0 else False

        # 2. Ensure github cli is authenticated
        self.gh_auth_var = True if subprocess.run(['gh', 'auth', 'status'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False







    # Install github cli
    def gh_inst(self):
        print("Installing Github CLI...")
        print("ensure you are logged in as an admin user")
        subprocess.run(['sudo', 'su'], stderr=subprocess.DEVNULL)
        time.sleep(2)
        return True if subprocess.run(['apt', 'install', '-y', 'gh'], stdout=subprocess.DEVNULL) == 0 else False







    # Configure github cli
    def gh_auth_login(self):
        print("Configuring Github CLI...")
        print("Please ensure you copy the number below before pressing <Enter>, you'll past the number in the website that will open")
        time.sleep(4)
        subprocess.run(['gh', 'auth', 'login', '-w'])





    # Clone a Repo
    def gh_repo_clone(self):
        repo = input("What Repo are you Cloning?: ")
        directory = input("What do you want to call this project? \nPress <Enter> for default: ")
        clone_result = True if subprocess.run(["gh","repo","clone",repo,directory], stdout=subprocess.DEVNULL).returncode == 0 else False

        if clone_result:
            print("\nThe {} project directory has been successfully created".format(repo))

        return clone_result




    # Create a Pull Request
    def gh_pr_new(self,base="master",head="dev"):
        return True if subprocess.run(["gh","pr","create","--assignee","@me","--base",base,"--head",head,"--fill"]).returncode == 0 else False






    # Create new github repo
    def gh_repo_new(self):
        directory = os.path.basename(os.getcwd())
        public = input("Should this Github repo be visible to the public?: Y/n ")
        if public.lower() in ("y","yes"):
            visible = "--public"
        else:
            visible = "--private"

        return True if subprocess.run(["gh","repo","create",directory,visible,"--confirm"]).returncode == 0 else False



    # Fork a Repo
    def gh_repo_fork(self):
        repo = input("What Repo are you collaborating on?: ")
        # Get directory name
        repo_file = repo.split("/")
        dir_name = repo_file[-1].split(".")
        
        is_cloned = True if subprocess.run(["gh","repo","fork",repo,"--clone=true","--remote=true"]).returncode == 0 else False
        if os.path.exists(dir_name[0]):
            os.chdir(dir_name[0])

        if is_cloned:
            print("Enter \"cd ",dir_name[0],"\" to enter into the project directory")

        return is_cloned




    # Confirm a Fork
    def confirm_fork(self):
        remotes = subprocess.run(["git","remote","-v"], capture_output=True, text=True).stdout

        if remotes.find("upstream") == -1:
            return False
        else:
            return True





    # List a user's repos
    def gh_repo_list(self,owner=""):
        return subprocess.run(["gh","repo","list",owner], capture_output=True, text=True).stdout



    # Add local SSH key to Github
    def gh_ssh_add(self):
        public_key = os.getenv('HOME')+'/.ssh/id_rsa.pub'
        return True if subprocess.run(["gh","ssh-key","add",public_key]).returncode == 0 else False
