import datetime

now = datetime.datetime.now()

print(type(now))
# print(now)

if 4 <= now.hour < 12:
    print("굿모닝")

elif 12 <= now.hour < 18:
    print("굿애프터눈")
    
elif 18 <= now.hour < 22:
    print("굿이브닝")
else:
    print("굿나잇")