def Display(No):
    if(No>0):
        
        
        No=No-1
        Display(No)
        print(No+1)

Display(4)