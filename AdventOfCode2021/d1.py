count = 0
array = []
with open("d1.txt") as fp:
    while True:
        count += 1
        line = fp.readline()
 
        if not line:
            break
        array.append(int(line))

print(array[0:5])

sum = 0
prev_sum = array[0] + array[1] + array[2]
curr_sum = 0

for i in range (3, len(array)):
    curr_sum = array[i] + array[i-1] + array[i-2]
    if prev_sum < curr_sum:
        sum +=1
    prev_sum = curr_sum
print(sum)