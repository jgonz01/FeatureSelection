from math import sqrt
import random

arr_data = []
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


def nearest_neighbor_loocv(subset):
    """This function finds the nearest neighbor and returns leave one out cross validation error."""

    subset_list = list(subset)
    total_correct = 0
    for i in range(len(arr_data)):
        shortest_distance = 9999999999999999999999.0
        shortest_index = -1
        for j in range(len(arr_data)):
            if j == i:
                continue
            dist = 0
            for feature in subset_list:
                dist += pow(arr_data[i][feature] - arr_data[j][feature], 2)
            dist = sqrt(dist)
            if dist < shortest_distance:
                shortest_distance = dist
                shortest_index = j
        if arr_data[i][0] == arr_data[shortest_index][0]:
            total_correct += 1

    return total_correct/num_instances


def forward():
    """This function handles forward selection."""

    subset = set()  # saves parent set
    best_accuracy = 0.0
    best_subset = set()  # saves best set
    for i in range(1, len(arr_data[0])):
        # print('Level: '+ str(i))
        accuracy = 0.0
        best_set = set()  # saves current best temp set
        for j in range(1, len(arr_data[0])):
            temp_set = subset.copy()  # saves set to test
            temp_set.add(j)
            if subset == temp_set:
                continue
            calc_accuracy = nearest_neighbor_loocv(temp_set)
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


def backward():
    """This function handles backward selection."""

    subset = set()  # saves parent set
    for i in range(num_features):
        subset.add(i+1)

    best_accuracy = nearest_neighbor_loocv(subset)  # saves best accuracy
    best_subset = subset.copy()  # saves best set
    print('\tUsing feature(s) ' + str(best_subset) + ' accuracy is ' + str(best_accuracy * 100) + '%')
    print('\nFeature set ' + str(best_subset) + ' was best, accuracy is ' + str(best_accuracy * 100) + '%\n')
    for i in range(1, len(arr_data[0])-1):
        # print('Level: '+str(i))
        accuracy = 0.0
        best_set = set()  # saves current best temp set
        for j in range(1, len(arr_data[0])):
            temp_set = subset.copy() - set([j])  # saves set to test
            if subset == temp_set:
                continue
            calc_accuracy = nearest_neighbor_loocv(temp_set)
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


def my_algorithm():
    """This algorithm is like forward selection except it deletes random data."""

    data_delete = random.sample(range(0, 200), 50)
    data_delete.sort()
    # Delete data
    for index in reversed(data_delete):
        del arr_data[index]

    subset = set()  # saves parent set
    best_accuracy = 0.0
    best_subset = set()  # saves best set
    for i in range(1, len(arr_data[0])):
        print('Level: '+ str(i))
        accuracy = 0.0
        best_set = set()  # saves current best temp set
        for j in range(1, len(arr_data[0])):
            temp_set = subset.copy()  # saves set to test
            temp_set.add(j)
            if subset == temp_set:
                continue
            calc_accuracy = nearest_neighbor_loocv(temp_set)
            if calc_accuracy > accuracy:
                accuracy = calc_accuracy
                best_set = temp_set.copy()
        subset = best_set.copy()
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_subset = subset.copy()

    print('Finished search!! The best feature subset is ' + str(best_subset) + ', which has an accuracy of '
          + str(best_accuracy * 100) + '%')


if __name__ == "__main__":

    print("Welcome to Jessica Gonzalez's Feature Selection Algorithm.")
    file_name = input("Type in the name of the file to test: ")
    algorithm = input("Type the number of the algorithm you want to run.\n"
                      "1) Forward Selection\n"
                      "2) Backward Selection\n"
                      "3) Jessica's Special Algorithm\n")

    read_file(file_name)

    # # Delete {8, 2} for small set
    # for data in arr_data:
    #     del data[8]
    #     del data[2]

    # # Delete {1, 3} for large set
    # for data in arr_data:
    #     del data[3]
    #     del data[1]

    num_instances = len(arr_data)
    num_features = len(arr_data[0]) - 1

    print('\nThis dataset has ' + str(num_features) + ' features (not including the class attribute)'
                                                    ' with ' + str(num_instances) + ' instances.\n')
    print('Beginning search.\n')

    if algorithm == '1':
        forward()
    elif algorithm == '2':
        backward()
    elif algorithm == '3':
        my_algorithm()


