import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.time.format.DateTimeFormatter;

// Enum for task priority levels
public enum Priority {
    LOW, MEDIUM, HIGH;
}

// Class representing a task
public class Task {
    String title;
    String description;
    LocalDateTime deadline;
    Priority priority;
    boolean done;

    // Constructor to initialize a task
    public Task(String title,String description,LocalDateTime deadline,Priority priority,boolean done) {
        this.title = title;
        this.description = description;
        this.deadline = deadline;
        this.priority = priority;
        this.done = done;
    }

    // Method to check if the task is overdue and display time left or overdue time
    public void isOverdue() {
        if (!done) {
            LocalDateTime now = LocalDateTime.now();
            Duration difference = Duration.between(now, deadline).abs();
            long hours = Math.abs(difference.toHours());
            long minutes = Math.abs(difference.toMinutes() % 60);

            if (now.isAfter(deadline)) {
                System.out.println("The task is overdue: " + hours + " hours and " + minutes + " minutes.");
            } else {
                System.out.println("This task has still :" + hours + " hours and " + minutes + "minutes left until deadline.");
            }
        } else {
            System.out.println("Task has already been done.");
        }
    }

    // Mark the task as done
    public void markAsDone() {
        if (done == false) {
            done = true;
        }
    }

    // String representation of the task for printing
    public String toString() {
        return "Title: " + title + " | Description: " + description + " | Deadline: " + deadline +
            " | Priority: " + priority + " | Done: " + done;
    }
}

// Class to manage a list of tasks
class TaskManager {
    List<Task> tasks = new ArrayList<>();

    // Add a task to the list
    public void addTask(Task task) {
        tasks.add(task);
    }

    // Remove a task by index
    public void removeTask(int index) {
        tasks.remove(index);
    }

    // Sort tasks based on a criterion (deadline, priority, or none)
    public void sortTasks(String criterion) {
        if (criterion.equals("deadline")) {
            tasks.sort(Comparator.comparing(task -> task.deadline));
        } else if (criterion.equals("priority")) {
            tasks.sort(Comparator.comparing(task -> task.priority));
        } else if (criterion.equals("none")) {
            // do nothing
        } else {
            System.out.println("Invalid input. Please choose either 'deadline', 'priority' or 'none'.");
        }
    }

    // Print the upcoming task with the nearest deadline
    public void printUpcomingTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
            return;
        }
        Task soonestEnding = tasks.stream()
            .filter(t -> t.deadline.isAfter(LocalDateTime.now()))
            .min(Comparator.comparing(t -> t.deadline))
            .orElse(null);

        if (soonestEnding != null) {
            System.out.println(soonestEnding);
        } else {
            System.out.println("No upcoming tasks found.");
        }
    }

    // Mark a specific task as done by its index
    public void markTaskAsDone(int index) {
        if (index < 0 || index >= tasks.size()) {
            System.out.println("Invalid index.");
            return;
        }
        tasks.get(index).markAsDone();
    }

    // Retrieve a task by its index
    public Task getTask(int index) {
        if (index >= 0 && index < tasks.size()) {
            return tasks.get(index);
        } else {
            System.out.println("Invalid index.");
            return null;
        }
    }
}

// Class for saving and loading tasks from a file
class FileHandler {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");

    // Save a list of tasks into a file
    public void saveTasks(List<Task> tasks, String filename) {
        if (!filename.endsWith(".txt")) {
            filename += ".txt";
        }

        try (java.io.PrintWriter writer = new java.io.PrintWriter(filename)) {
            for (Task task : tasks) {
                writer.println(task.title + ";" + 
                               task.description + ";" +
                               task.deadline.format(formatter) + ";" +
                               task.priority + ";" +
                               task.done);
            }
            System.out.println("Tasks saved successfully in a " + filename + " file.");
        } catch (IOException e) {
            System.out.println("Error while saving tasks: " + e.getMessage());
        }
    }

    // Load a list of tasks from a file
    public List<Task> loadedTasks(String filename) {
        List<Task> loadedTasks = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(";");
                if (parts.length == 5) {
                    String title = parts[0];
                    String description = parts[1];
                    LocalDateTime deadline = LocalDateTime.parse(parts[2], formatter);
                    Priority priority = Priority.valueOf(parts[3]);
                    boolean done = Boolean.parseBoolean(parts[4]);

                    Task task = new Task(title, description, deadline, priority, done);
                    loadedTasks.add(task);
                }
            }
            System.out.println("Tasks loaded successfully.");
        } catch (IOException e) {
            System.out.println("Error while loading tasks :" + e.getMessage());
        }
        return loadedTasks;
    }
}

// Main class that handles user interaction
public class Main {
    Scanner scanner = new Scanner(System.in);
    TaskManager manager = new TaskManager();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");

