""" #ex1: print line by line 
print ('Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star,\n\t\t How I wonder what you are')

#ex2: print python version 
import sys
print('Python version')
print(sys.version)
print('Info')
print(sys.version_info) """

""" #ex3:write date and time 
import datetime
time = datetime.datetime.now()
print ('current date and time = ' + str(time.strftime("%d-%m-%Y  %H:%M:%S"))) """

""" #ex4: radius input output area
from math import pi 
inp= float(input('input the radius of the circle : '))
Area= pi*inp**2
print('Area = ' + str(Area))  """

""" #ex; reverse two names 
first_name = str(input('first name = '))
last_name = str(input('last name = '))
print ('welcome ' + str(last_name) + ' ' + str(first_name) ) """

""" #Ex6: inp comma seperated numbers and outputs in list or tuple format 
values = (input('input anything seperated with commas = '))
list= values.split(',')
tuple=tuple(list)
print (list)
print(tuple) """

""" #ex7: to take in the user file and print its extention :
#ans: same as 6th just split it from . and print list[-1]
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1])) """

""" #ex8:to display first and last colors from the list 
values= input('input any color names : ')
list =values.split(',')
print ('first color is '+ str(list[0]) + ' & last color is ' + str(list[-1])) """

""" #Ex9: extract values from list and display as a date  
value= input('input the date :')
list=value.split(',')
print('The date is ' + str(list[0])+'/'+ str(list[1])+'/'+ str(list[2]))
 """

"""  #ex10: accept n and return n+nn+nnn
a = int(input("Input an integer : "))
n1 = int ( '%s' % a )
n2 = int ('%s%s' % (a,a) )
n3 = int ( '%s%s%s' % (a,a,a) )
print (n1+n2+n3)
 """

""" #ex11:to print syntax of an in built function of python we use __doc__
print(abs.__doc__) """

""" #ex12 : print calendar of a given month and year
import calendar
y= int(input('year = '))
m= int(input('month = '))
print(calendar.month(y, m)) """

"""  #ex13: python string as it is written use """  """ inside print 
print("
       what 
        is 
        up")  """

#ex14: program to calculate number of days between two given dates 
""" start_date= int(input('starting date = '))
end_date = int(input('end date = '))
list_start= start_date.split('/')
end_date= end_date.split('/')
y=(list_start[0]-end_date[0])*365
m=(list_start[0]-end_date[0]) """

""" #easy approach 
from datetime import date
f_date = (input('final date= '))
i_date = (input('initial date= '))
list_i= i_date.split('/')
list_f= f_date.split('/')
i= date(int(list_i[0]), int(list_i[1]) , int(list_i[2]))
f= date(int(list_f[0]),int(list_f[1]),int(list_f[2]))
diff= f-i
print(diff.days) """
#ex15: volume of spere
""" 
from math import pi
r=6
volume = 4.0/3.0 * pi*r**3
print(volume) """

 #ex16: Ans :number -17, if number is greater than 17 then return double the absolute value
"""
num= int(input ('Write a number= '))

if num <=17:
    print(2*abs(num-17))
    
else:
    print(num-17) """

#ex17: to chck if a number is in the range of 100 from 1000 or 2000
""" 
num = int(input('write a number to be checked = v'))

if abs(1000-num)<=100 or abs(2000-num)<=100:
    print("True")
else:
    print('False') """

#18:sum of three numbers if same then twrice the awnser 
#we know how to  do it 

#19:in a str if "is" is already there then return the same string if not then return the string with is attached 
#eg: if str= "array " op:isarray
#    if str="isempty" op:isempty
""" def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty")) """

#20: to get a str which is n copies of given string 
""" string= str(input('whrite the string to be repeated = '))
n= int(input('put in the number of time the string has to be repeated : '))
for  i in range(n):
    print(string) """

#or or or or or or or or or or or or or or or or or or or or or or or or or or or or or or or or or or   

""" def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3)) """


#21 accept a number and state whether its even or odd 

""" num = int(input('give a number= '))

if num % 2 == 0:
    print('the number is even ')
else:
    print('number is odd') """


#22 to count number 4 in a given list.
""" numbers= input('write a set of numbers with commas : ')
list_numbers = numbers.split(',')
print('list of numbers is =' + str(list_numbers))
i=0
counter= 0
for e_numbers in list_numbers:
    print(e_numbers)
    if int(e_numbers) == 4:
        counter += 1
        print('present counter value is '+ str(counter))
print("number of 4's in the list are = " + str(counter))
 """
  
#23 string first two characters n copies 
""" string= input('write the string =')
copies= int(input("number of copies to be created ="))
def get_copies(given_string,n):
    New_string=""
    for i in range(n):
        New_string += given_string
    return New_string


if len(string)<=2:
    print(get_copies(string,copies))
    
else:
    string_new= string[0] +string[1]
    print(get_copies(string_new,copies)) """

