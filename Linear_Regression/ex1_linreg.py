import numpy as np
from sklearn.linear_model import LinearRegression


def load_data(path):
    with open(path) as f:
        data = [list(map(float, i.strip().split())) for i in f.readlines()]
    data_array = np.array(data)
    m_, n_ = data_array.shape
    extra_ones = np.ones((m_, 1))
    data_array = np.append(extra_ones, data_array, axis=1)
    train_x = data_array[:int(m_ * 2 / 3), :14]
    train_y = data_array[:int(m_ * 2 / 3), [14]]
    test_x = data_array[int(m_ * 2 / 3):, :14]
    test_y = data_array[int(m_ * 2 / 3):, [14]]
    return train_x, test_x, train_y, test_y, m_, n_ + 1


def train_with_sklearn(train_x, train_y):
    linreg = LinearRegression(fit_intercept=False)
    linreg.fit(train_x, train_y)
    return linreg.coef_


def train(train_x, train_y, alpha,epoch):
    m_, n_ = train_x.shape
    theta = np.zeros((n_, 1))
    cost_data = [cost(theta, train_x, train_y)]
    count = 0
    while True:
        predicted_y = np.dot(train_x, theta)
        loss = predicted_y - train_y
        # old_theta = theta
        theta = theta - alpha * (np.dot(loss.T, train_x)).T/m_
        count += 1
        cost_data.append(cost(theta, train_x, train_y))
        if count % epoch == 0:
            return theta, cost_data

def train_stochastic(train_x, train_y, alpha, epoch):
    m_, n_ = train_x.shape
    theta = np.zeros((n_, 1))
    cost_data = [cost(theta, train_x, train_y)]
    count = 0
    while True:
        for i in range(m_):
            predicted_y = np.dot(train_x[i], theta)
            loss = np.asscalar(predicted_y - train_y[i])
            # old_theta = theta
            theta = theta - alpha * loss * train_x[i].reshape((14,1))/m_
        count += 1
        cost_data.append(cost(theta,train_x,train_y))
        if count % epoch == 0:
            return theta, cost_data

def cost(theata,X,Y):
    loss = np.dot(X, theata) - Y
    m = X.shape[0]
    cost = 1/(2 * m ) * np.sum(np.square(loss))
    return cost


if __name__ == "__main__":
    file_path = "/home/selwb/Document/Machine_learning/UFLDL/stanford_dl_ex-master/ex1/housing.data"
    train_X, test_X, train_Y, test_Y, m, n = load_data(file_path)
    theta ,cost_sto= train_stochastic(train_X, train_Y, 0.0001, 100000)
    # sk_theta = np.array(train_with_sklearn(train_X, train_Y)).T
    #
    # loss1 = np.dot(test_X, sk_theta) - test_Y
    # print(loss1)
