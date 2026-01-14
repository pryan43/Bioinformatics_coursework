"""
Purpose:
Summarize gene expression values from a CSV file by computing
mean and standard deviation overall and by sample category.

Concepts demonstrated:
- CSV file parsing
- Dictionaries and lists
- Basic statistical calculations
- Error handling and input validation
"""
import os
import os.path
import sys
import math
import csv


if len(sys.argv) < 3:
    print("There is a problem!", file=sys.stderr)
    sys.exit(1)


filename = sys.argv[1]
gene_name = sys.argv[2]

homedir = '/home/student'
downloads_dir = os.path.join(homedir, 'Downloads')
downloads_filename = os.path.join(downloads_dir, filename)



if os.path.exists(downloads_filename):
    print(downloads_filename, "is there")
else:
    print(downloads_filename, "does not exist")
    sys.exit(1)



with open(downloads_filename) as f:
    rows = csv.DictReader(f)

    total_values = []
    category_values = {}

    

    for r in rows:
        if gene_name in r.keys():
            exp_value = float(r[gene_name])
            total_values.append(exp_value)

              
            sample_category = r[list(r.keys())[0]]

            if sample_category not in category_values:
                category_values[sample_category] = []

            category_values[sample_category].append(exp_value)
    

def mean_value(seq):
    if len(seq) == 0:
        return 0
    return sum(seq) / len(seq)


def stdev_value(seq):
    if len(seq) < 2:
        return 0
    compute_mean = mean_value(seq)
    variance = sum((value - compute_mean) ** 2 for value in seq) / (len(seq) - 1)
    return math.sqrt(variance)
    

overall_mean = mean_value(total_values)
overall_stdev = stdev_value(total_values)

print('Overall mean:', overall_mean)
print('Overall standard deviation:', overall_stdev)


keys_float = {float(k): v for k,v in category_values.items()}
keys = list(keys_float.keys())
key_mean = mean_value(keys)
key_std = stdev_value(keys)


print('Category mean:', key_mean)
print('Category standard deviation:', key_std)

f.close()
    



    








