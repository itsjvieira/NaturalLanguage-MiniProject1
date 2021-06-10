# Natural Language 2020/2021, Mini-Project 1
# Joao Parreiro, 89483 / Joao Vieira, 90739

import re

file = open("DEV.txt")
labels_file = open("DEV-labels.txt", "a")
questions_file = open("DEV-questions.txt", "a")

for line in file:
    substrings = re.split(" ", line, 1)
    labels_file.write(substrings[0] + "\n")
    questions_file.write(substrings[1])

file.close()
labels_file.close()
questions_file.close()
