import json
import types

class kernel:
    def __init__(self):
        self.packages = []
        
        # --- Importing Packages ---
        with open("Packages/packages.json","r") as module_paths_file:
            packagesToImport = json.load(module_paths_file)["essentials"]
            
            for packagePath, packageName in packagesToImport.items():
                
                self.packages.append(packageName)
                
                module = __import__(f"Packages.{packageName}.{packagePath}", fromlist=[packageName])
                func = getattr(module, packageName)
                setattr(self, packageName, types.MethodType(func, self))
        
        self.system = {
            "OS": "Ash",
            "Kernel": "Ash 1.0",
            "Host": "root",
            "Shell": "konsole",
            "Path":"Local",
        }
        
        while True:
            shell = input(">>>").split(" ")
            
            if shell[0] in self.packages:
                self.output = getattr(self, shell[0])(shell[1:])
                getattr(self, self.system["Shell"])(self.output)