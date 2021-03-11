# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/git.py

import subprocess

class Git:
    def __init__(self,pwd):
        self.pwd = pwd

    def git_init(self):
        print("Please ensure you are INSIDE the directory you want to add to git. ")
        print("You are currently inside " + self.pwd)
        print("Do you want to continue?")
        start = input("Yes/No: ")

        if start.lower() == 'yes' or start.lower() == 'y':
            # Start git init
            print("Git is initializing in this directory")
            gitInit = subprocess.run(["git","init"])
            return True
        else:
            return False


class Github:
    def __init__():
        pass

