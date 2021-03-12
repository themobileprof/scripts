# Python 3
# Author: Samuel Anyaele - TheMobileprof.com
# scripts/help/git.py

import os
import time
from modules import git

class MainMenu:
    def show_menu(self):
        print("""This is the TMP Git Helper, what would you like to do?
        1. Add a new Project
        2. Get an existing project from Github
        3. Save my changes
        4. Undo a change
        5. Get the latest version of this project""")

        step = input("Choose a number from the menu above: ")
        time.sleep(1)
        
        return step


    def process_menu(self, argument):
        method_name = 'menu_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid menu option")
        # Call the method as we return it
        return method()
 
    def menu_1(self):
        # Add a new project
        # git_init
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()
        git_process = git.Git("~/" + os.path.relpath(current_dir, home_dir))
        git_result = git_process.git_init()
 
    def menu_2(self):
        pass
 
    def menu_3(self):
        pass

    def menu_4(self):
        pass
 
    def menu_5(self):
        pass


# Process Menu
menu = MainMenu()
selected_option = menu.show_menu()
menu.process_menu(selected_option)


