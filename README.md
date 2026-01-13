
# Hadith Terminal Greeter


## Prerequisites
Ensure you have the following installed on your system:

```bash
sudo apt update
sudo apt install python3 boxes lolcat git
````

## Installation

### 1. Clone the Repository

Clone this project into your home directory (or your preferred location):


```
git clone [https://github.com/YOUR_USERNAME/hadith-terminal-greeter.git](https://github.com/YOUR_USERNAME/hadith-terminal-greeter.git) ~/hadith_project
```

### 2. Configure Zsh

Add the execution logic to your `.zshrc` file to run on startup.

1. Open your config file:
    
    
    ```
    nano ~/.zshrc
    ```
    
1. Scroll to the bottom and paste the following block:

```
# --- Daily Hadith
echo ""
python3  ~/Documents/code/hadeeth_project/get_hadeeth.py | lolcat
echo ""
```

### 3. Apply Changes

Reload your terminal configuration:

Bash

```
source ~/.zshrc
```

## Project Structure

- **`get_hadith.py`**: Python script that parses the JSON files, selects a random entry, and strips file extensions for clean output.
- **`*.json`**: Database files containing Hadith collections (e.g., `nawawi40.json`).


Feel free to add more JSON files! Just make sure they follow the standard structure containing a `hadiths` list.