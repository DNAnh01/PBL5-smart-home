import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./CNN/imagesData/face.jpg')
# chuyển kích thức img thành khung hình vuông
img = cv2.resize(img, (1200, 1200))
# chuyển màu của img thành màu xám
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape) # (1200, 1200)

# convolution

class Conv2d:
    def __init__(self, input, kernelSize):
        self.input = input
        # kích cỡ của img
        self.height, self.width = input.shape
        self.kernel = np.random.randn(kernelSize, kernelSize)
        # print(kernel)
        '''
        [[ 0.23512125 -0.68516903 -0.5429533 ]
        [-0.00981667 -0.42392471  1.04781965]
        [-1.27972119 -0.23502826  1.29476504]]
        '''
        self.results = np.zeros((self.height - kernelSize + 1, self.width - kernelSize + 1))
        # roi -> region of interesting 
    def getROI(self):
        """
        tìm vùng dữ liệu quan tâm
        """
        for row in range(0, self.height - self.kernel.shape[0] + 1):
            for column in range(0, self.width - self.kernel.shape[1] + 1):
                roi = self.input[row: row + self.kernel.shape[0], column: column + self.kernel.shape[1]]
                yield row, column, roi

    def operate(self):
        for row, column, roi in self.getROI():
            self.results[row, column] = np.sum(roi * self.kernel)

        return self.results

conv2d = Conv2d(img_gray, 5)

img_gray_conv2d = conv2d.operate()
plt.imshow(img_gray_conv2d, cmap='gray')
plt.show()
