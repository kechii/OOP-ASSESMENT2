import csv  # imported this for dealing with CSV files

def read_grades(filename):
    grades = []  # Empty list to store the grades
    try:
        # open and read the file
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    # Convert the grade to a float and add it to the list
                    grade = float(row['overall_grade'])
                    grades.append(grade)
                except ValueError:
                    # messed up entering the grades
                    print(f"Warning: Invalid grade for student {row['student_name']}: {row['overall_grade']}")
    except FileNotFoundError:
        #  file's missing
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        # touchie the file
        print(f"Error: Permission denied to read file '{filename}'.")
    except csv.Error as e:
        # CSV bonkers
        print(f"Error reading CSV file: {e}")
    except Exception as e:
        # Catch-all for unexpected errors happening
        print(f"An unexpected error occurred while reading the file: {e}")
    
    return grades  # grades we managed to get

def calculate_average(grades):
    if not grades:
        return 0  # Can't divide by zero, duh
    return sum(grades) / len(grades)  # Add 'em up and divide

def write_result(filename, average):
    try:
        # Try to write the result to a file
        with open(filename, 'w') as file:
            file.write(f"The average grade is: {average:.2f}")
        print(f"Result successfully written to {filename}")
    except PermissionError:
        print(f"Error: Permission denied to write to file '{filename}'.")
    except Exception as e:
        # Something else went wrong
        print(f"An unexpected error occurred while writing the result: {e}")

def main():
    input_file = "1731.txt"  # Our input file
    output_file = "average_grade.txt"  #  saves the result
    
    grades = read_grades(input_file)  # Get them grades
    
    if grades:
        average = calculate_average(grades)  # making the calculation
        write_result(output_file, average)  # Save the result
    else:
        print("No valid grades found. Cannot calculate average.")  # incase no grades to work with


if __name__ == "__main__":
    main()