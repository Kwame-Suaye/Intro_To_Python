list = []
list.append('a')
print (list)
#Line 1 creates a variable for a group mof items
#Line 2 pushes a into the variable
#Line 3 prints the variable 'a'

#min_max
def even_num(min, max):
     even = []
     for a in range(min, max):
         if a % 2 ==0:
            even.append(a)
     return even
    
print(even_num(1,10))
Even_numbers=even_num(20,30)
print(Even_numbers)
    