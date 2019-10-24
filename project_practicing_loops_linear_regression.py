"""This project is implementing a version of Linear Regression in Python. The program is running an experiment to bounce different sizes of balls, and fitting lines to the data points. This algorithm minimizes the error (the distance from each point to the line), and finds the best fit when given a set of data."""

#Using the equation of straight line : y = m*x + b, when m is the slope of the line and b is the intercept, where the line crosses the y-axis.
def get_y(m, b, x):
  y = m*x + b
  return y

#tests:

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# Trying different m values and b values to see which line produces the least error. 
#This function returns the distance between the line and the point.
def calculate_error(m,b,point):
    x_point = point[0]
    y_point = point[1]
    y_from_get_y = get_y(m,b,x_point)
    difference = y_from_get_y - y_point
    return abs(difference)

#tests:

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))

#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))

#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))

#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


#The experiment is comparing the width of bouncy balls to how high they bounce.

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
#The first datapoint, (1, 2), means that 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.


# This function iterates through each `point` in `points` and calculates the error from that point to the line (calling the function `calculate_error`). 
def calculate_all_error(m,b,points):
    running_total = 0
    for point in points:
        running_total = calculate_error(m,b,point)
    return running_total

#tests:    

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))


# So far the program calculates how much error a line produces when we try to fit it to the data.

# From this point, we would like to find the m and b that minimizes this error, and thus fits the data best.

# By trial and error, the program checks different slopes (m values) and  different intercepts (b values) and sees which one produces the smallest error value for the dataset.

#Using list comprehension, this list goes from -10 to 10 inclusive, in increments of 0.1.
possible_ms = [m*0.1 for m in range(-100,101)]
#Using list comprehension, this list goes from -20 to 20 inclusive, in steps of 0.1.
possible_bs = [b*0.1 for b in range(-200,201)]


#The following varivable should start at infinity so that any error we get at first will be smaller than our value.
smallest_error = float("inf")
best_m = 0
best_b = 0

# In order to find the smallest error, the following loop will make every possible y = m*x + b line by pairing all of the possible ms with all of the possible bs. Then, we will see which line produces the smallest total error with the set of data stored in datapoins.
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m,b,datapoints) < smallest_error:
            best_m = m
            best_b = b
            smallest_error = calculate_all_error(m,b,datapoints)
print (best_m)
print (best_b)
print (smallest_error)

#test:

#the line that fits the data best has an m of 0.3 and a b of 1.7: y = 0.3x + 1.7 .This line produced a total error of 5.
#The line's prediction for the bounce height of a ball with a width of 6 is:

#should print 3.5 (meters)
print (get_y(0.3,1.7,6))


