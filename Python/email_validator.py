import re

a = "user@example.com"
b = "user@example"
regex = r"@.*\."
print(f"이메일 주소: {a}")
if re.search(regex, a):
    print("유효함")
else:
    print("유효하지 않음")
print(f"이메일 주소: {b}")
if re.search(regex, b):
    print("유효함")
else:
    print("유효하지 않음")
