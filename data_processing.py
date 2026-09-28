def print_stats(data: list[dict]) -> None:
    """
    Accepts a dataset stored as a list of dictionaries.
    Prints each column's name, and its most common value (for text columns)
    or it's average value (for numeric columns)
    """
    
    # This assuming that all dictionaries in the list will have same keys
    columns = data[0].keys()

    for column in columns:
        # This determine if this is a text or numeric column
        if type(data[0][column]) == float:
            # Task 1: Initialize our variables
            data_sum = 0.0
            data_count = 0
            
            # Task 2: Loop through the rows to gather data
            for row in data:
                # This adds the numeric value from this row to your sum
                data_sum += row[column] 
                # Increment your counter by 1
                data_count += 1
                
                # Task 3: Calculate and print AFTER the loop finishes
            average = data_sum / data_count
            print(f"average value for {column}: {average:.1f}")
                
        else:  # this is a text column
            
            # build a dict that counts number of times we've seen each value
            # within this column
            value_counts = dict()
            for row in data:
                value_counts[row[column]] = value_counts.get(row[column], 0) + 1

            # identify the key correponding to the max value
            biggest_count = 0
            most_common = None
            for value, count in value_counts.items():
                if count > biggest_count:
                    biggest_count = count
                    most_common = value
            
            print(f"most common value for {column}: {most_common}")
