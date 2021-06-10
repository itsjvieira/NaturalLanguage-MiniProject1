# Natural Language 2020/2021, Mini-Project 1
# Joao Parreiro, 89483 / Joao Vieira, 90739

import itertools
import re
import sys

if len(sys.argv) != 4:
    print("ERROR: Invalid number of arguments!")
    sys.exit(1)

label_type = sys.argv[1]
right_labels_file = open(sys.argv[2])
predicted_labels_file = open(sys.argv[3])

right = 0
total = 0

predicted_labels = []
right_labels = []

if label_type == "-coarse":
    for line in predicted_labels_file:
        line = line.replace("\n", "")
        predicted_labels.append(line)

    for label in right_labels_file:
        substrings = re.split(":", label, 1)
        right_labels.append(substrings[0])

    for (right_label, predicted_label) in zip(right_labels, predicted_labels):
        if right_label == predicted_label:
            right += 1
        total += 1
elif label_type == "-fine":
    for line in predicted_labels_file:
        line = line.replace("\n", "")
        predicted_labels.append(line)

    for line in right_labels_file:
        line = line.replace("\n", "")
        right_labels.append(line)

    for (right_label, predicted_label) in zip(right_labels, predicted_labels):
        if right_label == predicted_label:
            right += 1
        total += 1
else:
    print("ERROR: Invalid label type!")
    sys.exit(1)

print("result:", (right / total) * 100)

predicted_labels_file.close()
right_labels_file.close()
