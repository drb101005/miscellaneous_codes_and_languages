class Person {
    String name;
    int id;

    // Constructor of Person class
    Person(String name, int id) {
        this.name = name;
        this.id = id;
        System.out.println("Person constructor called.");
    }

    // Method to display person details
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("ID: " + id);
    }
}

// Employee class inherits from Person
class Employee extends Person {
    double salary;

    // Constructor of Employee class
    Employee(String name, int id, double salary) {
        super(name, id); // calling parent constructor
        this.salary = salary;
        System.out.println("Employee constructor called.");
    }

    // Overriding displayDetails method
    void displayDetails() {
        super.displayDetails(); // calling parent method
        System.out.println("Salary: " + salary);
    }
}

// Main class
public class InheritanceWithSuperDemo {
    public static void main(String[] args) {
        Employee emp = new Employee("Jai", 101, 50000.0);
        emp.displayDetails();
    }
}