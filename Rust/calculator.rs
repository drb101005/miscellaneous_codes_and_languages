use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter two numbers separated by space:");

    io::stdin().read_line(&mut input).unwrap();
    let nums: Vec<f64> = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    println!("Sum: {}", nums[0] + nums[1]);
}
