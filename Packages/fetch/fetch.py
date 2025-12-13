def fetch(self,shell):
    return(
            f"OS: {self.system["OS"]}\n"
            f"Kernel: {self.system["Kernel"]}\n"
            f"Path: {self.system["Path"]}\n"
            f"Host: {self.system["Host"]}\n"
            f"Shell: {self.system["Shell"]}\n"
            f"Packages: {len(self.packages)}"
            )