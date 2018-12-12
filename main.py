

file_small = "small.txt"
file_large = "large.txt"


def read_file(file):
    """This function reads the file and saves the data."""

    with open(file) as data_set:
        for line in data_set:
            arr = line.split()
            for num in arr:
                print(float(num))


if __name__ == "__main__":
    print("Welcome to Jessica Gonzalez's Feature Selection Algorithm.")
    file_name = input("Type in the name of the file to test: ")
    read_file(file_name)

