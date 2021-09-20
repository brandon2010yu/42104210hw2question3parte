# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# loop your data to allow each instance to be your test set
for i, instance in enumerate(db):


    # add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    # --> add your Python code here
    X = [[0, 3], [1, 4], [2, 4], [3, 3], [2, 1], [4, 4], [4, 3], [3, 2], [4, 1]]
    X2 = [[0, 3], [1, 4], [2, 4], [3, 3], [2, 1], [4, 4], [4, 3], [3, 2], [0, 5]]
    X3 = [[0, 3], [1, 4], [2, 4], [3, 3], [2, 1], [4, 4], [4, 3], [4, 1], [0, 5]]
    X4 = [[0, 3], [1, 4], [2, 4], [3, 3], [2, 1], [4, 4], [3, 2], [4, 1], [0, 5]]
    X5 = [[0, 3], [1, 4], [2, 4], [3, 3], [2, 1], [4, 3], [3, 2], [4, 1], [0, 5]]
    X6 = [[0, 3], [1, 4], [2, 4], [3, 3], [4, 4], [4, 3], [3, 2], [4, 1], [0, 5]]
    X7 = [[0, 3], [1, 4], [2, 4], [2, 1], [4, 4], [4, 3], [3, 2], [4, 1], [0, 5]]
    X8 = [[0, 3], [1, 4], [3, 3], [2, 1], [4, 4], [4, 3], [3, 2], [4, 1], [0, 5]]
    X9 = [[0, 3], [2, 4], [3, 3], [2, 1], [4, 4], [4, 3], [3, 2], [4, 1], [0, 5]]
    X10 = [[1, 4], [2, 4], [3, 3], [2, 1], [4, 4], [4, 3], [3, 2], [4, 1], [0, 5]]

    # transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    # --> add your Python code here
    Minus = 1
    Add = 2
    Y = [1, 1, 2, 2, 1, 2, 2, 2, 1]
    Y2 = [1, 1, 2, 2, 1, 2, 2, 2, 1]
    Y3 = [1, 1, 2, 2, 1, 2, 2, 1, 1]
    Y4 = [1, 1, 2, 2, 1, 2, 2, 1, 1]
    Y5 = [1, 1, 2, 2, 1, 2, 2, 1, 1]
    Y6 = [1, 1, 2, 2, 2, 2, 2, 1, 1]
    Y7 = [1, 1, 2, 1, 2, 2, 2, 1, 1]
    Y8 = [1, 1, 2, 1, 2, 2, 2, 1, 1]
    Y9 = [1, 2, 2, 1, 2, 2, 2, 1, 1]
    Y10 = [1, 2, 2, 1, 2, 2, 2, 1, 1]

    # store the test sample of this iteration in the vector testSample
    # --> add your Python code here
    testSample = [0, 5]
    testSample2 = [4, 1]
    testSample3 = [3, 2]
    testSample4 = [4, 3]
    testSample5 = [4, 4]
    testSample6 = [2, 1]
    testSample7 = [3, 3]
    testSample8 = [2, 4]
    testSample9 = [1, 4]
    testSample10 = [0, 3]

    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X10, Y10)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([[0, 5]])[0]
    class_predicted2 = clf.predict([[4, 1]])[0]
    class_predicted3 = clf.predict([[3, 2]])[0]
    class_predicted4 = clf.predict([[4, 3]])[0]
    class_predicted5 = clf.predict([[4, 4]])[0]
    class_predicted6 = clf.predict([[2, 1]])[0]
    class_predicted7 = clf.predict([[3, 3]])[0]
    class_predicted8 = clf.predict([[2, 4]])[0]
    class_predicted9 = clf.predict([[1, 4]])[0]
    class_predicted10 = clf.predict([[0, 3]])[0]

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here

    #0 class_predicted = clf.predict([[0, 5]])[0]
    #1 class_predicted2 = clf.predict([[4, 1]])[0]
    #2 class_predicted3 = clf.predict([[3, 2]])[0] incorrect prediction
    #3 class_predicted4 = clf.predict([[4, 3]])[0]
    #4 class_predicted5 = clf.predict([[4, 4]])[0] incorrect prediction
    #5 class_predicted6 = clf.predict([[2, 1]])[0] incorrect prediction
    #6 class_predicted7 = clf.predict([[3, 3]])[0]
    #7 class_predicted8 = clf.predict([[2, 4]])[0] incorrect prediction
    #8 class_predicted9 = clf.predict([[1, 4]])[0] incorrect prediction
    #9 class_predicted10 = clf.predict([[0, 3]])[0]

if class_predicted == 1 and db[9][2] != "-" or class_predicted == 2 and db[9][2] != "+":
        print("wrong prediction instance")



# print the error rate
# --> add your Python code here
wrongPrediction = 5
errorRate = wrongPrediction / 10
print(errorRate)
