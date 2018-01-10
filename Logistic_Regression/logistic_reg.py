#-*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LogisticRegression


def sigmod(x):
    result = 1/np.float64(1+np.exp(-x))
    return np.float64(result)

def logstic_gradient_batch(train_x, train_y, epoch=1000, alpha=0.001):
    train_x = train_x.astype(np.float64)
    train_y = train_y.astype(np.float64)
    theta = np.ones((train_x.shape[1], 1), dtype=np.float64)

    for i in range(epoch):
        loss = train_y - np.exp(np.dot(train_x, theta)) / sigmod(np.dot(train_x, theta))
        theta = theta + alpha * np.dot(train_x.T, loss)
    return theta


def logstic_gradient_sto(train_x, train_y, epoch=1000, alpha=0.001):
    train_x = train_x.astype(np.float64)
    train_y = train_y.astype(np.float64)
    theta = np.ones((train_x.shape[1], 1), dtype=np.float64)

    # for m in range(epoch):
    #     for i in range(train_x.shape[0]):
    #         loss =  train_y[i] - np.exp(np.dot(train_x[i], theta)) / sigmod(np.dot(train_x[i], theta))
    #         theta = theta + alpha * np.dot(train_x[i], loss.reshape(-1, 1))
    return theta


def logistic_sk(train_x, train_y):
    lr = LogisticRegression(fit_intercept=False)
    lr.fit(train_x, train_y)
    return lr.coef_

if __name__ == '__main__':

    a1 = np.array([1,2,3]).reshape(3, 1)
    b1 = np.array([1,0,1]).reshape(-1, 1)
    print(logstic_gradient_sto(a1, b1))