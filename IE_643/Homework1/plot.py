import matplotlib.pyplot as plt

def plotline(w, theta, title='Data Plot', xlabel='x2', ylabel='x1'):
    x = [i for i in range(-5, 5)]
    y = [((w[0] * x + theta_i)/w[1]) * -1 for w, theta_i, x in zip(w, theta, x)]
    plt.plot(x, y, label='Line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
