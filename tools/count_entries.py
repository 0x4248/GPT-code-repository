import os

import os

def count_total_lines():
    total_lines = 0
    for root, dirs, files in os.walk("repository/"):
        for file in files:
            if file.startswith("code."):
                with open(os.path.join(root, file)) as f:
                    total_lines += sum(1 for line in f if line.strip() and not line.startswith("#"))
    return total_lines

if __name__ == "__main__":
    count = 0
    for file in os.listdir("repository"):
        if os.path.isdir("repository/"+file):
            count += 1
    with open("README.md", "r") as f:
        readme = f.read()
    lines = readme.split("\n")
    lines[4] = "There are `"+str(count)+"` entires in this repository"
    lines[6] = "There is a total of `"+str(count_total_lines())+"` lines of code in this repository"
    with open("README.md", "w") as f:
        f.write("\n".join(lines))
