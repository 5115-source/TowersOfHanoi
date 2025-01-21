#Main method
def main():
    #User Input
    n = int(input("Enter number of disks: "))
    moves = [0] #Used a list as it can be updated within the moveDisks method
    #Find the solution recursively
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C', moves)
    print(f"Number of moves needed: {moves[0]}")

#The method for finding the solution to move n disks 
#from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower, moves):
    if n != 0: #Stopping condition
        moveDisks(n - 1, fromTower, auxTower, toTower, moves)
        print(f"Move disk {n} from {fromTower} to {toTower}")
        moveDisks(n - 1, auxTower, toTower, fromTower, moves)
        moves[0] += 1 #Each iteration add 1 to the index 0 of the moves list

#If there is a main method, run it
if __name__ == "__main__":
    main()