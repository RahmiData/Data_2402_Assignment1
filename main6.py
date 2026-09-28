from data_processing import print_stats
from file_IO import load_from_csv

# Test CSV loading on the massive census file
print("=== Loading census_dataset.txt ===")
census_data = load_from_csv("census_dataset.txt")

print(f"Successfully loaded {len(census_data)} rows!")
print("\n=== Census Statistics ===")
print_stats(census_data)