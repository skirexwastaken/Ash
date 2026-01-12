# --- Package that manages CLI interface ---
def konsole(self,output):
    if output:
        if isinstance(output,list):
            for line in output:
                print(line)
    
        else:
            print(output)