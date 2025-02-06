import pandas as pd

# Input and output file paths
input_file = "dataset/01-Student-course-mapping.csv"
output_file = "dataset/01-Student-course-mapping_clean.csv"

rows = []

# Open and read the file as text
with open(input_file, "r") as f:
    lines = f.readlines()

# The first line is the header. In your file it reads:
# STUDENT_ID|TERM|COURSE|STUDENT
# But the data rows only contain 2 fields (STUDENT_ID and a composite field).
header = lines[0].strip().split("|")
# We will use our own column names for the cleaned file.
clean_columns = ["STUDENT_ID", "TERM", "COURSE", "STUDENT"]

# Process each subsequent line
for line in lines[1:]:
    line = line.strip()
    if not line:
        continue  # skip empty lines

    # Split by the pipe delimiter.
    parts = line.split("|")
    if len(parts) < 2:
        continue  # skip malformed lines

    student_id = parts[0].strip()
    # Remove leading/trailing quotes from the composite field.
    composite_field = parts[1].strip().strip("'\"")

    # A row may contain multiple composite entries separated by commas.
    composite_entries = composite_field.split(",")
    for composite in composite_entries:
        composite = composite.strip()
        # Split the composite entry by period.
        # Expected parts: [TERM, COURSE_PART1, COURSE_PART2, STUDENT]
        items = composite.split(".")
        if len(items) == 4:
            term = items[0].strip()
            course = items[1].strip() + "." + items[2].strip()
            student = items[3].strip()
            rows.append([student_id, term, course, student])
        else:
            # If the composite entry doesn't have exactly 4 parts,
            # you might log or handle the error.
            print(f"Skipping malformed composite entry: {composite}")

# Create a new DataFrame from the cleaned rows.
df_clean = pd.DataFrame(rows, columns=clean_columns)

# Optionally inspect the DataFrame
print(df_clean.head())

# Write out a cleaned CSV file (comma separated by default)
df_clean.to_csv(output_file, index=False)
