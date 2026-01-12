# ---- Simply package that shows information about packages from their .txt files ---
def show(self,shell):
    if len(shell) == 1:
        if shell[0] in self.packages:
            with open(f"Packages/{shell[0]}/{shell[0]}.txt") as file:
                return (file.readlines())
        
        elif shell[0] == "all":
            return (self.packages)
        
        else:
            return ("Syntax Error")
            
    else:
        return ("Syntax Error")