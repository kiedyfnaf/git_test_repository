import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.Year;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.time.format.DateTimeFormatter;

class Loan {
    LibraryItem item;
    Member member;
    LocalDateTime dueDate;

    public Loan(LibraryItem item, Member member, LocalDateTime dueDate) {
        this.item = item;
        this.member = member;
        this.dueDate = dueDate;
    }

    public String toString() {
        return "Item " + item.getId() + " | Member: " + member.getMemberId() +
         " | Due date: " +
          dueDate.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));
    }
}

abstract class LibraryItem {
    String id;
    String title;
    int year;

    public abstract String getDetails();
    
    public String getTitle() {
        return title;
    }

    public String getId() {
        return id;
    }

    public int getYear() {
        return year;
    }
}

public class CommonDetails {
    String id;
    String title;
    int year;

    public CommonDetails(String id, String title, int year) {
        this.id = id;
        this.title = title;
        this.year = year;
    }
}

class Book extends LibraryItem {
    String author;
    String publisher;

    public Book(String id, String title, int year, String author, String publisher) {
        this.id = id;
        this.title = title;
        this.year = year;
        this.author = author;
        this.publisher = publisher;
    }

    public String getDetails() {
        return "Id: " + id + " | Title: " + title + " | Year: " + year + " | Author: " +
            author + " | Publisher: " + publisher + ".";
    }

}

class Magazine extends LibraryItem {
    int issueNumber;

    public Magazine(String id, String title, int year, int issueNumber) {
        this.id = id;
        this.title = title;
        this.year = year;
        this.issueNumber = issueNumber;
    }

    public String getDetails() {
        return "Id: " + id + " | Title: " + title + " | Year: " + year + 
            " | Issue Number: " + issueNumber + ".";
    }
}

class DVD extends LibraryItem {
    double duration;
    String regionCode;

    public DVD(String id, String title, int year, double duration, String regionCode) {
        this.id = id;
        this.title = title;
        this.year = year;
        this.duration = duration;
        this.regionCode = regionCode;
    }

    public String getDetails() {
        return "Id: " + id + " | Title: " + title + " | Year: " + year + 
            " | Duration: " + duration + " | Region code: " + regionCode + ".";
    }
}

class Member {
    String memberId;
    String name;
    List<Loan> loans = new ArrayList<>();
    
    public Member(String memberId, String name) {
        this.memberId = memberId;
        this.name = name;
    }

    public Loan borrow(LibraryItem item) {
        Loan loan = new Loan(item, this, LocalDateTime.now().plusDays(10));
        loans.add(loan);
        return loan;
    }

    public void returnItem(LibraryItem item) {
        boolean doesLoanExist = false;
        for (Loan loan : loans) {
            if (loan.item == item) {
                loans.remove(loan);
                doesLoanExist = true;
                System.out.println("You have returned: " + item.getTitle());
                break;
            }
        }
        if (!doesLoanExist) {
            System.out.println("You did not loan this item.");
        }
    }

    public void showLoanedItems() {
        if (loans.size() == 0) {
            System.out.println("Member:" + memberId + " has not loaned any items.");
        }
        for (Loan loan : loans) {
            System.out.println(loan.toString());
        }
    }

    public void showOverDueLoans() {
        boolean overDue = false;
        for (Loan loan : loans) {
            if (loan.dueDate.isBefore(LocalDateTime.now())) {
                System.out.println(loan.toString());
                overDue = true;
            }
        }
        if (overDue == false) {
            System.out.println("Member: " + memberId + " has not overdue loans.");
        }
    }

    public String getName() {
        return name;
    }

    public String getMemberId() {
        return memberId;
    }
}

class Library {
    Map<String,LibraryItem> catalog = new HashMap<>();
    Map<String,Member> members = new HashMap<>();

    public void addItem(LibraryItem item) {
        catalog.put(item.getId(), item);
    }

    public void removeItem(String itemId) {
        if (catalog.containsKey(itemId)) {
            catalog.remove(itemId);
            System.out.println("An item with id: " + itemId + " has been deleted.");
        } else {
            System.out.println("An item with id: " + itemId + " does not exist within the library.");
        }
        
    } 

    public void registerMember(Member m) {
        members.put(m.memberId, m);
    }

    public List<LibraryItem> searchByTitle(String title) {
        List<LibraryItem> results = new ArrayList<>();
        for (LibraryItem item : catalog.values()) {
            if (item.getTitle().equalsIgnoreCase(title)) {
                results.add(item);
            }
        }
        return results;
    }

