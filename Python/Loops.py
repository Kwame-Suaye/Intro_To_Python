i = 0
while(i < 10):
    i = i + 1
    print (i)
j = 7
while(j < 17):
    j = j + 1
    print(j)
#even number
minimum = 12
maximum = 20

for number in range(minimum, maximum+2):
    if(number % 2 == 0):
        print("{0}".format(number))
        
#input numbers
minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(minimum, maximum+2):
    if(number % 2 == 0):
        print("evens: ", "{0}".format(number))

  

        