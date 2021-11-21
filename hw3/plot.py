import matplotlib.pyplot as plt

def visualize(filename, xvalues, yvalues, title='figure', xlabel='x_label', ylabel='y_label'):
    """
        Helper functions for analysis
        Draws plot then save as image
    """
    plt.figure()
    plt.scatter(xvalues, yvalues)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    ### TODO: WRITE YOUR CODE HERE. ############################################
    xs, ys = [10,20,50,100,200,500], [1333.9,1488.87,1599.64,1691.64,1814.55,2094.77]
    visualize('plot22.png', xs, ys, "beta = 0.02, delta = 0.6", "Number of initial active nodes", "Number of recovered nodes") # Example
    ############################################################################