import numpy as np
import random as rand




def dice(dictionary):

    number = rand.randint(1,6)
    for i in dictionary:   
        if(i == number):
            dice = dictionary.get(i)
        
     
         
            
       
    
    return number, dice


