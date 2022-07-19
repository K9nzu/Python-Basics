# كود طباعة كلمه
# print ('Hi')
# print ("Oh\nHello")
# print ('good\'thanks')
# print ('oh\toh')

# العمليات الحسابية 
# print (7+7)
# print (10-6)
# print (4*4)
# print (30/2)
# print (20%3)
# print (4 < 3)
# print (10 >= 10)
# print (30 == 40)
# print (40 != 50)
# print ('n' > 'o')
# print (pow(3,3))
# print (max(5,12))
# print (min(3,15))
# print (round(5.8))
# from math import *
# print (floor(4.7))
# print (ceil(4.7))
# print (sqrt(9))

# كود المتغيرات
# a = 5
# c = -2
# b = 2
# print (a+b)
# print (str(a)+' Nice Number')
# print (abs(c))
# m = 5
# m += 2
# print (m) or (m + 2)
# title = 'Welcome'
# print (title+' to my house')
# title2 = 'HELLO'
# print (title2.lower()) or (title2.lower().islower())
# print (title.upper()) or (title.upper().isupper())
# print (title.isupper()) or (title.islower())
# print (len(title))
# print (title[0])
# print (title,title2)
# print (title.index('l'))
# print (title.replace('Wel', 'don\'t '))

# my = 'Project'
# mylist = list (my)
# print (mylist) or (my[3]) or (my)


# lol = my + ' ' + 'Ammar'
# print (lol)

# *علامة التنصيص للارقام اختياريه لكن بعض الاكواد تكون مضره

# date = '{}/{}/{}' .format (7 , 2022 , 'jwan')
# print (date)

# k = 'from {0} to {4}' .format ('earth' , 'mre6' , 'zahra' , 'mshtre' , 'moon')
# print (k)

# car = '{d:} vehicle speed' .format (100)
# print (car)

# القوائم
# list = ['hi','how','bad','are','you','bad']
# list.append ('Good')
# list.insert (1 , 'hello')
# list.remove ('bad')
# list.reverse ()
# print (list) 
# print (list.count ('bad'))

# numbers = [10,6,8,7,9,4,3,5,2,1,0,'Night','Evening']
# numbers.sort ()
# print (numbers)
# print (2 in numbers)
# print (4 not in numbers)
# print ('Night' is 'Evening')
# print ('Night' is not 'Evening')

# الثوائم الثابتة (Tuples)
# Tuples = (32, 23) # لا تتغير ابدا القائمة
# list_of_tuples = [(18,17), (34,26), (68,56)] # و ممكن ان تصبح قوائم ايضا
# Tuples[1] = 46 # مثال الكود لما اضفته لا يغير اي شيئ لانها قائمة ثابته تستخدم كمثال على الاحداثيات
# print (Tuples[1])

# الفهرس
# amunt = {'ahmed': 6 , 'noor': 10 , 'farah': 12}
# amunt ['mohamad'] = 15
# del amunt ['noor']
# print (amunt.keys())
# print (list (amunt.keys()))
# print (amunt) or (amunt ['farah'])
# print ('ammar' in amunt)

# القواميس (Dictionaries)
# month = {
#     'jan' : "January",
#     'feb' : "Febraury",
#     'mar' : "March"
# }
# print (month.get('april'))
# print (month['jan'])
# print (month.get('ahmed', 'is not month'))

# عمليات العلاقات و العمليات الشرطية
# print (False and False)
# print (True and True)
# print (True and False)
# print (False and True)
# print (True or True)
# print (False or False)
# print (True or False)
# print (False or True)

# print (not (5 > 7) and (3 == 3)) or False

# الجمل الشرطية (Conditionals)
# age = 15
# if age < 18:
#     print ('Sorry You can not Register You must be 18')

# Age = 19
# if Age < 18:
#    print ('Sorry You can not Register You must be 18')
# else:
#    print ('Welcome to website')

# print ('Sorry You can not Register You must be 18' if 15 < 18 else "Welcome to website") # هذا الكود اختصار لي الجمل الشرطية

# is_hungry = True

# if is_hungry:
#     print ("you are hungry")

# else:
#     print('you are not hungry')

# is_hungry = True
# hungry = False

# if is_hungry and hungry:
#     print ("you are hungry")

# else:
#     print('you are not hungry')

# if is_hungry or hungry:
#     print ("you are hungry")

# else:
#     print('you are not hungry')

# is_hungry = True
# hungry = False

# if is_hungry and hungry:
#     print ("you are hungry")

