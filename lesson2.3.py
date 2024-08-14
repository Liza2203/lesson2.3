my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index=0
while index<len(my_list):
    a=my_list[index]
    index+=1
    if a>0 and a!=0:
        print(a)
    elif a<0:
        break


