import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        # compute the dot product of the stored weight vector and the given input and return an nn.DotProduct object
        return nn.DotProduct(self.w, x)

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        # convert a scalar Node into a Python floating-point number
        predicted = nn.as_scalar(self.run(x))
        # return 1 if the dot product is non-negative or -1 otherwise
        if predicted >= 0:
            return 1
        else:
            return -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        # use a flag for iteration
        learning = True
        batchSize = 1
        while learning:
            # set the flag to exit the loop
            learning = False
            for x, y in dataset.iterate_once(batchSize):
                if self.get_prediction(x) != nn.as_scalar(y):
                    # set the flag to stay in the loop
                    learning = True
                    # change the value of the parameter
                    self.w.update(nn.as_scalar(y), x)
            
        
        
class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.w1 = nn.Parameter(1, 15)
        self.b1 = nn.Parameter(1, 15)
        self.w2 = nn.Parameter(15, 10)
        self.b2 = nn.Parameter(1, 10)
        self.w3 = nn.Parameter(10, 1)
        self.b3 = nn.Parameter(1, 1)
        self.batchSize = 10
        self.learningRate = 0.002
        # for the update() function, we change the sign of the multiplier to ensure gradient updates
        # are performed in correct direction to ensure gradient descent
        self.directionNumber = - self.learningRate

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        # apply the function f(x) = relu( relu(x * W1 + b1) * W2 + b2) * W3 + b3
        # to build a simple neural network for mapping an input row vector x to an output vector
        firstLayer = nn.AddBias(nn.Linear(x, self.w1), self.b1)
        secondLayer = nn.AddBias(nn.Linear(nn.ReLU(firstLayer), self.w2), self.b2)
        thirdLayer = nn.AddBias(nn.Linear(nn.ReLU(secondLayer), self.w3), self.b3)
        return thirdLayer

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SquareLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        # use flag for the loop
        Flag = True
        while Flag:
            # set the flag to exit the loop
            Flag = False
            for x, y in dataset.iterate_once(self.batchSize):
                grad_wrt = nn.gradients([self.w1, self.b1, self.w2, self.b2, self.w3, self.b3], self.get_loss(x, y))
                # use the changed sign of the multiplier in the update() function
                self.w1.update(self.directionNumber, grad_wrt[0])
                self.b1.update(self.directionNumber, grad_wrt[1])
                self.w2.update(self.directionNumber, grad_wrt[2])
                self.b2.update(self.directionNumber, grad_wrt[3])
                self.w3.update(self.directionNumber, grad_wrt[4])
                self.b3.update(self.directionNumber, grad_wrt[5])
                if nn.as_scalar(self.get_loss(x, y)) >= 0.02:
                    # if each loss is not smaller than 0.02, set the flag to stay in the loop
                    Flag = True
        

class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.w1 = nn.Parameter(784, 392)
        self.b1 = nn.Parameter(1, 392)
        self.w2 = nn.Parameter(392, 196)
        self.b2 = nn.Parameter(1, 196)
        self.w3 = nn.Parameter(196, 98)
        self.b3 = nn.Parameter(1, 98)
        self.w4 = nn.Parameter(98, 49)
        self.b4 = nn.Parameter(1, 49)
        self.w5 = nn.Parameter(49, 10)
        self.b5 = nn.Parameter(1, 10)
        self.batchSize = 100
        self.learningRate = 0.15
        # for the update() function, we change the sign of the multiplier to ensure gradient updates
        # are performed in correct direction to ensure gradient descent
        self.directionNumber = - self.learningRate

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        # apply the function f(x) = relu( relu(x * W1 + b1) * W2 + b2) * W3 + b3
        # to build a simple neural network for mapping an input row vector x to an output vector
        # Do not put a ReLU activation after the last layer of the network
        firstLayer = nn.AddBias(nn.Linear(nn.ReLU(x), self.w1), self.b1)
        secondLayer = nn.AddBias(nn.Linear(nn.ReLU(firstLayer), self.w2), self.b2)
        thirdLayer = nn.AddBias(nn.Linear(nn.ReLU(secondLayer), self.w3), self.b3)
        fourthLayer = nn.AddBias(nn.Linear(nn.ReLU(thirdLayer), self.w4), self.b4)
        fifthLayer = nn.AddBias(nn.Linear(fourthLayer, self.w5), self.b5)
        return fifthLayer

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SoftmaxLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        accuracy = 0
        # the model should achieve an accuracy of at least 98% on the test set
        while accuracy < 0.98:
            for x, y in dataset.iterate_once(self.batchSize):
                loss = self.get_loss(x, y)
                grad_wrt = nn.gradients([self.w1, self.b1, self.w2, self.b2, self.w3, self.b3, self.w4, self.b4, self.w5, self.b5], loss)
                for i in range(len([self.w1, self.b1, self.w2, self.b2, self.w3, self.b3, self.w4, self.b4, self.w5, self.b5])):
                    # use the changed sign of the multiplier in the update() function
                    [self.w1, self.b1, self.w2, self.b2, self.w3, self.b3, self.w4, self.b4, self.w5, self.b5][i].update(self.directionNumber, grad_wrt[i])
            # compute validation accuracy for the model and decide whether to stop training
            accuracy = dataset.get_validation_accuracy()