#24: check if the passeds letter is vowel or not: 
""" letter= input("input a letter to check = ")
print (letter)
if letter =='a' or letter =='e' or letter =='i' or letter =='o' or letter =='u':
    print(" a vowel")
else:
    print("consonant") """

#better solution **********************************************

""" def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e')) """


#25: to find a number in the list :
""" data= input("input the list= ")
num= input("Number to be found? ")
list_data= data.split(",")
def find_the_number(data_in, number):
    return number in data_in

print(find_the_number(list_data, num)) """

#26: create a histogram:********************************************************
""" data_n= input("put in the data names= ")
data= input("put in the data= ")
assert len(data_n)==len(data)
list_data_n=data_n.split(",")
list_data=data.split(",")

def histogram(names,data):
    output= ""
    j=0
    for i in names:
        output+= "\n"+ i + "="
        
        stars= int(data[j])
        if j<= len(data):
            for n in range(stars):
                output +="@"
            j += 1   
    return output       

print(histogram(list_data_n , list_data)) """

#27: concatinate all the elements in the list ********************************************

""" def concatinate(list_1):
    final_string=""
    for i in range(len(list_1)):
        final_string += list_1[i]
    return final_string

list_strings= input("give list of strings= ")
final_list= list_strings.split(',')

print(concatinate(final_list)) """

#28:to print all even numbers from a given list in the same order and stop if any number is greater than 237
""" def print_even_numbers(list):
    even_no_list=[]
    for i in range(len(list)):
        if list[i] % 2==0 and list[i] != 237:
            even_no_list.append(list[i])
        elif list[i] == 237:
            break
    
    return even_no_list

print (print_even_numbers([    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ])) """

#29: print a set containing all the colors from color_list1 which are not in list 2 
""" def segregate_colors(color_list_1,color_list_2):
    color=[]
    i=0
    j=0
    for i in range(len(color_list_1)):
        if color_list_1[i] in  color_list_2:
            pass
        else:
            color.append(color_list_1[i])
            
    return color

print (segregate_colors(["green","blue","red","yellow"],["blue","yellow"])) """

#simple solution ********************************************************************************

""" color_list_1 = set(["White", "Black", "Red"])  #set is a collection which is unordered and unindexed and doesnt allow repetition
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2)) """


#30 area of triangle***********************************************************************8
#simple we know how to do it 
""" b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area) """

 
#31 gcd of two positive integers ************************************************************
""" def gcd(x,y):
    gcd=1
    if x % y==0:
        return x if x < y else y
    for k in range(int(y/2),0,-1):
        if x % k==0 and y % k==0:
            gcd= k
            break
    return gcd
print (gcd(6,4)) """

#32: lcm**********************************************************************

""" def lcm(x,y):
    z= x if x>y else y

    while True:
        if z % x==0 and z % y==0:
            lcm=z
            break
        z+=1
    return z

print(lcm(4,6))
print(lcm(15,17)) """

#33: sum of 3 integers but 0 is two values are equal then sum is zero 

""" def sum(x,y,z):
    summ=0 
    if x==y or y==z or z==x:
        summ=0
    else:
        summ=x+y+z
    return summ
print(sum(2,4,2))
 """
#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
""" def sum(x,y):
    z=x+y
    summ=0
    if z<=20 and z>15:
        summ=20
    else:
        summ=x+y
    return summ
print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12)) """
#35Write a Python program to add two objects if both objects are an integer type.
""" def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20)) """

#36:formatted display of information:
""" def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address)) 

personal_details()"""

#37for writing equations:
""" x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result)) """

#38rounding off nummbers 
""" amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2)) """

#39 euclidian distance
""" import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance) """

#40 to check wheter file exist 
""" import os.path
open('abc.txt','w') #creates a file
print(os.path.isfile('D:\projects\practise\sample.jpg'))# checks for a file """

#41: to chcek the bit of os
""" import struct
print(struct.calcsize("P") * 8) """

#42:os name platform ND RELEASE
""" import platform
import os
print(os.name)
print(platform.system())
print(platform.release()) """

#43:python site packages
""" import site; 
print(site.getsitepackages()) """

#44:to call external command in python 
""" import os
print(os.system('ls -l')) """

#45:path and name of the file currently executing 
""" import os 
print("the name and path of this file is =",os.path.realpath(__file__))"""

#46 number of CPU
""" import multiprocessing
print(multiprocessing.cpu_count()) """

#47 string to int or float
""" n="5.6739"
print(float(n))
print(int(float(n))) """

