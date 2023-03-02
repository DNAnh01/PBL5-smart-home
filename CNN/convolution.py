import cv2
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(5) # The random times will produce the same number

img = cv2.imread('./CNN/imagesData/face.jpg')
img = cv2.resize(img, (1200, 1200))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255 # Convert to gray and normalization
# print(img_gray.shape) # (1200, 1200)
print(img_gray)
# convolution

class Conv2d:
    def __init__(self, input, kernelSize, padding=0, stride=1):
        self.input = np.pad(input, ((padding, padding), (padding, padding)), 'constant') # Conv's own input
        self.stride = stride 
        self.kernel = np.random.randn(kernelSize, kernelSize)
        # print(self.kernel)
        '''
        [[ 0.44122749 -0.33087015  2.43077119]
        [-0.25209213  0.10960984  1.58248112]
        [-0.9092324  -0.59163666  0.18760323]]
        '''
        self.results = np.zeros((int((self.input.shape[0] - self.kernel.shape[0])/self.stride) + 1,
                                 int((self.input.shape[1] - self.kernel.shape[1])/self.stride) + 1))

    def getROI(self):
        """
        Region Of Interesting
        """
        for row in range(int((self.input.shape[0] - self.kernel.shape[0])/self.stride) + 1):
            for column in range(int((self.input.shape[1] - self.kernel.shape[1])/self.stride) + 1):
                roi = self.input[row*self.stride: row*self.stride + self.kernel.shape[0],
                                 column*self.stride: column*self.stride + self.kernel.shape[1]]
                yield row, column, roi

    def operate(self):
        for row, column, roi in self.getROI():
            self.results[row, column] = np.sum(roi * self.kernel)
        return self.results

class ReLU:
    def __init__(self, input):
        self.input = input
        self.result = np.zeros((self.input.shape[0], self.input.shape[1]))

    def operate(self):
        for row in range(self.input.shape[0]):
            for column in range(self.input.shape[1]):
                self.result[row, column] = 0 if self.input[row, column] < 0 else self.input[row, column]
        return self.result
    
class LeakyReLU:
    def __init__(self, input):
        self.input = input
        self.result = np.zeros((self.input.shape[0], self.input.shape[1]))

    def operate(self):
        for row in range(self.input.shape[0]):
            for column in range(self.input.shape[1]):
                self.result[row, column] = 0.1*self.input[row, column] if self.input[row, column] < 0 else self.input[row, column]
        return self.result

fig = plt.figure(figsize=(12, 12))
for i in range(1, 10):
    conv2d = Conv2d(input=img_gray,kernelSize= 3, padding=2, stride=i)
    img_gray_conv2d = conv2d.operate()
    conv2d_relu = ReLU(input=img_gray_conv2d)
    img_gray_conv2d_relu = conv2d_relu.operate()

    plt.subplot(3, 3, i)
    plt.imshow(img_gray_conv2d_relu, cmap='gray')
    plt.axis('off')

plt.show()
