# Hadeeth Terminal Greeter

A lightweight Zsh integration that displays a random Hadith from the Nawawi 40, Qudsi, and Shah Waliullah collections every time you open your terminal.

<img width="1919" height="547" alt="image" src="https://github.com/user-attachments/assets/f35dcb31-576a-47ae-a44e-695e499edb8d" />



## Prerequisites
You need a few lightweight tools installed:

```bash
sudo apt update
sudo apt install python3 lolcat

```



## Installation

### 1. Clone the Repository

Clone the project to your home directory:

```bash
git clone https://github.com/TalhaMaaz/Terminal-hadeeth-greeter.git ~/hadeeth_project

```



### 2. Configure Zsh/bash

To run the greeter on startup, add the following block to the bottom of your `~/.zshrc` or `~/.bashrc` file:

```bash
echo ""
python3  ~/hadeeth_project/get_hadeeth.py | lolcat
echo ""
```



### 3. Apply Changes

Reload your terminal configuration:

```bash
source ~/.zshrc  # or source ~/.bashrc

```
