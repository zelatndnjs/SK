num = "901212-1234567"
year = 1900 + int(num[:2:])
month = int(num[2:4])
day = int(num[4:6])
print(f"{year}년 {month}월 {day}일")