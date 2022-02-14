#q1
def f(str):
    str = str.split()                                                                 
    str2 = []                                                                         
    for i in str:
        if i not in str2:
            str2.append(i)                                                            
    for i in range(0,len(str2)):
        print("frequency of", str2[i], "is", str.count(str2[i]))                  


string = input("Enter ur string\n")                                                  
length = len(string.split())                                                        
if length>1:
    f(string)                                                                    
else:
    fre = {i: string.count(i) for i in set(string)}                             
    print("count of all characters in ur string is :\n ", str(fre))

#q2
i=0
while i<1:
    date = int(input("Enter date: (1-31)\n"))
    month = int(input("Enter month: (1-12)\n"))
    year = int(input("Enter year: (1800-2025)\n"))
    print("input date is", date, "/", month, "/", year)

    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and date == 31 and (year<=2025 and year>=1800):
        print("next date is", 1, "/", month+1, "/", year)
        break

    elif month == 12 and date == 31 and (year<=2025 and year>=1800):
        print("next date is", 1, "/", 1, "/", year+1)
        break

    elif (month == 4 or month == 6 or month == 9 or month == 11) and date == 30 and (year<=2025 and year>=1800):
        print("next date is", 1, "/", month+1, "/", year)
        break

    elif month == 2 and date == 28 and year%4 != 0 and (year<=2025 and year>=1800):
        print("next date is", 1, "/", 3, "/", year)
        break

    elif month == 2 and date == 29 and year%4 == 0 and (year<=2025 and year>=1800):
        print("next date is", 1, "/", 3, "/", year)
        break

    elif month == 2 and date > 29 and year%4 == 0 and (year<=2025 and year>=1800):
        print("given wrong input")
        continue

    elif month == 2 and date > 28 and year%4 != 0 and (year<=2025 and year>=1800):
        print("given wrong input")
        continue

    elif (month<=12 and month>=1) and (year<=2025 and year>=1800) and (date>=1 and date<=31):
        print("next date is", date+1, "/", month, "/", year)
        break

    else:
        print("given wrong input")
        continue


#q3
list1 = []      #create an empty list
n = 0
while n<1:
    choice = input("Type 'y' to enter number / Type 'n' to cancel\n") #now ask if user wants to enter the number or not
    if choice == 'n' or choice == 'N':
        break

    elif choice == 'y' or choice == 'Y':
        num = int(input("Enter the number\n"))
        list1.append(num)          #add the number to list1
        continue

    else:
        print("given wrong input, try again")
        continue

print("Numbers entered are :", list1)
list2 = [(i, i*i) for i in list1]        
print("Given number, square of given number :", list2)


#q4
grade = int(input("Please enter the grade (4-10)\n"))
if grade == 10:
    print("Your Grade is ‘A+’ and Outstanding Performance.\n")
elif grade == 9:
    print("Your Grade is ‘A’ and Excellent Performance.\n")
elif grade == 8:
    print("Your Grade is ‘B+’ and Very Good Performance.\n")
elif grade == 7:
    print("Your Grade is ‘B’ and Good Performance.\n")
elif grade == 6:
    print("Your Grade is ‘C+’ and Average Performance.\n")
elif grade == 5:
    print("Your Grade is ‘C’ and Below Average Performance.\n")
elif grade == 4:
    print("Your Grade is ‘D’ and Poor Performance.\n")
else:
    print("Error, grade is out of range, please enter grade between 4 to 10\n")

#q5
k=6
for i in range(0,k):
    for j in range(0,i):
        print(' ', end='')
    for j in range(0, 2*(k-i)-1):
        print(chr(65+j), end='')
    print()

#q6
dict1 = {}
i = 0
while i < 1:
    choice = input("Type 'y' to enter Name and SID / Type 'n' to cancel\n")
    if choice == 'n' or choice == 'N':
        break

    elif choice == 'y' or choice == 'Y':
        sid = input("Enter the SID\n")
        name = input("Enter the Name\n")
        dict1.update({sid: name})
        continue

    else:
        print("given wrong input, try again")
        continue

print(dict1)
sortkey = {k: v for k, v in sorted(dict1.items())}
sortval = {k: v for k, v in sorted(dict1.items(), key=lambda v: v[1])}

print("Dictionary after sorting it by key is :", sortkey)
print("Dictionary after sorting it by value is :", sortval)

findst = input("Enter the student's SID which you want to find\n")
print("Name of the student whose SID is", findst, "is", dict1.get(findst))


#q7
def fibonacci(n):         #in fibonacci sequence, each term is the sum of its previous two terms
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

terms = int(input("Enter the number of terms you want to print in the fibonacci sequence\n"))
list1 = []        

if terms <= 0:        
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       list1.append(fibonacci(i))

print(list1)
average = sum(list1)/terms
print("The average of fibonacci sequence upto",terms, " terms is", average)


#q8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print("part a:")
print("Set of all elements that are in Set1 and Set2 but not in both is", set1.union(set2).difference(set1.intersection(set2)))
universal = set1.union(set2.union(set3))
set1_inter_set2 = set1.intersection(set2)
set2_inter_set3 = set2.intersection(set3)
set1_inter_set3 = set1.intersection(set3)
one_of_3_sets = universal.difference(set1_inter_set2).difference(set2_inter_set3).difference(set1_inter_set3)
print("part b:")
print("Set of all elements that are in only one of the three sets Set1, Set2 and Set3 is", one_of_3_sets)
two_of_3_sets = universal.difference(one_of_3_sets)
print("part c:")
print("Set of elements that are exactly two of the sets Set1, Set2 and Set3 is", two_of_3_sets)
set4 = {1,2,3,4,5,6,7,8,9,10}
not_in_set1 = set4.difference(set1)
print("part d:")
print("Set of all integers in the range 1 to 10 that are not in Set1 is", not_in_set1)
not_in_universal = set4.difference(universal)
print("part e:")
print("set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 is", not_in_universal)

