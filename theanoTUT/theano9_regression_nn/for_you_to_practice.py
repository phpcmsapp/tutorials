# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

# 9 - regression example
"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import theano
import theano.tensor as T
import numpy as np
import matplotlib.pyplot as plt


class Layer(object):
    def __init__(self, inputs, in_size, out_size, activation_function=None):
        self.W = theano.shared(np.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(np.zeros((out_size, )) + 0.1)
        self.Wx_plus_b = T.dot(inputs, self.W) + self.b
        self.activation_function = activation_function
        if activation_function is None:
            self.outputs = self.Wx_plus_b
        else:
            self.outputs = self.activation_function(self.Wx_plus_b)


# Make up some fake data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise        # y = x^2 - 0.5

# show the fake data
plt.scatter(x_data, y_data)
plt.show()

# determine the inputs dtype


# add layers


# compute the cost


# compute the gradients


# apply gradient descent


# prediction


for i in range(1000):
    # training

    if i % 50 == 0:
        pass