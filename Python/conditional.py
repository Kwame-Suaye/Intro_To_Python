i = 8
if(i % 2 == 0):
    print ("Even Number")
else:
    print ("Odd Number")

#evens
def evens(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(evens([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#persons age
Age = int(input("Whats your age: "))
if Age >= 18:
   print("You are old")
else :
   print("You are young")
   
#Year
Year = int(input("Which Year Were you born: "))
age = 2019-Year
print("Your age is: ", age)

#Leap Year
year = int(input("Enter a year: "))
if year % 4==0:
   print("It is a leap Year")
else :
   print("It is not a Leap Year")
   