# elif is_hungry and not hungry:
#     print ("but you must to eat")

# else:
#     print('you are not hungry')

# المقارنات (Comparisons)

# def max_num(num1,num2,num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1

#     elif num2 >= num1 and num2 >= num3:
#         return num2
    
#     else:
#         return num3

# print (max_num(4, 8, 6))

# print (max(10,20,500))

# def string(str1, str2):
#     if str1 != str2:
#         print("is string do match")
#     else:
#         print('is string dont match')

# string('ammar', 'ahmed')

# def string(str1, str2):
#     if str1 == str2:
#         print("is string do match")
#     else:
#         print('is string dont match')

# string('ammar', 'ahmed')

# جمل الدوران
# while age < 18:
#     print ('Sorry You can not Register your age is')
#     print (age)
#     age += 1
# or 
# while age < 18:
#     print ('Sorry You can not Register your age is ' + str (age))
#     age += 1
    
# ages = [22 , 23 , 5 , 8 , 15 , 18 , 13]
# for age in ages:
#     print (age)
    
# for index , age in enumerate(ages):
#     print (index)
#     print (age)


# i = 1

# while i <= 10:
#     print (i)
#     i += 1
# else:
#     print ('the condition not true')

# print('The Loop Has Ended')

# while i <= 10:
#     i += 1
#     if i == 6:
#         continue or break
#     print (i)

# for char in 'Ahmed':
#     print (char)

# letter = ['mohamad', 'moyad', 'samer', 'loser']
# user = 'noor'

# print(len('Ammar'))
# for Let in letter:
#     print(Let)

# for x in range(10):
#     print(x)

# for x in range(5,15):
#    print(x)

# for x in range(len(letter)):
#    print(letter[x])

# for i in range(10):
#     if i % 2 ==0:
#         print (i,' is an even number')
#     else:
#         print(i,' is an odd number')

# for i in range(len(letter)):
#     if letter[i] == 'loser':
#         print (i,' this loser')
#     else:
#         print(i,' this not loser')

# letter = ['mohamad', 'moyad', 'samer', 'loser']

# for let in letter :
#     if let == 'samer':
#         print (let,' is your friend')
#         break
#     else:
#         print(let,' is not your friend')

# for x in range(2, 10):
#     if x == 7:
#         continue
#     print (x, 'is the chosen number')

#الدوال (Functions)
# def how_y():
#     print('good thx')

# print('nice')
# how_y()
# print('finy')

# def say_hi(name):
#     print('Hi ' + name)

# say_hi('Ammar')

# def say_hi(name, age):
#     print('Hi ' + name +'Your age is '+ age)

# say_hi('Ammar ','18')

# def say_hi(name, age):
#     print('Hi ' + name +'Your age is '+str(age))

# say_hi('Ammar ', 18)

# def cube(num):
#     return num*num*num

# result = cube(5)

# print (result)

# def calc(num1, num2):
#     return num1+num2

# print (calc(5, 5))

# دالة الأس (Power)
# def power(base_num, power_num):
#     result = 1
#     for index in range (power_num):
#         result = result * base_num
#     return result
# print (power(2,3))

# قوائم ثنائية الابعاد (2D Lists & Nested Loops)
# no_list = [
#     [1,9,6],
#     [8,5,2],
#     [4,3,7],
#     [0]
# ]

# print(no_list[2][1])

# no_list = [
#     [1,9,6],
#     [8,5,2],
#     [4,3,7],
#     [0]
# ]

# for lob in no_list:
#     print(lob)

# no_list = [
#     [1,9,6],
#     [8,5,2],
#     [4,3,7],
#     [0]
# ]

# for lob in no_list:
#     for no in lob:
#         print(no)

# الاخطاء (Errors)
# try:
#     value = int(input('Enter a number: '))
#     print (value)
#     division = 10 / 0
# except ValueError:
#     print ('try again and input a number')
# except ZeroDivisionError:
#     print('invalid input')

# print('success')

# try:
#     value = int(input('Enter a number: '))
#     print (value)
#     division = 10 / 0
# except ValueError as err:
#     print (err)
# except ZeroDivisionError as err1:
#     print (err1)

# print('success')

# قراءة الملفات (Reading Files)
# open ('names and jobs.txt', 'r') 
# open ('names and jobs.txt', 'r+') 
# open ('names and jobs.txt', 'w') 
# open ('names and jobs.txt', 'w+') 
# open ('names and jobs.txt', 'a') 
# open ('names and jobs.txt', 'a+') 

