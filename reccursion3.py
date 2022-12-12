def Display(No):
    fact=1
    if(No<0):
       fact=fact*No
       No=No-1
       Display(No)
        #No=No-1
       
       
        
        
    #return sum


print("Addition is:",Display(4))