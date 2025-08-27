def Record():
    f=open('record.txt','r')
    record=f.read().splitlines()
    for i in record:
        print(i)
