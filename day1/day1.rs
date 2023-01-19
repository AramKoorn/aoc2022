use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    let mut numbers = vec![];
    let mut tmp = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        if !line.is_empty() {
            let number: i32 = line.parse().unwrap_or_default();
            tmp += number;
        } 
        else {
            numbers.push(tmp);
            tmp = 0;
        }
    };

    numbers.sort();

    let answer1 = numbers[numbers.len() - 1];
    let answer2: i32 = numbers.iter().rev().take(3).sum();

    //println!("Numbers in file: {:#?}", numbers);
    println!("{:?}", answer1);
    println!("{}", answer2);
}
