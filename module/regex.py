import re

# challenge 1
while True:
    dob = input("生年月日を入力してください(yyyy/mm/dd)")
    result = re.search("", dob)
    if result:
        print(f"{dob}は正しいフォーマットです")
        break
    else:
        print(f"{dob}は正しくないフォーマットです")
    