    // Allow the user to add a new task
    public void addTask() {
        System.out.print("Enter task title: ");
        String title = scanner.nextLine();

        System.out.print("Enter task description: ");
        String description = scanner.nextLine();

        System.out.print("Enter the deadline (e.g. 21-04-2023 19:31): ");
        String deadlineInput = scanner.nextLine();
        LocalDateTime deadline = LocalDateTime.parse(deadlineInput, formatter);

        System.out.print("Enter its priority: ");
        String priorityInput = scanner.nextLine();
        Priority priority = Priority.valueOf(priorityInput.toUpperCase());

        Task task = new Task(title, description, deadline, priority, false);
        manager.addTask(task);

        System.out.println("Task added:\n" + task);
    }

    // View tasks with optional sorting
    public void viewTasks() {
        System.out.print("Sorted by (deadline/priority/none): ");
        String deadlineOrPriority = scanner.nextLine();

        manager.sortTasks(deadlineOrPriority);

        if (manager.tasks.isEmpty()) {
            System.out.println("No tasks available.");
        } else {
            for (Task task : manager.tasks) {
                System.out.println(task);
            }
        }
    }

    // View only overdue tasks
    public void viewOverdue() {
        boolean anyOverdue = false;
        for (Task task : manager.tasks) {
            if (!task.done && task.deadline.isBefore(LocalDateTime.now())) {
                System.out.println(task);
                anyOverdue = true;
            }
        } 
        if (anyOverdue == false) {
            System.out.println("No overdue tasks found.");
        }
    }

    // Mark a task as done by its index
    public void markAsDone() {
        System.out.print("Which task do you want to mark as done (index): ");
        int inputIndex = Integer.parseInt(scanner.nextLine());
    
        if (inputIndex < 0 || inputIndex >= manager.tasks.size()) {
            System.out.println("Invalid task index.");
            return;
        }
    
        Task selectedTask = manager.getTask(inputIndex);
        selectedTask.markAsDone();
        System.out.println("Task with an index " + inputIndex + " has been marked as done.");
    }
    
    // Delete a task by its index
    public void deleteTask() {
        System.out.print("Which task do you want to delete (index): ");
        int inputIndex = Integer.parseInt(scanner.nextLine());

        manager.removeTask(inputIndex);

        System.out.println("Task at index " + inputIndex + " has been deleted.");
    }
    
    // Save or load tasks from a file
    public void saveAndLoad() {
        FileHandler fileHandler = new FileHandler();
        System.out.println("Save or load (save/load): ");
        String saveOrLoad = scanner.nextLine();

        System.out.println("Enter the filename: ");
        String fileName = scanner.nextLine();

        if (saveOrLoad.equalsIgnoreCase("save")) {
            fileHandler.saveTasks(manager.tasks, fileName);
        } else if (saveOrLoad.equalsIgnoreCase("load")) {
            List<Task> loadedTasks = fileHandler.loadedTasks(fileName);

            while (true) {
                System.out.println("You want to overwrite or merge (overwrite/merge): ");
                String input = scanner.nextLine();

                if (input.equalsIgnoreCase("merge")) {
                    manager.tasks.addAll(loadedTasks);
                    break;
                } else if (input.equalsIgnoreCase("overwrite")) {
                    manager.tasks.clear();
                    manager.tasks.addAll(loadedTasks);
                    break;
                } else {
                    System.out.println("Invalid input. Please type 'overwrite' or 'merge'.");
                }
            }
        } else {
            System.out.println("Invalid input. Please enter 'save' or 'load'.");
        }
    }
    
    // Display the menu options
    public void openMenu() {
        System.out.println("Click a number you wish to proceed with:\n" +
        "1.Add Task\n" +
        "\n" +
        "2.View Tasks (sorted)\n" +
        "\n" +
        "3.View Overdue\n" +
        "\n" +
        "4.Mark as Done\n" +
        "\n" +
        "5.Delete Task\n" +
        "\n" +
        "6.Save & Load\n" +
        "\n" +
        "7.Exit");
    }

    // Read and validate user menu input
    public int userInput() {
        while (true) {
            String input = scanner.nextLine();
            try {
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("That is not a valid number!");
            }
        }
    }

    // Main loop: run the task manager app
    public static void main(String[] args) {
        Main mainApp = new Main();

        while (true) {
            mainApp.openMenu();
            int inputNumber = mainApp.userInput();

            if (inputNumber == 1) {
                mainApp.addTask();
            } else if (inputNumber == 2) {
                mainApp.viewTasks();

            } else if (inputNumber == 3) {
                mainApp.viewOverdue();

            } else if (inputNumber == 4) {
                mainApp.markAsDone();

            } else if (inputNumber == 5) {
                mainApp.deleteTask();

            } else if (inputNumber == 6) {
                mainApp.saveAndLoad();
                
            } else if (inputNumber == 7) {
                System.out.println("Goodbye!");
                break;
            }
        }
    }
}
