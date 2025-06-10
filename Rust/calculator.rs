use std::io;

fn main() {
    println!("Simple Rust Calculator");

    // Read first number
    let mut input1 = String::new();
    println!("Enter the first number:");
    io::stdin().read_line(&mut input1).expect("Failed to read input");
    let num1: f64 = input1.trim().parse().expect("Please enter a valid number");

    // Read operator
    let mut operator = String::new();
    println!("Enter an operator (+, -, *, /):");
    io::stdin().read_line(&mut operator).expect("Failed to read input");
    let operator = operator.trim();

    // Read second number
    let mut input2 = String::new();
    println!("Enter the second number:");
    io::stdin().read_line(&mut input2).expect("Failed to read input");
    let num2: f64 = input2.trim().parse().expect("Please enter a valid number");

    // Perform calculation
    let result = match operator {
        "+" => num1 + num2,
        "-" => num1 - num2,
        "*" => num1 * num2,
        "/" => {
            if num2 == 0.0 {
                println!("Error: Cannot divide by zero.");
                return;
            }
            num1 / num2
        }
        _ => {
            println!("Invalid operator.");
            return;
        }
    };

    println!("Result: {}", result);
}