#48 to list all the files in a directory
""" from os import listdir
from os.path import isfile,join
file_list=[]
for f in listdir('D:\DEEP LEARNING CODES\practise'):
    print("file in the dir is = " + str(f))
    if isfile(join('D:\DEEP LEARNING CODES\practise',f)):
        file_list.append(f)
print(file_list) """


#49:DETERMINE PROFILING(how long various parts of the program took to execute) OF PYTHON PROGRAM
""" import cProfile
def sum():
    print(1+2)
cProfile.run('sum()') """

#50 print to stderr
""" import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")  """



#51 to get a current username
""" import getpass
print(getpass.getuser()) """

#52 get the local ip address using pythons stdlib
""" import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0]) """
  
#53: to get height and width of console
""" def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size()) """

#54: get excecution time
""" import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n)) """


#55 first n positive integers sum
""" n= int(input("sum of how many integers ="))

def sum_n(num):
    i=0
    count=0
    print("num is " + str(num+2))
    for i in range(num+1):
        print("i is " + str(i) + "num is " +str(num))
        count = count + i
        print("count is " + str(count))
    return count

print(sum_n(n))
 """

#56: hights to cms 
""" print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm) """

#57: to add a path get absolute file path:
""" def get_path(file_name_1):
    import os  
    return os.path.abspath(file_name_1)
print("Absolute file path: "+ str(get_path("IELTS.pdf"))) """

#58  to calculate sum of digits in an integer 
""" n = input("enter a integer")

if len(n)==1:
    print(n)
else:
    n_add=0
    for i in range(len(n)):
        n_add+= int(n[i])
    print(n_add) """

#59 sort 3 int without conditional statemnet:
""" x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3) """

#60 sort files by date 
""" import os
from os import listdir
import glob

for f in glob.glob('D:\DEEP LEARNING CODES\practise'):
    print(f)
    f.sort(key=os.path.getmtime)
print("\n".join(f)) """

# importing numpy as np
""" import numpy as np

# declare matrix with np
gfg = np.array([[6, 9], [8, 5], [18, 21]])

# using array.flatten() method
print(gfg.flatten())
 """

#finding the smallest number in a list BFS
""" take = input("input a list of numbers : ") 
list_of_numbers= take.split(",")

x=1000000000
for i in range(len(list_of_numbers)):
    if int(list_of_numbers[i]) < x:
        x= int(list_of_numbers[i])

print("the smallest no is : " + str(x)) """


#********************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************
#***************************************************** S E A R C H   &   S O R T ********************************************************************************************************
#********************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************


#BINARY SEARCH (given a ascending order list)

""" take= input("list of numbers = ")
find= int(input("number to be foud = "))

list_1= take.split(",")

not_found = True
lower= 0
higher= int(len(list_1)-1)
middle= int((lower + higher) / 2)

while not_found:
    middle= int((lower + higher) / 2)
    
    if find < int(list_1[middle]):
        higher= middle-1
        print("stuck in first loop")

    elif find > int(list_1[middle]):
        lower=  middle + 1
        print("stuck in second loop")
    
    elif (higher == lower and higher == middle) or (find == int(list_1[middle])):
        not_found= False
        print(" number  found = " + str(list_1[higher])+ " in "+ str(higher)+"position" )

    else:
        not_found= False
        print("numbernot found") """
    
#oroorrooororororororororororoororororororoororororororroorroorororoororororoorororororororooorororo
""" def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5)) """



#SEQUENTIAL SEARCH

""" take= input("list of numbers = ")
find= int(input("number to be found = "))

list_final= take.split(",")
found= False
for i in range(len(list_final)):

    if find == int(list_final[i]):
        print("number found, position is "+ str(i))
        found=True
        break 
if not found:
    print("number not found in the list ")  """
        

#BUBBLE SORT

""" take= input("list to be sorted: ")
list_1= take.split(",")

swap= True


def check_for_list(list):
    count=0
    for i in range(len(list)-1):
        if int(list[i])<int(list[i+1]):
            count += 1  

    if count == (len(list)-1):
        return True
    else:
        return False
             

while swap:

    for i in range(len(list_1)-1):
        if int(list_1[i]) > int(list_1[i+1]):
            sp= list_1[i+1]
            list_1[i+1] = list_1[i]
            list_1[i] = sp
            
                    
    if check_for_list(list_1):
        swap=False
        break

print(list_1) """

#oroorrooororororororororororoororororororoororororororroorroorororoororororoorororororororooorororo
#oroorrooororororororororororoororororororoororororororroorroorororoororororoorororororororooorororo

""" def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):                   #******************************
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)
 """

 #SELECTION SORT 
