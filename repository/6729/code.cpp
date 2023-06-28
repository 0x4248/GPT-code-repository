#include <iostream>
#include <string>
#include <random>

int main(int argc, char** argv) {
    // Check if user entered correct number of command line arguments
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <password_length> <complexity>" << std::endl;
        return 1;
    }

    // Parse command line arguments
    int password_length = std::stoi(argv[1]);
    std::string complexity = argv[2];

    // Define character sets based on password complexity
    std::string uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    std::string lowercase = "abcdefghijklmnopqrstuvwxyz";
    std::string digits = "0123456789";
    std::string special = "!@#$%^&*()_-+={}[]\\|:;<>,.?/~`";

    std::string charset = "";
    if (complexity == "low") {
        charset = lowercase + digits;
    } else if (complexity == "medium") {
        charset = uppercase + lowercase + digits;
    } else if (complexity == "high") {
        charset = uppercase + lowercase + digits + special;
    } else {
        std::cerr << "Error: invalid complexity level" << std::endl;
        return 1;
    }

    // Seed random number generator with random device
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, charset.size() - 1);

    // Generate password
    std::string password = "";
    for (int i = 0; i < password_length; i++) {
        password += charset[dis(gen)];
    }

    std::cout << "Generated password: " << password << std::endl;

    return 0;
}
