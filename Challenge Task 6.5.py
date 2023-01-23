# Challenge Task 6.5

average = 0
sum_nums = 0
finish = True
sum = 0
while finish == True:
    sum_nums = sum_nums + 1 
    total = int(input(f"Enter number {sum_nums}:"))
    if (total == -1):
        finish = False
    else:
        sum_nums += average
        sum += total
average = sum / sum_nums
print(average)
