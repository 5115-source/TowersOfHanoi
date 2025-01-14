#Main method
def main():
    #User Input
    n = int(input("Enter number of disks: "))
    #Find the solution recursively
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')

#The method for finding the solution to move n disks 
#from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    if n != 0: #Stopping condition
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print(f"Move disk {n} from {fromTower} to {toTower}")
        moveDisks(n - 1, auxTower, toTower, fromTower)

#If there is a main method, run it
if __name__ == "__main__":
    main()