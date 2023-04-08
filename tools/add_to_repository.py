import random
import shutil
import os


def count_lines(file_path):
    with open(file_path, "r") as f:
        return sum(1 for line in f)


if __name__ == "__main__":
    print("Welcome to GPT code repository")
    print("Please copy the code that ChatGPT generated into ADD_TO_REPOSITORY.txt")
    print("Press enter when done")
    open("ADD_TO_REPOSITORY.txt", "w").close()
    input(">")

    id = random.randint(1000, 9999)

    print("Enter the prompt you used into ADD_PROMPT.txt")
    print("Press enter when done")
    open("ADD_PROMPT.txt", "w").close()
    input(">")

    print("Enter the title that ChatGPT generated")
    title = input(">")

    print("Enter the description that ChatGPT generated into ADD_DESCRIPTION.txt")
    print("Press enter when done")
    open("ADD_DESCRIPTION.txt", "w").close()
    input(">")

    print("Enter the language that ChatGPT generated")
    language = input(">")

    print("What is the file extension of the code e.g .py .c .cpp .java")
    extension = input(">")

    os.mkdir("repository/" + str(id))

    shutil.copy("ADD_TO_REPOSITORY.txt", "repository/" + str(id) + "/code" + extension)
    shutil.copy("ADD_PROMPT.txt", "repository/" + str(id) + "/prompt.txt")

    lines_of_code = count_lines("ADD_TO_REPOSITORY.txt")

    # Create a readme file
    with open("repository/" + str(id) + "/README.md", "w") as f:
        f.write("# " + title + " - " + str(id) + "\n\n")
        f.write("**Language**: `" + language + "`\n\n")
        f.write("**Lines of code**: `" + str(lines_of_code) + "`\n\n")
        f.write("## Description\n\n")
        with open("ADD_DESCRIPTION.txt", "r") as description_file:
            description_text = description_file.read()
        f.write(description_text + "\n\n")
        f.write("## Code\n\n``` " + language + "\n")
        with open("ADD_TO_REPOSITORY.txt", "r") as code_file:
            code_text = code_file.read()
        f.write(code_text + "\n```\n\n")
        f.write("## Prompt\n\n")
        with open("ADD_PROMPT.txt", "r") as prompt_file:
            prompt_text = prompt_file.read()
        f.write("```" + "\n")
        f.write(prompt_text + "\n")
        f.write("```")
    os.remove("ADD_TO_REPOSITORY.txt")
    os.remove("ADD_PROMPT.txt")
    os.remove("ADD_DESCRIPTION.txt")