    public List<LibraryItem> searchByYear(int year) {
        List<LibraryItem> results = new ArrayList<>();
        for (LibraryItem item : catalog.values()) {
            if (item.getYear() == year) {
                results.add(item);
            }
        }
        return results;
    }

    public void loanItem(String itemId, String memberId) {
        if (catalog.containsKey(itemId)) {
            Member m = members.get(memberId);
            if (m != null) {
                LibraryItem item = catalog.get(itemId);
                Loan loan = m.borrow(item);
                catalog.remove(itemId);
                System.out.println("Item loaned. Due date: " +
                 loan.dueDate.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")));
            } else {
                System.out.println("No member with Id: " + memberId + " exists.");
            }
            
        } else {
            System.out.println("You cannot loan the item with id: " + itemId);
        }
    }

    public void returnItem(String itemId, String memberId) {
        Member m = members.get(memberId);
        if (m == null) {
            System.out.println("No member with Id: " + memberId + " exists.");
            return;
        }
        if (!catalog.containsKey(itemId)) {
            boolean foundLoan = false;
            for (Loan loan : new ArrayList<>(m.loans)) {
                if (loan.item.getId().equals(itemId) && loan.member.getMemberId.equals(m.getMemberId())) {
                    LibraryItem item = loan.item;
                    m.loans.remove(loan);
                    catalog.put(itemId, item);
                    foundLoan = true;
                    break;
                }   
            }
            if (!foundLoan) {
                System.out.println("You have not loaned the item or the item doesnt exist: " + itemId);
            }         
        } else {
            System.out.println("The item :" + itemId + " is already in the library.");
        }
    }
}

class Main {
    Scanner scanner = new Scanner(System.in);
    Library lib = new Library();
    public int userInput() {
        while (true) {
            String input = scanner.nextLine().trim().toLowerCase();
            try {
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("That is not a valid number!");
            }
        }
    }

    public CommonDetails addDetails() {
        System.out.println("Fill the details of this item; " + "\n" + "Item id: ");
        while (true) {
            String id = scanner.nextLine().trim().toLowerCase();
            if (!lib.catalog.containsKey(commonDetails.id)) {
                break;
            } else {
                System.out.println("An item with this ID already exists. Please try again: ");
            }
        }
        System.out.println("Title: ");
        String title = scanner.nextLine().trim().toLowerCase();
        System.out.println("Year of publishing: ");
        int year = Integer.parseInt(scanner.nextLine());
        return new CommonDetails(id, title, year);
    }

    public void addItemMain() {
        CommonDetails commonDetails = addDetails(); //Later check if this item maybe alredy is in the library
        System.out.println("What is it (book, dvd, magazine): ");
        while (true) {
            String itemType = scanner.nextLine().trim().toLowerCase();
            if (itemType.equalsIgnoreCase("book")) {
                System.out.println("Author: ");
                String author = scanner.nextLine().trim().toLowerCase();
                System.out.println("Publisher: ");
                String publisher = scanner.nextLine().trim().toLowerCase();
                Book item = new Book(commonDetails.id, commonDetails.title, commonDetails.year, author, publisher);
                lib.addItem(item);
                break;
            } else if (itemType.equalsIgnoreCase("dvd")) {
                System.out.println("Duration: ");
                double duration = Double.parseDouble(scanner.nextLine());
                System.out.println("Region code: ");
                String regionCode = scanner.nextLine().trim().toLowerCase();
                DVD item = new DVD(commonDetails.id, commonDetails.title, commonDetails.year, duration, regionCode);
                lib.addItem(item);
                break;
            } else if (itemType.equalsIgnoreCase("magazine")) {
                System.out.println("Issue number: ");
                int issueNumber = Integer.parseInt(scanner.nextLine());
                Magazine item = new Magazine(commonDetails.id, commonDetails.title, commonDetails.year, issueNumber);
                lib.addItem(item);
                break;
            } else {
                System.out.println("Invalid input. Please write 'book', 'dvd' or 'magazine': ");
            }
        }
    }

    public void removeItemMain() {
        System.out.println("What is the Id of this item: ");
        String id = scanner.nextLine().trim().toLowerCase();
        lib.removeItem(id);
    }

    public String removeOrAdd() {
        System.out.println("You wish to (add/remove); ");
        while (true) {
            String input = scanner.nextLine().trim().toLowerCase();
            if (!(input.equalsIgnoreCase("add") || input.equalsIgnoreCase("remove"))) {
                System.out.println("Invalid input. Enter 'add' or 'remove': "); 
            } else {
                return input;
            }
        }
    }

