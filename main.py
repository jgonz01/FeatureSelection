

arr_data = []
features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_instances = None
num_features = None


def read_file(file):
    """This function reads the file and saves the data to a 2d array."""

    global arr_data

    with open(file) as data_set:
        for line in data_set:
            arr = line.split()
            arr_tmp = []
            for num in arr:
                arr_tmp.append(float(num))
            arr_data.append(arr_tmp)


def nearest_neighbor(subset):
    """This function returns how many instances were guessed correctly."""

    subset_list = list(subset)
    for instance in arr_data:
        shortest_distance = 9999999999999999999999.0
        for feature in subset_list:
            distance +=

def forward():
    """This function handles forward selection."""

    subset = set()
    best = None
    for i in range(1, len(arr_data[0])):
        print(i)
        for j in range(1, len(arr_data[0])):
            #accuracy = 0.0
            subset = subset & set([j])
            nearest_neighbor(subset)
            #print('set: ' + str(subset))


if __name__ == "__main__":

    print("Welcome to Jessica Gonzalez's Feature Selection Algorithm.")
    file_name = input("Type in the name of the file to test: ")
    algorithm = input("Type the number of the algorithm you want to run.\n"
                      "1) Forward Selection\n"
                      "2) Backward Selection\n"
                      "3) Jessica's Special Algorithm\n")

    read_file(file_name)
    num_instances = len(arr_data)
    num_features = len(arr_data[0]) - 1

    forward()

    if algorithm == '1':
        print('1')
    elif algorithm == '2':
        print("2")
    elif algorithm == '3':
        print("3")