'''
ملاحظة
                  | r   r+   w   w+   a   a+
------------------|--------------------------
read              | +   +        +        +
write             |     +    +   +    +   +
create            |          +   +    +   +
truncate          |          +   +
position at start | +   +    +   +
position at end   |                   +   +

'''

# التطبيق على امر r
# file = open ('names and jobs.txt', 'r') 
# print (file.readable())
# print (file.read())
# file.close()

# file = open ('names and jobs.txt', 'r') 
# print (file.readline())
# print (file.readline())
# file.close()

# file = open ('names and jobs.txt', 'r') 
# print (file.readlines())
# file.close()

# file = open ('names and jobs.txt', 'r') 
# print (file.readlines()[2])
# file.close()

# file = open ('names and jobs.txt', 'r') 
# for lines in file.readlines():
#     print (lines)
# file.close()

# file = open ('names and jobs.txt', 'r') 
# for lines in file.readlines():
#     print (lines)
# file.close()

# التطبيق على امر a
# file = open ('names and jobs.txt', 'a') 
# file.write('abdalah - foot ball player')
# file.close()

# file = open ('names and jobs.txt', 'a') 
# file.write('\nabdalah - foot ball player') #\n لاضافة سطر جديد و الكتابه فيه
# file.close()

# التطبيق على امر w
# file = open ('write', 'w') 
# list_of_ph = ['this is a first line', '\nthis is a second line', '\nthis is a third line']
# file.writelines(list_of_ph) 
# file.close()

# (*args)
# def sum_nums(x , y):
#     return x + y
    
# print(sum_nums(3 , 8))

# def sum_list(my_list):
#     result = 0
#     for g in my_list:
#         result += g
#     return result

# list_of_nums = [4, 2, 4, 2, 3]
# print(sum_list(list_of_nums))

# def nums(*args): # ملاحظة كلمة args ليست ضروري فقط هذه الكلمة المتعارف عليها المهم هو الرمز >*< هذا
#     result = 0
#     for s in args:
#         result += s
#     return result

# print (nums(6, 4))

# def my_sun(a, k ,*args, option=True):
#     result = 0
#     if option:
#         for x in args:
#             result += x
#         return a + k + result
#     else:
#         return result

# print (my_sun(3, 2, 4, 1, option=False))

# (**kwargs) # ملاحظة ال ** تستخدم فقط مع الدكشنري def
# def make_sent(**kwargs):
#     result = ''
#     for arg in kwargs.values():
#         result += arg
#     return result

# print (make_sent(a='ammar ', b='is ', x='developer'))

# def human_details(**kwargs):
#     for key, value in kwargs.items():
#         print (f'{key} : {value}')

# human_details(name='mohamad', job='developer', age='46')
# print('------------------')
# human_details(name='ammar', job='engineer', age='23')

# def wg(x, y, *args, option=True, **kwargs):
#     print(x, y)
#     print(args)
#     print(option)
#     print(kwargs)
#     print(kwargs.values())
#     print(kwargs.items())
    
# wg(1, 2, '3 is args', "4 is args", channel='Ammar')
# wg(1, 2, '3 is args', "4 is args", option=False, channel='Ammar', action='follow')

# (unpacking operators)
# klist = [3, 4, 2]
# print (*klist) # سوف يطبع لي القيم فقط من دون اقواس و نصوص

# def my_sum(x , y , z):
#     print (x + y + z)

# My_List = [5 , 2 , 3]
# my_sum(*My_List)

# def My_sum (*args):
#     result = 1
#     for m in args:
#         result += m
#     return result

# list1 = [1 , 2 , 3]
# list2 = [4 , 5 , 6]
# list3 = [7 , 8 , 9]

# print (My_sum(*list1 , *list2 , *list3))

# my_List = [5 , 8 , 4 , 9 , 2 , 6]
# a, *b, c = my_List

# print (a)
# print (b)
# print (c)

# my_first_list = [1,2,3]
# my_second_list = [4,5,6]
# my_merged_list = [*my_first_list,*my_second_list]
# print (my_merged_list)

# my_first_dict = {'A':1, 'B':2}
# my_second_dict = {'C':3, 'D':4}
# my_merged_dict = {**my_first_dict,**my_second_dict}
# print (my_merged_dict)

# list_of_char = ['Ammar', *'poison']
# print (list_of_char)

#                      و الحمد الله خلصنه الاساسيات :)
#                                 The End