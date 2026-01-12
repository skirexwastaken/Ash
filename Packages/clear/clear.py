# --- Package that cleans shell ---
import os
def clear(self,shell):
    os.system('cls' if os.name == 'nt' else 'clear')