# GPT code repository
# This repository contains code examples that chatGPT has generated.
# Github: https://www.github.com/lewisevans2007/GPT-code-repository
# By: Lewis Evans

import os

language_count = {}

code_folder_path = "repository"

extensions = {
    "Python": [".py"],
    "C++": [".cpp", ".hpp", ".h"],
    "C": [".c"],
    "Java": [".java"],
    "JavaScript": [".js"],
    "HTML": [".html"],
    "CSS": [".css"],
    "PHP": [".php"],
    "SQL": [".sql"],
    "Ruby": [".rb"],
    "Rust": [".rs"],
    "Go": [".go"],
    "Swift": [".swift"],
    "Kotlin": [".kt"],
    "TypeScript": [".ts"],
    "C#": [".cs"],
    "Scala": [".scala"],
    "Perl": [".pl"],
    "R": [".r"],
    "Objective-C": [".m"],
    "VBA": [".vba"],
    "MATLAB": [".m"],
    "Dart": [".dart"],
    "Lua": [".lua"]
}

for root, dirs, files in os.walk(code_folder_path):
    for file in files:
        file_extension = os.path.splitext(file)[1]
        for language, exts in extensions.items():
            if file_extension in exts:
                with open(os.path.join(root, file), "r", encoding="utf8") as f:
                    line_count = sum(1 for line in f)
                if language in language_count:
                    language_count[language] += line_count
                else:
                    language_count[language] = line_count

total_lines = sum(language_count.values())

stats = ""

for language, lines in language_count.items():
    percentage = round(lines / total_lines * 100, 2)
    stats += f"{language}: {percentage}%\n"

# below the line in README.md that says ## Languages used
with open("README.md", "r") as f:
    readme = f.read()

readme = readme.split("## Languages used")[0] + "## Languages used\n\n```\n" + stats + "```\n\n" 

with open("README.md", "w") as f:
    f.write(readme)