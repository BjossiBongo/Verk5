n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1,n+1):
    if i==1:
        first_num=1
        print(first_num)
    elif i==2:
        second_num=2
        print(second_num)
    elif i==3:
        third_num=3
        print(third_num)
    else:
        next_num=first_num+second_num+third_num
        first_num=second_num
        second_num=third_num
        third_num=next_num
        print(next_num)

