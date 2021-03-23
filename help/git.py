# Python 3

# Author: Samuel Anyaele - TheMobileprof.com
# scripts/help/git.py

import os
import time
from modules import git
from modules import misc

class MainMenu:
    def __init__(self):

        # 1. GIT
        self.git_class = git.Git()
        # 1a. Installation
        if not self.git_class.git_inst_var:
            self.git_class.git_inst()
        else:
            pass

        # 1b. Configuration
        if not self.git_class.config_name_var:
            self.git_class.git_conf('user.name',input("What is your name? "))
            self.git_class.git_conf('user.email',input("what is your email (for Github)? "))
            self.git_class.git_conf('init.defaultBranch', 'master')
            self.git_class.git_conf('pull.rebase', 'false')
        else:
            pass

        # 2. GITHUB
        self.gh_class = git.Github()
        # 2a. Installation
        if not self.gh_class.gh_inst_var:
            self.gh_class.gh_inst()
        else:
            pass

        # 2b. Configuration
        if not self.gh_class.gh_auth_var:
            self.gh_class.gh_auth_login()





    def show_menu(self):
        print("""> TheMobileprof Git Helper
        What would you like to do?
        1. Create a new Project (Init & Push)
        2. Copy a project from Github (Clone)
        3. Contribute to a Project (Fork)
        4. Save my changes (Commit & PR)
        5. Undo changes (Stash)
        6. Get the latest version of this project (Pull)
        0. To exit""")

        step = input("Choose a number from the menu above: ")
        time.sleep(1)
        
        return step







    def process_menu(self, argument):
        method_name = 'menu_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid menu option")
        # Call the method as we return it
        return method()

    # 1. Create a new Project (Init & Push)
    def menu_1(self):
        # git init
        if not self.git_class.git_init():
            exit()

        # Create base files
        open(".gitignore", mode='a').close()
        open("README.md", mode='a').close()


        # git add
        if self.git_class.git_add():
            # git commit
            self.git_class.git_commit("First commit")


        # git checkout development branch
        self.git_class.git_checkout("-b","dev")

        # Ensure there is Internet
        if not misc.internet_on():
            exit()
        
        # Ask to create Github repo
        github_proceed = input("Would you like to create a Github repo (Online)? Y/n: ")
        if github_proceed.lower() != 'y':
            exit()

        # github create new repo
        self.gh_class.gh_repo_new()

        # github push development
        self.git_class.git_push('dev', "--set-upstream")



 
    # 2. Copy a project from Github (Clone)
    def menu_2(self):
        self.gh_class.gh_repo_clone()
 
    # 3. Contribute to a Project (Fork)
    def menu_3(self):
        self.gh_class.gh_repo_fork() 

    # 4. Save my changes (Commit & PR)
    def menu_4(self):
        # git checkout development branch
        self.git_class.git_checkout("dev")

        # git add
        if self.git_class.git_add():
            # git commit
            self.git_class.git_commit()

        print('Development branch has been saved!')
        pr_merge = input("Would you like to save to the main branch now? Y/n: ")
        # Exit if user doesn't want to merge to master
        if pr_merge.lower() != "y":
            exit()

        # if forked, Pull Request else Merge
        if self.gh_class.confirm_fork():
            # github pull request to master xxxxxxx
            self.gh_class.gh_pr_new()
        else:
            # git merge to master
            if self.git_class.git_checkout("master"):
                self.git_class.git_merge("dev")
                self.git_class.git_push("master")
                self.git_class.git_checkout("dev")
        print('Saved!')
        time.sleep(2)
 
    # 5. Undo a change (Stash)
    def menu_5(self):
        if self.git_class.git_stash():
            print("Undo successful")
        else:
            print("Undo failed")

    # 6. Get the latest version of this project (Pull)
    def menu_6(self):
        self.git_class.git_pull()


# Process Menu
menu = MainMenu()
selected_option = menu.show_menu()
menu.process_menu(selected_option)


