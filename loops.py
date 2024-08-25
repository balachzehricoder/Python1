fact = 1
i= 1
num = int(input("Enter a number: "))
while i <= num:
  fact = fact * i
  i = i + 1
  print("factoorial of", num, "is", fact, "")



start_year = int(input("start year"))
end_year = int(input("end year"))

for year in range(start_year, end_year + 1):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(year)