    public void addNewMember() {
        System.out.println("The name: ");
        String userInputName = scanner.nextLine().trim().toLowerCase();
        System.out.println("Member id: ");
        while (true) {
            String userInputMemberId = scanner.nextLine().trim().toLowerCase();
            if (!lib.members.containsKey(userInputMemberId)) {
                Member m = new Member(userInputMemberId, userInputName);
                lib.registerMember(m);
                System.out.println("Member added: " + userInputName + " (" + userInputMemberId + ")");
                break;
            } else {
                System.out.println("There already exists a member with such id. Please choos again: ");
            }
        }
    }
    
    public void bookLoanOrReturn() {
        System.out.println("What do you wish to do (book/loan/return): ");
        while (true) {
            String userInput = scanner.nextLine().trim().toLowerCase();
            if (userInput.equalsIgnoreCase("book")) {
                // Not today
            } else if (userInput.equalsIgnoreCase("loan")) {
                System.out.println("Member id: ");
                String userInputMemberId = scanner.nextLine().trim().toLowerCase();
                System.out.println("Item id: ");
                String userInputItemId = scanner.nextLine().trim().toLowerCase();
                if (lib.members.containsKey(userInputMemberId) && lib.catalog.containsKey(userInputItemId)) {
                    lib.loanItem(userInputItemId, userInputMemberId);
                    break;
                } else {
                    System.out.println("Wrong Member id or Item id.");
                }
            } else if (userInput.equalsIgnoreCase("return")) {
                System.out.println("Member id: ");
                String userInputMemberId = scanner.nextLine().trim().toLowerCase();
                System.out.println("Item id: ");
                String userInputItemId = scanner.nextLine().trim().toLowerCase();
                if (lib.members.containsKey(userInputMemberId) && lib.catalog.containsKey(userInputItemId)) {
                    lib.returnItem(userInputItemId, userInputMemberId);
                    break;
                } else {
                    System.out.println("Wrong Member id or Item id.");
                }
            }
        }
    }

    public void searchLibraryBy() {
        System.out.println("By what do you wish to search (title/id/year): ");
        while (true) {
            String userInput = scanner.nextLine().trim().toLowerCase();
            if (userInput.equalsIgnoreCase("title")) {
                System.out.println("Enter the title: ");
                String userInputTitle = scanner.nextLine().trim().toLowerCase();
                List<LibraryItem> sortedByTitle = searchByTitle();
                if (sortedByTitle.size() != 0) {
                    for (LibraryItem item : sortedByTitle) {
                        System.out.println(item.getDetails());
                        break;
                    }
                }

            } else if (userInput.equalsIgnoreCase("id")) {
                System.out.println("Enter the id: ");
                String userInputId = scanner.nextLine().trim().toLowerCase();
                LibraryItem item = catalog.get(userInputId);
                if (item != null) {
                    System.out.println(item.getDetails());
                    break;
                } else {
                    System.out.println("Item with id: " + userInputId + " does not exist within the library.");
                }
            } else if (userInput.equalsIgnoreCase("year")) {
                System.out.println("Enter the year: ");
                int userInputYear = Integer.parseInt(scanner.nextLine(userInput));
                List<LibraryItem> sortedByYear = searchByYear();
                if (sortedByYear.size() != 0) {
                    for (LibraryItem item : Year) {
                        System.out.println(item.getDetails());
                        break;
                    }
                }
            } else {
                System.out.println("Invalid input. Please enter 'title', 'id' or 'year': ");
            }
        }
    }

    public void openMenu() {
        System.out.println("Click a number you wish to proceed with:\n" +
        "1.Add/remove an item\n" +
        "\n" +
        "2.View member\n" +
        "\n" +
        "3.Book/loan/return an item\n" +
        "\n" +
        "4.Register a member\n" +
        "\n" +
        "5.Search the library\n" +
        "\n" +
        "6.Exit");
    }

    public static void main(String[] args) {
        Main mainApp = new Main();

        while (true) {
            mainApp.openMenu();
            int inputNumber = mainApp.userInput();

            switch (inputNumber) {
                case 1 :
                    String removeOrAdd = mainApp.removeOrAdd();
                    if (removeOrAdd.equals("add")) {
                        mainApp.addItemMain();
                    } else {
                        mainApp.removeItemMain();
                    }
                    break;
                case 2:
                    // Crete a password for the member while he is making an account 
                    // so when we wants to check his deatils (name, ...) he has to
                    // enter a password, but if its to check loans he does (or does idk yet)
                    break;
                case 3:
                    mainApp.bookLoanOrReturn();
                    break;

                case 4:
                    mainApp.addNewMember();
                    break;

                case 5:
                    mainApp.searchLibraryBy();
                    break;

                case 6:
                    System.out.println("Goodbye!");
                    break;
                
                default:
                    break;
            }
        }
    }
}