#  for min number swapping
""" take= input("list of number to be sorted = ")
list_final= take.split(",")

for j in range(len(list_final)):

    for k in range(j,len(list_final)):
        
        counter = 0

        for l in range(j,len(list_final)):
            if int(list_final[k]) <= int(list_final[l]): 
                counter += 1

        if counter == (len(list_final)-j):
            temp = list_final[j]
            list_final[j]=list_final[k]
            list_final[k]= temp
            

print("sorted list=" + str(list_final)) """

#for max number swapping 
""" def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist) """


# INSERTION METHOD 

""" take = input("enter a list of numbers :")
list= take.split(",")

def insertionSort(nlist):
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue


insertionSort(list)
print(list)
 """
# T H R E A D I N G


""" import threading
import random
import time

fingers= 0
list_1= []

def print_now():
    global fingers 
    global list_1
    while True:
        list_1.append(fingers)
        print("audio to be played= " + str(list_1) )
        time.sleep(5)

def True_1():
    global fingers
    global list_1

    while True:
        fingers= random.randint(0,5)
        print("finger chosen = " + str(fingers))
        time.sleep(1)
        
thread1 = threading.Thread(target=print_now)
thread1.start()

thread2 = threading.Thread(target=True_1)
thread2.start() """

#Write a Python program to import built-in array module and display the namespace of the said module.
""" import array 

for name in array.__dict__:
    print(name) """


#Write a Python program to create a class and display the namespace of the said class

""" class Anant:
    def __init__(self):
        self.x=0

    def __format__(self, format_spec: str) -> str:
        pass 

for name in Anant.__dict__:
    print(name) """

#Write a Python program to create an instance of a specified class and display the namespace of the said instance

""" class Hand_signs:
    def __init__(self,animal_name,number_of_limbs,number_of_eyes):
        self.animal_name= animal_name
        self.number_of_limbs= number_of_limbs
        self.number_of_eyes= number_of_eyes

animal = Hand_signs("cow",4,2)

print(animal.__dict__)
for name in animal.__dict__:
    print(name) """

#Write a python program which import the abs() function using the builtins module, display the documentation of abs() function and find the absolute value of -155

""" import builtins
help(builtins.print)
print(builtins.abs(-155)) """

#Define a Python function student(). Using function attributes display the names of all arguments.

""" def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
print(student('S122', 'Wilson Medina', 'VI')) """

#Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.

""" def student_data(student_id, **kwargs):
    print (f"student_id: {'student_id'} ")

    if  'student_name' in kwargs:
        print(f"student_name = $ {kwargs['student_name']}")

    if "student_name" and "student_calss " in kwargs:
        print(f"student name:  {kwargs['student_name']} \n student class: {kwargs['student_name']} ")

student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V') """

#Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.

""" class Student:
    pass  
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__) """

#Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
""" class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()

print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))  """


# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
""" class Student:
    student_name = 'Terrance Morales'
    marks = 93  
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Angel Brooks')
setattr(Student, 'marks', 95) 
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}") """

#Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their values of the said class. Now remove the student_name attribute and display the entire attribute with values.
""" class Student:
    student_id = 'V10'
    student_name = 'Jacqueline Barnett'  

print("Original attributes and their values of the Student class:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print("\nAfter adding the student_class, attributes and their values with the said class:")
Student.student_class  = 'V'
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print("\nAfter removing the student_name, attributes and their values from the said class:")
del Student.student_name
#delattr(Student, 'student_name')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
 """
# Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given format.
""" class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS' 
student1 = Student()
student2 = Student() 
student1.student_id = "V12"
student1.student_name = "Ernesto Mendez"
student2.student_id = "V12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
 """

#Write a Python class to convert an integer to a roman numeral.

""" class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))

 """
#Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

""" class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()")) """


#Write a Python program to get all possible unique subsets from a set of distinct integers.

""" class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))
 """

""" import cv2

cap= cv2.VideoCapture(0)

while True:
    _,frame= cap.read()

    cv2.imshow("frame",frame)

    key= cv2.waitKey(50)
    if key== 27:
        break
cap.release()
cv2.destroyAllWindows() """

#MERGE SORT
""" import numpy as np


arr=input("give the numbers in the array ")

print(arr)

array= arr.split(",")

print(array)
l=int(input("l= "))
m=int(input("m= "))
r= int(input("r= "))

def merge(list_array,l,m,r):
    first_array=[]
    second_array=[] 
    final_list_1=[]
    final_list_2=[]
    
    for i in range(l): 
        print("list_array "+str(i)+" "+ str(list_array[i]))
        first_array.append(int(list_array[i]))
        
    first_array.sort()
    print( first_array)

    for i in range(m,r): 
        print("list_array "+str(i)+" "+ str(list_array[i]))
        second_array.append(int(list_array[i]))
        
    second_array.sort()
    print(second_array)

    concatinate(first_array,second_array)

def concatinate(lst1,lst2):
    lst1.extend(lst2)
    print(lst1)

merge(array,l,m,r) """

