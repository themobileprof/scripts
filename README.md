# Termux Automation Scripts

This is a collection of scripts that make 
it easy to setup and use Termux on Android for 
beginner programmers.

> [!IMPORTANT]
> ## Requirements
> + Install Termux (Linux Terminal emulator) from **F-Droid** (https://f-droid.org/packages/com.termux), 
you can also download the Termux APK (Version 0.118.0) directly from the F-Droid repo here: https://f-droid.org/repo/com.termux_118.apk
> + We recommend at least a 2GB RAM Android phone.

> [!NOTE]
> For iOS users, unfortunately, Termux does no work! More unfortunately, there are no comparative alternatives.
However, you can try [**a-shell** for local programming](https://apps.apple.com/us/app/a-shell/id1473805438) and 
[**xTerminal** for remote SSH access](https://apps.apple.com/us/app/xterminal-ssh-terminal-shell/id1544728400) - extra note: xTerminal is not free

## Initial Setup file
The very first file to run after downloading   
termux is termux_setup.

Here is the initialization syntax:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/termux_setup && chmod +x ./setup && ./setup && exit
```
This Script will do the following:
1. Update Termux
1. Install Openssh
1. Install and Setup Openssl
1. Install Unzip
1. Install and Configure Git
1. Install Gh (Github CLI)
1. Install Zsh
After this, exit (if the script doesn't do that automatically)
and reopen Termux.

# Other Scripts
Additionally we have more scripts too for other functionalities:

## Other Local Setup Scripts
1. [The Editor setup script](../blob/develop/editor_setup): This installs Neovim, a fork of Vim and the defactor code editor on Linux terminal. To use this script in Termux, copy and paste the below snippet of code into your terminal:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/editor_setup && chmod +x ./setup && ./setup && exit
``` 
1. [The Apps setup script](../blob/develop/apps_setup): This script installs programming languages like Python, NodeJS, and PHP. To use this script in Termux, copy and paste the below snippet of code into your terminal:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/apps_setup && chmod +x ./setup && ./setup && exit
``` 

## Cloud Setup Scripts
1. [The GCP CLI setup script](../blob/develop/gcp_cli_setup): This script installs Google cloud CLI for managing Google Cloud resources. To use this script in Termux, copy and paste the below snippet of code into your terminal:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/gcp_cli_setup && chmod +x ./setup && ./setup && exit
``` 
1. [The AWS CLI setup script](../blob/develop/aws_cli_setup): This script installs AWS CLI for managing Amazon Web Services. To use this script in Termux, copy and paste the below snippet of code into your terminal:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/aws_cli_setup && chmod +x ./setup && ./setup && exit
``` 
1. [The Azure CLI setup script](../blob/develop/azure_cli_setup): This script installs Azure CLI for managing Microsoft Azure Cloud resources. To use this script in Termux, copy and paste the below snippet of code into your terminal:
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/develop/azure_cli_setup && chmod +x ./setup && ./setup && exit
``` 

For any feedbacks or enqiries, please reach out here: themobileprof.com @ gmail.com
