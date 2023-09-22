# Termux Automation Scripts

This is a collection of scripts that make 
it easy to setup and use Termux on Android for 
beginner programmers.

**PS:** For iOS users, unfortunately, Termux does no work! More unfortunately, there are no comparative alternatives.
However, you can try **a-shell** for local programming (https://apps.apple.com/us/app/a-shell/id1473805438) and 
**xTerminal** for remote SSH access (https://apps.apple.com/us/app/xterminal-ssh-terminal-shell/id1544728400) - extra note: xTerminal is not free

## Requirements
+ Install Termux (Linux Terminal emulator) from **F-Droid** (https://f-droid.org/packages/com.termux), 
you can also download the Termux APK (Version 0.118.0) directly from the F-Droid repo here: https://f-droid.org/repo/com.termux_118.apk
+ We recommend at least a 2GB RAM Android phone.

## Initial Setup file
The very first file to run after downloading   
termux is termux_setup.

Here is the initialization syntax:
```
curl -Lo setup https://is.gd/themobileprof \
&& chmod +x ./setup \
&& ./setup \
&& exit
```
*OR*
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/master/termux_setup && chmod +x ./setup && ./setup && exit
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
1. The Editor setup script: https://raw.githubusercontent.com/themobileprof/scripts/master/editor_setup
1. The Apps setup script: https://raw.githubusercontent.com/themobileprof/scripts/master/apps_setup

## Cloud Setup Scripts
1. The GCP CLI setup script: https://raw.githubusercontent.com/themobileprof/scripts/master/gcp_cli_setup
1. The AWS CLI setup script: https://raw.githubusercontent.com/themobileprof/scripts/master/aws_cli_setup
1. The Azure CLI setup script: https://raw.githubusercontent.com/themobileprof/scripts/master/azure_cli_setup

For any feedbacks or enqiries, please reach out here: themobileprof.com @ gmail.com
