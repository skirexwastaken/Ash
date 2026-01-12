# --- Importing source code  and libraries---
from Source.shell import shell
import os

# --- Cleaning shell ---
os.system('cls' if os.name == 'nt' else 'clear')

# --- Launching Ash shell ---
shell()