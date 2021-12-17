with open("d3.txt") as fin: 
    data = [i for i in fin.read().strip().split("\n")]

gam = ""

for i in range(len(data[0])):
    s = 0
    for arr in data:
        s += int(arr[i])
    gam += "1" if s > len(data) / 2 else "0"

eps = ""

for i in gam:
    eps += "1" if i == "0" else "0"

gam_ra = int(gam, 2)
eps_ra = int(eps, 2)

power = gam_ra * eps_ra
print(power)