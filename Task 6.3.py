# Task 6.3

average = 0
sum_nums = 0 
while sum_nums < 10:
    sum_nums = sum_nums + 1 
    total = int(input(f"Enter number {sum_nums}:"))
    average = average + total
average = average / sum_nums
print(average)
