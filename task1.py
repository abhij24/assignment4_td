try:
    file = open('sample.txt', 'r+')
    reading_file1 = file.readline()
    reading_file2 = file.readline()
    print("Reading file content:")
    print(f"Line 1: {reading_file1}")
    print(f"Line 2: {reading_file2}")
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")