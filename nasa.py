from typing import Literal, Tuple, List

#list of all assumed directions in this scenario
directions = ['N', 'E', 'S', 'W']

def left(x: int, y: int, dir: str) -> Tuple[int, int, str]:
    ind = directions.index(dir)
    dir = directions[(ind - 1) % 4]
    #print(f"{x} {y} {dir}")
    return x,y,dir

def right(x: int, y: int, dir: str) -> Tuple[int, int, str]:
    ind = directions.index(dir)
    dir = directions[(ind + 1) % 4]
    #print(f"{x} {y} {dir}")
    return x,y,dir

def move(x: int, y: int, dir: str) -> Tuple[int, int, str]:
    updated_x, updated_y =x, y
    if dir == 'N':
        updated_y += 1
    elif dir == 'E':
        updated_x += 1
    elif dir == 'S':
        updated_y -= 1
    else: #W
        updated_x -= 1

    #return updated position if the move is valid, else return the current position
    if 0 <= updated_x <= ur_coords_x and 0 <= updated_y <= ur_coords_y:
        return updated_x, updated_y, dir
    else:
        print(f"Oops! Out of bounds")
        return x, y, dir 
    
def validate_instructions(instructions: str) -> bool:
    for instruction in instructions:
        #handling case sensitivity while validating instructions
        if instruction not in 'LRMlrm':
            print(f"Invalid instruction string - Gotta start with this one from the top")
            return False
    return True

def validate_parts(parts: List[str]) -> bool:
    if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit() or parts[2].upper() not in directions:
        print(f"Invalid start position. Try Again...")
        return False
    
    parts[2] = parts[2].upper()

    x, y = int(parts[0]), int(parts[1])
    if not (0 <= x <= ur_coords_x and 0 <= y <= ur_coords_y):
        print(f"Out of bounds: ({x}, {y}). Try Again...")
        return False
    return True

def read_input() -> List[Tuple[Tuple[int, int, str], str]]:
    robots = []
    while True:
        try:
            position = input("Enter the robot's initial position (or press Enter to stop): ").strip()
            if not position:
                break

            #input position and validate
            parts = position.split()
            if not validate_parts(parts):
                continue

            #input instructions and validate
            instructions = input("Provide instructions: ").strip()
            if not validate_instructions(instructions):
                continue

            robots.append((parts, instructions.upper()))
            #print(robots)
        except:
            break
    return robots

def process_input(robots: List[Tuple[Tuple[int, int, str], str]]) -> None:
    for i,robot in enumerate(robots,1):
        ((x, y, dir), instructions) = robot
        print(f"Robot {i}:\nStart position = ({x}, {y}) {dir} with Instructions = {instructions}")
        for instruction in instructions:
            x, y, dir = map_instr[instruction](int(x), int(y), dir)
        print(f"Final position = ({x}, {y}) {dir}")  

#entry point
if __name__ == '__main__':
    print("Welcome to NASA!")
    try:
        #plateau boundaries
        ur_coords_x, ur_coords_y = input("Enter the upper right coordinates of the plateau (format - <int> <int>): ").split()
        ur_coords_x = int(ur_coords_x)
        ur_coords_y = int(ur_coords_y)
    except:
        print("Invalid input.")
        exit()

    map_instr = {'L': left,'R': right,'M': move}

    #read and process input
    process_input(read_input())