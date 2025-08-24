public class HelloWorld {
    public static void main(String[] args) {
      System.out.println("Hello World!");
      System.out.println("No u");
    }
  }

/* 
 Main method: lists program's tasks we mark the beggining and end with {} 
 System: Build-in java class that has useful tools
 Println: short for "print line" and Out: is short for Output

 import java.util.Scanner; (to import a scanner)
 Before the programm is run, compiler transforms it into binary and then lets the computer run it
 We can compile a java file by "javac (name).java"
 You can run a compiled code in a terminal using "java (name)"
 A double data type can hold huge int numbers and decimal ones
 A char can hold a single character
 (name)++ increases the value by one and -- reduces by one
 a.equals(b) checks if a==b as strings
 final int year = 2, makes this variable unchangable later
 void means there is no specific output from the method
 public means that otherclasses can access this method
 methods can have same names as long as their parameter list is unique (very cool)
 toString() method lets us print an objcet in a way we want (parameters as variables)
 if we create an array with new String[5]; (its an array of size 5, and this size cannot be changed)

 ArrayList<String> toDoList = new ArrayList<String>(); (Thats how you create a list)
 for the ArrayList we use    .get()   instead of [] as in arrays
 and to change values in the index we use   .set(0, "name")
 to remove we use  .remove("index or the name of the object")
 you can check the index of sth by   .indexOf()
 For-each loops    for(String i : inventoryItems)    then i will be the next thing in the list each iteration
 name.concat("man") equals nameman  (just adds two strings)
 .equals()  (checks if two strings are equal)
 class Triangle extends Shape {}     (this makes Triangle inherit all functions of Shape and you can add a triangle specific ones now)

 catch and try : used for handling errors
              public class Main{
                public static void main(String[] args) {
                int width = 0;
                int length = 40;
                try {
                  int ratio = length / width;
                } catch (ArithmeticException e) {
                  System.err.println("ArithmeticException: " + e.getMessage());
                }
              }
              }
*/