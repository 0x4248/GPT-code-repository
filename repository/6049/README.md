# File Searcher - 6049

**Language**: `Rust`

**Lines of code**: `34`

## Description

This program searches for files in a given directory that match a user-specified pattern. The user can specify the directory to search and the pattern to match. The program uses the Rust standard library and the walkdir crate to traverse the directory and search for files.

## Code

``` Rust
extern crate walkdir;

use std::env;
use std::path::PathBuf;
use walkdir::WalkDir;

fn main() {
    // Parse command line arguments
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: {} <directory> <pattern>", args[0]);
        std::process::exit(1);
    }
    let directory = &args[1];
    let pattern = &args[2];

    // Traverse the directory and search for files matching the pattern
    let mut results: Vec<PathBuf> = Vec::new();
    for entry in WalkDir::new(directory).into_iter().filter_map(|e| e.ok()) {
        if entry.file_type().is_file() && entry.file_name().to_string_lossy().contains(pattern) {
            results.push(entry.path().to_path_buf());
        }
    }

    // Print out the matching file paths
    if results.is_empty() {
        println!("No files matching pattern '{}' were found in directory '{}'.", pattern, directory);
    } else {
        println!("Files matching pattern '{}' in directory '{}':", pattern, directory);
        for path in results {
            println!("{}", path.to_string_lossy());
        }
    }
}

```

## Prompt

```
Make me a program in rust that is more than 20 lines of code long and is complex and interesting.

Don’t make the program more than 150 lines long

When you create the program make a title for it and a short description of what it does.

Don’t use python and don’t make a game try to make something interesting.
```