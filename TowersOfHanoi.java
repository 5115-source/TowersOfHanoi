package Chapter19Generics;

import java.util.*;


public class TowersOfHanoi {
    private static int move;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number of disks: ");
        move = input.nextInt();

        Towers(move);

        input.close();
    }

    public static void Towers(int disk){
        Stack<Integer> fromTower = new Stack<>();
        Stack<Integer> toTower = new Stack<>();
        Stack<Integer> auxTower = new Stack<>();

        for(int i = move; i >= 1; i--){
            fromTower.push(i);
        }

        Towers(disk, fromTower, "A", toTower, "C", auxTower, "B");

    }

    private static void Towers(int disk, Stack<Integer> fromTower,String fromTowerName, Stack<Integer> toTower, String toTowerName, Stack<Integer> auxTower, String auxTowerName){
            if(disk == 1){//base case, simplest case.
                Integer diskMoved = fromTower.pop();//pop the disk on top off
                toTower.push(diskMoved);//push the disk onto the toTower
                System.out.printf("Move disk %d from tower %s to tower %s%n", disk, fromTowerName, toTowerName);
            }else{
                Towers(disk - 1, fromTower, fromTowerName, auxTower, auxTowerName, toTower, toTowerName);
                System.out.printf("Move disk %d from tower %s to tower %s%n", disk, fromTowerName, toTowerName);
                Towers(disk - 1, auxTower, auxTowerName,  toTower, toTowerName,  fromTower, fromTowerName);
        }
    }
}
