import java.util.Scanner;

public class TaskScheduler {

    // A custom array list to store the tasks
    private static class Task {
        String name;
        float time;
    }

    private Task[] tasks = new Task[10];
    private int size;

    public TaskScheduler() {
        size = 0;
    }

    // Method to add a new task to the list
    public void addTask(String name, float time) {
        for (int i = 0; i < size; i++) {
            if (tasks[i].name.equals(name)) {
                // Do not allow for duplicate tasks
                System.out.println("A task with the name '" + name + "' already exists");
                return;
            }
        }
        if (size == tasks.length) {
            resize();
        }
        Task t = new Task();
        t.name = name;
        t.time = time;
        tasks[size] = t;
        size++;
    }

    // Method to remove a task from the list
    public void removeTask(String name) {
        int index = -1;
        for (int i = 0; i < size; i++) {
            if (tasks[i].name.equals(name)) {
                index = i;
                break;
            }
        }
        if (index == -1) {
            // Task not found
            System.out.println("A task with the name '" + name + "' could not be found");
            return;
        }
        for (int i = index; i < size - 1; i++) {
            tasks[i] = tasks[i + 1];
        }
        size--;
    }

    // Method to view all the tasks in the list
    public void viewTasks() {
        for (int i = 0; i < size; i++) {
            Task t = tasks[i];
            System.out.println((i + 1) + ". " + t.name + " (" + t.time + " hours)" + "/n");
        }
    }

    // Method to resize the array if it is full
    private void resize() {
        Task[] newTasks = new Task[tasks.length * 2];
        for (int i = 0; i < tasks.length; i++) {
            newTasks[i] = tasks[i];
        }
        tasks = newTasks;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TaskScheduler scheduler = new TaskScheduler();

        final int ADD_TASK = 1;
        final int REMOVE_TASK = 2;
        final int VIEW_TASKS = 3;
        final int SIZE = 4;
        final int EXIT = 5;


        int choice;
        do {
            System.out.println("1. Add a task");
            System.out.println("2. Remove a task");
            System.out.println("3. View all tasks");
            System.out.println("4. Size");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

            if (choice == ADD_TASK) {
                sc.nextLine(); // Consume the newline character
                System.out.print("Enter the name of the task: ");
                String name = sc.nextLine();
                System.out.print("Enter the duration of the task (in hours): ");
                float time = sc.nextFloat();
                scheduler.addTask(name, time);
            } else if (choice == REMOVE_TASK) {
                sc.nextLine(); // Consume the newline character
                System.out.print("Enter the name of the task you would like to remove (case sensitive): ");
                String name = sc.nextLine();
                scheduler.removeTask(name);
            } else if (choice == VIEW_TASKS) {
                scheduler.viewTasks();
            } else if (choice == SIZE) {
                System.out.println(scheduler.size);
            } else {
                System.out.println("Invalid choice");
            }
            if (choice == VIEW_TASKS) {
                scheduler.viewTasks();
            }
        } while (choice != EXIT);
    }
}
