import os
import types

class shell:
    def __init__(self):
        # --- List of all imported packages ---
        self.packages = []
        
        # --- Ash information and settings ---
        self.system = {
            "Shell": "Ash",
            "Version": "Ash 1.0",
            "Host": "root",
            "Shell": "konsole",
            "Path":"Local",
        }
        
        # --- Importing Packages ---
            
        for package in os.listdir("Packages"):
            self.packages.append(package)
                
            module = __import__(f"Packages.{package}.{package}", fromlist=[package])
            func = getattr(module, package)
            setattr(self, package, types.MethodType(func, self))
            
        # --- Shell Loop ---
        while True:
            shell = input(">>>").split(" ")
            
            if shell[0] in self.packages:
                self.output = getattr(self, shell[0])(shell[1:])
                getattr(self, self.system["Shell"])(self.output)