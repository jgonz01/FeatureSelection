from math import sqrt

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
    total_correct = 0
    for i in range(len(arr_data)):
        #print('i: ' + str(i))
        shortest_distance = 9999999999999999999999.0
        shortest_index = -1
        for j in range(len(arr_data)):
            if j == i:
                continue
            #print('j: ' + str(j))
            dist = 0
            for feature in subset_list:
                dist += pow(arr_data[i][feature] - arr_data[j][feature], 2)
                #print('feature: ' + str(feature) + ' dist: '+ str(dist))
            dist = sqrt(dist)
            if dist < shortest_distance:
                shortest_distance = dist
                shortest_index = j
        #print(str(arr_data[i][0]) + ' and ' + str(arr_data[shortest_index][0]))
        if arr_data[i][0] == arr_data[shortest_index][0]:
            total_correct += 1

    return total_correct/num_instances


def forward():
    """This function handles forward selection."""

    subset = set()
    best_accuracy = 0.0
    best_subset = set()
    for i in range(1, len(arr_data[0])):
        #print('i: ' + str(i))
        accuracy = 0.0
        best_set = set()
        for j in range(1, len(arr_data[0])):
            #print('j: ' + str(j))
            temp_set = subset.copy()
            temp_set.add(j)
            if subset == temp_set:
                continue
            calc_accuracy = nearest_neighbor(temp_set)
            print('\tUsing feature(s) ' + str(temp_set) + ' accuracy is ' + str(calc_accuracy*100) + '%')
            if calc_accuracy > accuracy:
                accuracy = calc_accuracy
                best_set = temp_set.copy()
        subset = best_set.copy()
        if accuracy > best_accuracy:
            print('\nFeature set ' + str(subset) + ' was best, accuracy is ' + str(accuracy * 100) + '%\n')
            best_accuracy = accuracy
            best_subset = subset.copy()
        else:
            print('\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)\n'
                  'Feature set ' + str(subset) + ' was best, accuracy is ' + str(accuracy*100) + '%\n')

    print('Finished search!! The best feature subset is ' + str(best_subset) + ', which has an accuracy of '
          + str(best_accuracy*100) + '%')


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

    print('\nThis dataset has ' + str(num_features) + ' features (not including the class attribute)'
                                                    ' with ' + str(num_instances) + ' instances.\n')

    if algorithm == '1':
        print('Beginning search.\n')
        forward()
    # elif algorithm == '2':
    #     #print("2")
    # elif algorithm == '3':
    #     #print("3")


