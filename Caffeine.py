import math

#input for caffeine level

startLevel = float ((input) ("Please enter starting caffeine level."))

#this is first half life
six = startLevel / 2.0
print (("The caffeine level after six hours is ") , (six) , ("mg"))
 
#this is second half life
twelve = six / 2.0
print (("The caffeine level after twlve hours is ") , (twelve) , ('mg'))

#this is third half life
eighteen = twelve / 2
print (("The caffeine level after eighteen hours is ") , (eighteen) , ("mg"))

#this will keep the program open until you are ready to exci
input ('Press ENTER to exit')