# --- Package that displays system information and settings ---
def fetch(self,shell):
    return(
            f"Shell: {self.system["Shell"]}\n"
            f"Version: {self.system["Version"]}\n"
            f"Path: {self.system["Path"]}\n"
            f"Host: {self.system["Host"]}\n"
            f"Shell: {self.system["Shell"]}\n"
            f"Packages: {len(self.packages)}"
            )