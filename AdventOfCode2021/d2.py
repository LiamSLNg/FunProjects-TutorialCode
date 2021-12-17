with open("d2.txt") as fin: 
    data = [i for i in fin.read().strip().split("\n")]

def part1():
    for_pos = 0
    vert_pos = 0
    for instr in data:
        command = instr[0]
        var = int(instr[-1])
        if command == "f":
            for_pos += var
        elif command == "d":
            vert_pos += var
        elif command == "u":
            vert_pos -= var
    return for_pos * vert_pos

def part2():
    for_pos = 0
    vert_pos = 0
    aim_pos = 0
    for instr in data:
        command = instr[0]
        var = int(instr[-1])
        if command == "f":
            for_pos += var
            vert_pos += aim_pos * var
        elif command == "d":
            aim_pos += var
        elif command == "u":
            aim_pos -= var
            
    return for_pos * vert_pos

print(part2())