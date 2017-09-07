""" Perceptron Learning Algorithm """

import numpy as np
import matplotlib.pyplot as plt

sign = lambda x: x and (1, -1)[x < 0]

# data should be [[[1, 2, 3, 4], 1],[[5, 6, 7, 8], -1], ...]
def run_pla(data):
    """ try to get hypothesis """
    hypo = np.array(data[0][0])
    print "init h " + str(hypo)
    has_wrong = True
    while has_wrong:
        has_wrong = False
        for datum in data:
            if sign(np.dot(hypo, datum[0])) != sign(datum[1]):
                if len(datum[0]) == 2:
                    draw_data(USER_DATA, hypo)
                has_wrong = True
                hypo = hypo + sign(datum[1]) * np.array(datum[0])

    return hypo

def draw_data(data, line = []):
    # y=-ax/b
    data_x1 = np.array([x[0][0] for x in data])
    data_x2 = np.array([x[0][1] for x in data])
    data_y = np.array([y[1] for y in data])
    max_x1 = data_x1.max()+2
    min_x1 = data_x1.min()-2
    max_x2 = data_x2.max()+2
    min_x2 = data_x2.min()-2
    line_a = line[0]
    line_b = line[1]
    line_min = -line_a*min_x1/line_b
    line_max = -line_a*max_x1/line_b

    plt.plot([min_x1, max_x1], [line_min, line_max])
    plt.axis([min_x1, max_x1, min_x2, max_x2])
    plt.scatter(data_x1[data_y > 0], data_x2[data_y > 0], c='r', marker='o')
    plt.scatter(data_x1[data_y < 0], data_x2[data_y < 0], c='b', marker='^')
    plt.show()

USER_DATA = [
        [[-3, 3, 3], 1],
        [[1, 2, 1], 1],
        [[-3, -4, -5], -1],
        [[3, 2, 7], 1],
        [[5, 3, 8], 1],
        [[2, -4, -2], -1],
        [[1, 8, 2], 1],
        [[-5, -3, -1], -1],
        [[7, 2, 5], 1],
        [[-1, -5, -3], -1]]
        
hypo_g = run_pla(USER_DATA)
print hypo_g
if len(hypo_g) == 2:
    draw_data(USER_DATA, hypo_g)
