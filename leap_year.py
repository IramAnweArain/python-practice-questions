'''An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
Given a year, determine whether it is a leap year.'''
def is_leap(year):
    leap = False
    if(year%4 == 0 and year%100 != 0) or (year%400 ==0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))