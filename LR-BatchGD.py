import numpy as np

def hypothesis(b1, b2, x):
    predicted_y = (b1 + (b2 * x))
    return predicted_y

def gradient_descent(b1, b2, data, alpha, iterate):
    partial_b1 = partial_b2 = 0
    new_b1 = b1
    new_b2 = b2
    for convergence in range(iterate):
        for i in range(len(data)):
            x = float(data[i, 0])
            y = float(data[i, 1])
            partial_b1 += (1 / float(len(data))) * (hypothesis(new_b1, new_b2, x) - y)
            partial_b2 += (1 / float(len(data))) * (hypothesis(new_b1, new_b2, x) - y) * x
        new_b1 = (b1 - (alpha * partial_b1))
        new_b2 = (b2 - (alpha * partial_b2))
    return [new_b1, new_b2]


if __name__ == '__main__':
    b1 = b2 = 0
    alpha = 0.0008
    iterate = 1000
    data = np.genfromtxt('LinearRegression.csv', delimiter=',')
    [new_b1, new_b2] = gradient_descent(b1, b2, np.asarray(data), alpha, iterate)
    x = float(input("Enter X value to predict : "))
    y = hypothesis(new_b1, new_b2, x)
    print('\nPredicted Y value is : {}'.format(y))

    print("\nB1 and B2 are \nb1:{} \nb2:{}".format(new_b1, new_b2))

