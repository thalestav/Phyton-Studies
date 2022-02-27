# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
check_a = year % 4
check_b = year % 100
check_c = year % 400

if check_a == 0:
  if check_b == 0:
    if check_c != 0:
      print("Not Leap")
    else:
      print("Leap")
  else:
    print("Leap")
else :
  print("Not Leap")



