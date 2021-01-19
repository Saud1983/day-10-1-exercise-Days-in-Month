def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year.")
        return True
      else:
        # print("Not leap year.")
        return False
    else:
      # print("Leap year.")
      return True
  else:
    # print("Not leap year.")
    return False

def days_in_month(the_year, the_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if month == 2:
    result=is_leap(the_year) # result can be ommitted and use the function directly
    if result == True: # or if is_leap(the_year):
      return 29
    else:
      return month_days[1]
  else:
    return month_days[the_month-1]

  # another way to do this
  # if is_leap(the_year) and the_month == 2:
  #   return 29
  # return month_days[the_month-1]


  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)