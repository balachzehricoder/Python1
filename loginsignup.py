name = input("enter your name")

email = input("enter your email")

password = input("enter your password")

lemail = input("enter your email")
lpass = input("enter your password")


if lemail == email and lpass == password:
  print("login successfull")
  studentname = input("enter your name")

  studentmarks = int(input("enter your marks"))

  if studentmarks >= 90:

    print("A+")


  elif studentmarks >= 80:

    print("A")




  elif studentmarks >= 70:

    print("B+")




  elif studentmarks >= 60:

    print("B")





  elif studentmarks >= 50:

    print("C+")



  elif studentmarks >= 40:

    print("C")





  elif studentmarks >= 30:

    print("D+")





  elif studentmarks >= 20:

    print("D")





  elif studentmarks >= 10:

    print("E+")





  elif studentmarks >= 0:
    print("E")





firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
oprator = input("Enter operator: ")

if oprator == '+' and firstnumber and secondnumber:
  print(firstnumber + secondnumber)
elif oprator == '-' and firstnumber and secondnumber:
  print(firstnumber - secondnumber)
elif oprator == '*' and firstnumber and secondnumber:
  print(firstnumber * secondnumber)
elif oprator == '/' and firstnumber and secondnumber:
  print(firstnumber / secondnumber)









else:
  print("login failed")