# Image Resizer - 9281

**Language**: `C++`

**Lines of code**: `37`

## Description

This program takes an input image file, resizes it to a user-specified dimension, and saves the resized image as a new file. The program uses the OpenCV library for image manipulation.

This program is a command-line tool that can be used to resize images to a specified dimension. It uses the OpenCV library to read the input image file, resize it, and write the resized image as a new file. The user can specify the input image file path, output image file path, and the desired dimension for the resized image as command line arguments. The program performs basic error checking and returns appropriate error messages if any errors occur.

## Code

```C
#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv) {
    // Check if user entered correct number of command line arguments
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " <input_image_path> <output_image_path> <dimension>" << std::endl;
        return 1;
    }

    // Parse command line arguments
    std::string input_image_path = argv[1];
    std::string output_image_path = argv[2];
    int dimension = std::stoi(argv[3]);

    // Read input image
    cv::Mat input_image = cv::imread(input_image_path);
    if (input_image.empty()) {
        std::cerr << "Error: could not read input image " << input_image_path << std::endl;
        return 1;
    }

    // Resize image
    cv::Mat resized_image;
    cv::resize(input_image, resized_image, cv::Size(dimension, dimension));

    // Write output image
    if (!cv::imwrite(output_image_path, resized_image)) {
        std::cerr << "Error: could not write output image " << output_image_path << std::endl;
        return 1;
    }

    std::cout << "Resized image saved as " << output_image_path << std::endl;

    return 0;
}

```

## Prompt

```
Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

Don’t make the program more than 150 lines long

When you create the program make a title for it and a short description of what it does.

Don’t use python and don’t write a game
```