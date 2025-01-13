# This is a chatGPT rewrite of the java program to python, if any errors show up feel free to tweak things.

# Python uses input() instead of Scanner for getting user input. int() is used to conver the input int an integer.

# Python uses def to define functions, also the method signatures don't require a declaration of the type for the method.

# Python uses print() with formatted strings (f-strings) for output to the terminal.

# Main method: We use the if __name__ == "__main__": check to run the main method, which is a common Python convention for ensuring that the script runs properly when executed directly.
def move_disks(n, from_tower, to_tower, aux_tower):
    # Basecase 0, do nothing
    if n != 0:
        move_disks(n - 1, from_tower, aux_tower, to_tower)
        print(f"Move disk {n} from {from_tower} to {to_tower}")
        move_disks(n - 1, aux_tower, to_tower, from_tower)


def main():
    n = int(input("Enter number of disks: "))
    print("The moves are:")
    move_disks(n, 'A', 'C', 'B')


if __name__ == "__main__":
    main()
