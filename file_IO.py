

def load_from_html(filename: str) -> list[dict]:
    """
    reads a dataset in HTML format. converts numeric data to float.
    raises an AttributeError if the table rows do not all have the same number of values.
    :param filename: the file path of the html data to read
    :return: the dataset as a list of dictionaries - one dict per object in the file
            each dictionary should map column names to values
    """    
    with open(filename, 'r') as file:
        contents = file.read()
        all_rows = []

        head, body = contents.split('</thead>')

        # process the head first, pull out the column names
        head_parts = head.split('<td>')

        columns = []
        for column_name in head_parts[1:]:
            columns.append(
                column_name.replace('</td>', '').replace('</tr>', '').strip()
            )
        
        # strip off some unecessary tags
        body = body.replace('</tr>', '')
        body = body.replace('</tbody>\n</table>', '')

        # process the rest of the text: the table body
        rows_text = body.split('<tr>')
        for row_text in rows_text[1:]: # skip the first, which just has a <tbody> tag
            row_text = row_text.replace('</td>', '')
            values = row_text.split('<td>')
            values = values[1:]

            # check the row has the right number of values in it
            if len(values) != len(columns):
                raise AttributeError(f'wrong number of values in row: {row_text}')

            this_row_dict = dict()
            for i in range(len(columns)):
                this_column = columns[i]
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    pass

                this_row_dict[this_column] = this_value
            
            all_rows.append(this_row_dict)
    
    return all_rows

def load_from_csv(filename: str) -> list[dict]:
  """Reads a tabular dataset in CSV format without external libraries.

  Converts numeric values to float where possible.
  """
  all_rows = []

  with open(filename, 'r') as file:
    lines = file.readlines()

    # If the file is completely empty, return empty list
    if not lines:
      return all_rows

    # Extract header columns from the first line
    header_line = lines[0].strip()
    columns = [col.strip() for col in header_line.split(',')]

    # Process each data row
    for line in lines[1:]:
      line = line.strip()
      if not line:
        continue  # skip blank lines

      values = [val.strip() for val in line.split(',')]

      # Check for row value alignment with headers
      if len(values) != len(columns):
        raise AttributeError(f'wrong number of values in row: {line}')

      row_dict = {}
      for i in range(len(columns)):
        col_name = columns[i]
        val = values[i]

        # Convert to float if numeric
        try:
          val = float(val)
        except ValueError:
          pass

        row_dict[col_name] = val

      all_rows.append(row_dict)

  return all_rows




def load_dataset(filename: str) -> list[dict]:
    """
    Identifies if a dataset is CSV or HTML format and parses it accordingly.
    Raises an Exception if the file is neither or cannot be parsed.
    """
    # Quick probe: read the beginning of the file to inspect the format
    try:
        with open(filename, 'r') as file:
            preview = file.read(500).strip().lower()
    except Exception as e:
        raise Exception("Error, data must be in valid CSV or HTML format") from e

    # Check for HTML signature
    if '<table' in preview:
        try:
            return load_from_html(filename)
        except Exception as e:
            raise Exception("Error, data must be in valid CSV or HTML format") from e

    # Check if it behaves as a valid CSV (try loading via load_from_csv)
    # Exclude files known not to be CSV (like ARFF headers starting with '@')
    if not preview.startswith('@'):
        try:
            return load_from_csv(filename)
        except Exception:
            pass

    # If parsing as both HTML and CSV fails
    raise Exception("Error, data must be in valid CSV or HTML format")




def save_to_json(data: list[dict], filename: str) -> None:
    """
    Saves a dataset (list of dictionaries) into a JSON formatted file.
    Does not use any external libraries.
    """
    json_rows = []

    for row in data:
        row_pairs = []
        for key, val in row.items():
            # Format string values with quotes, numbers without quotes
            if isinstance(val, str):
                formatted_val = f'"{val}"'
            elif isinstance(val, (int, float)):
                formatted_val = str(val)
            else:
                formatted_val = f'"{str(val)}"'

            row_pairs.append(f'"{key}": {formatted_val}')

        # Combine into an object string: {"k1": v1, "k2": v2}
        row_string = "{" + ", ".join(row_pairs) + "}"
        json_rows.append(row_string)

    # Wrap the full array: [ {...}, {...} ]
    full_json_str = "[\n  " + ",\n  ".join(json_rows) + "\n]"

    with open(filename, 'w') as file:
        file.write(full_json_str)