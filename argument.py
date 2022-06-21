#1#Write a function that takes one argument as a list a=[2,4,6,8] and remove the second 
#last item from that list and returns the whole list without the removed item
def remove_item(list):
    list.remove(list[-2])
    return list
a = [2,4,6,8]
print(remove_item(list=a))


#Write a python program that has a list days = ["Monday","Tuesday","Friday","Monday"] and
#counts the number occurrences of Monday
def week_days():
    days = ["Monday","Tuesday","Friday","Monday"]
print(week_days.count("Mondays"))
    


# #3#Write a python function named smallest that accepts a list of unsorted integers and returns
# #the smallest number in the list.Example:smallest([3,6,8,2,4,1,5,7]) returns 1
smallest = [3,6,8,2,4,1,0,5,7]
print(min(smallest))


# #4#Write a function named divisible_by_seven that;using the range function and a for loop
# #returns a list containing all the numbers between 100 and 200 that are divisible by 7
def divisible():
     for i in range(100,200):
        if i%7==0:              
            print(i)
divisible()

#5#Write a python program that takes two inputs(as int) from a user and adds
#the 2 numbers,checks if the sum is greater than 10,less than 10 or equal 10
#and prints a statement after each check
num1 = int(input("enter number to calculate: "))
num2 = int(input("enter number to calculate: "))
sum = num1 + num2
if sum >10:
    print("sum is greater than 10")
elif sum <10:
    print("sum is less than 10")
else:
    print("sum is equal to 10")
    
#6#Write a function that takes one argument which is a list a=[1,2,3,4,5] and
#returns True if 4 is present in the list and False if 4 is not in the list
a=[1,4,2,3,5]
a = a.count(4)
if a>0:
      print(f"{True} 4 is present in the list")
elif a<4:
     print(f"{False} 4 is not present in the list")
    
    


#7#Write a function that takes one argument which is a list
# fruits=["apples","grapes","pineapple"]and removes the last fruit from the list
#then returns the list without the removed fruit
fruits=["apples","grapes","pineapple"]
print(fruits.pop())
print(fruits)

#8#Write a python program that takes in a list of cars,cars=["Ford","BMW","vOLVO"]
#and returns a sorted list
def cars_number():
    car=["Ford","BMW","VOLVO"]
    car.sort()
    print(car)
cars_number()


 