# Degree to radian
import math
Degree = 32
Radian = Degree*(math.pi/180)
print(Radian)
#surface area and volume
radius = input("Enter The radius: ")
area = 4*(math.pi)*radius*radius
Volume = 4/3*(math.pi)*radius*radius*radius
print "Surface Area is: ", area
print "Volume is: ", Volume
#Time
import datetime
now = datetime.datetime.now()
print "Current date and time : "
print (now.strftime("%Y-%m-%d %H:%M:%S"))
#Split
names = "Kwame Akwetey"
data = names.split() 
for temp in data:
    print temp 
#Join
words = ['He', 'is', 'a', 'bad', 'boy']
print ' ',words.join
