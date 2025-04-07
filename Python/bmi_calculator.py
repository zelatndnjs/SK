weight = float(input())
height = float(input())
height /= 100
bmi = weight / (height ** 2)
print(f"체중(kg): {weight:.0f}")
print(f"키(cm): {height*100:.0f}")
print(f"BMI: {bmi:.1f}")