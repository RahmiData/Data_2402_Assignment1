from file_IO import load_from_html
from data_processing import print_stats
# 1. Test the normal HTML loading
print("=== Testing student_dataset.txt ===")
table = load_from_html("student_dataset.txt")
print_stats(table)

# 2. Test the corrupted HTML loading
print("\n=== Testing student_dataset_corrupted.txt ===")
try:
    corrupted_table = load_from_html("student_dataset_corrupted.txt")
except AttributeError as e:
    print("Successfully caught expected AttributeError:")
    print(e)

