# Sudoku Solver - 7108

**Language**: `Rust`

**Lines of code**: `87`

## Description

This program solves a 9x9 Sudoku puzzle using backtracking algorithm. It takes an input file containing a partially filled Sudoku puzzle and outputs the solution in the console.

To use this program, create a file named puzzle.txt in the same directory as the Rust file, and write the partially filled Sudoku puzzle in it. Use the . character to denote empty cells. For example:

```
53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
```

Then, run the program using cargo run command in the terminal. The program will read the puzzle from the input file, print it to the console, solve it, and print the solution to the console.

## Code

``` Rust
use std::fs;

const SIZE: usize = 9;
const EMPTY: char = '.';

fn main() {
    let input_file = "puzzle.txt";
    let puzzle = read_puzzle(input_file);
    print_puzzle(&puzzle);

    if solve(&mut puzzle) {
        println!("Solution:");
        print_puzzle(&puzzle);
    } else {
        println!("No solution found.");
    }
}

fn read_puzzle(file_name: &str) -> [[char; SIZE]; SIZE] {
    let contents = fs::read_to_string(file_name).expect("Failed to read file");
    let mut puzzle = [[EMPTY; SIZE]; SIZE];
    for (i, line) in contents.lines().enumerate() {
        for (j, ch) in line.chars().enumerate() {
            puzzle[i][j] = ch;
        }
    }
    puzzle
}

fn print_puzzle(puzzle: &[[char; SIZE]; SIZE]) {
    for i in 0..SIZE {
        for j in 0..SIZE {
            print!("{} ", puzzle[i][j]);
        }
        println!();
    }
    println!();
}

fn solve(puzzle: &mut [[char; SIZE]; SIZE]) -> bool {
    if let Some((i, j)) = find_empty_cell(puzzle) {
        for ch in 1..=9 {
            let ch = char::from_digit(ch, 10).unwrap();
            if is_valid_move(puzzle, i, j, ch) {
                puzzle[i][j] = ch;
                if solve(puzzle) {
                    return true;
                }
                puzzle[i][j] = EMPTY;
            }
        }
        false
    } else {
        true
    }
}

fn find_empty_cell(puzzle: &[[char; SIZE]; SIZE]) -> Option<(usize, usize)> {
    for i in 0..SIZE {
        for j in 0..SIZE {
            if puzzle[i][j] == EMPTY {
                return Some((i, j));
            }
        }
    }
    None
}

fn is_valid_move(puzzle: &[[char; SIZE]; SIZE], row: usize, col: usize, ch: char) -> bool {
    for i in 0..SIZE {
        if puzzle[row][i] == ch || puzzle[i][col] == ch {
            return false;
        }
    }

    let box_row = (row / 3) * 3;
    let box_col = (col / 3) * 3;
    for i in box_row..box_row + 3 {
        for j in box_col..box_col + 3 {
            if puzzle[i][j] == ch {
                return false;
            }
        }
    }

    true
}

```

## Prompt

```
Make me a program in rust that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.
```