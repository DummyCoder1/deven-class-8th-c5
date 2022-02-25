age = int(input('type your age'))
if age < 0:
    print('not a valid age')
elif age >= 12 and age< 20:
    print('you are teenager')
elif age==20 :
    print('you have just entered adulthood')
else:
    print('you are a economical group')
