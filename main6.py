from data_processing import print_stats
from file_IO import load_dataset, save_to_json

# 1. Test load_dataset on HTML
print("=== Testing load_dataset on HTML ===")
html_data = load_dataset("student_dataset.txt")
print(f"Loaded {len(html_data)} HTML records.")

# 2. Test save_to_json
print("\n=== Testing save_to_json ===")
save_to_json(html_data[:5], "student_sample.json")
print("Saved 5 records to student_sample.json successfully!")

# 3. Test load_dataset on CSV
print("\n=== Testing load_dataset on CSV ===")
csv_data = load_dataset("census_dataset.txt")
print(f"Loaded {len(csv_data)} CSV records.")

# 4. Test load_dataset on invalid format (vote.arff)
print("\n=== Testing load_dataset on ARFF (should raise Exception) ===")
try:
    load_dataset("vote.arff")
except Exception as e:
    print("Caught expected exception:")
    print(e)