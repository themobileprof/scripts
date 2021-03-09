# Termux Automation Scripts

This is a collection of scripts that make 
it easy to setup Termux on Android for 
beginner programmers.

## Initial Setup file
The very first file to run after downloading 
termux is termux_setup
Here is the initialization syntax:
```
curl -Lo setup \
&& https://is.gd/themobileprof \
&& chmod +x setup \
&& ./setup \
&& exit
```
*OR*
```
curl -Lo setup https://raw.githubusercontent.com/themobileprof/scripts/master/termux_setup && chmod +x setup && ./setup && exit
```
This will Script do the following:
1. Update Termux
1. Install Openssh
1. Install and Setup Openssl
1. Install unzip
1. Install and Configure Git
1. Install Gh (Github CLI)
1. Install Python & pip
1. Install Nodejs and Npm
1. Install Neovim 
    1. Download Neovim config file from (Github.com/themobileprof/env)
    1. Using vim-plug, install Neovim plugins
1. Install Zsh

After this, restart Termux.
