
for i in range(1000):
    if(i/10>=10):
        password=i
    elif(i/10>=1):
        password='0'+str(i)
    else:
        password='00'+str(i)
    print(password)

