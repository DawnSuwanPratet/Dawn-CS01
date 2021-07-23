A = int(input("Enter your score: "))

if A >= 0 and A <= 10:
    print("ไม่ผ่าน")
elif A >= 11 and A <= 20:
    print("ปรับปรุง")
elif A >= 21 and A <= 30:
    print("ดีมาก")
else:
    print("Error")