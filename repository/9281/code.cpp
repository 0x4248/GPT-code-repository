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
