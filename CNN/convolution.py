import cv2
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)  # The random times will produce the same number

img = cv2.imread('./CNN/imagesData/face.jpg')
img = cv2.resize(img, (1200, 1200))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/255  # Convert to gray and normalization
# print(img_gray.shape) # (1200, 1200)
# print(img_gray)
# print(img.shape) # (1200, 1200, 3)
'''
    Đối vs img thì parameter số lượng layer nằm ở đằng sau
    Còn đối vs np.array thì parameter số lượng layer nằm ở đằng trc
'''
# Convolution


class Conv2d:
    def __init__(self, input, numberOfKernel=8, kernelSize=3, padding=0, stride=1):
        # Conv's own input
        self.input = np.pad(input, ((padding, padding), (padding, padding)), 'constant')
        self.stride = stride
        '''
            self.kernel  bản chất như np.array thì parameter số lượng layer nằm ở đằng trc
        '''
        self.kernel = np.random.randn(numberOfKernel, kernelSize, kernelSize)
        # print(self.kernel)
        '''
        [[ 0.44122749 -0.33087015  2.43077119]
        [-0.25209213  0.10960984  1.58248112]
        [-0.9092324  -0.59163666  0.18760323]]
        '''
        # print(self.kernel.shape) # (8, 3, 3)

        '''
            self.results bản chất cũng là những chỉ số dữ liệu của tấm hình nên parameter số lượng 
            layer phải nằm ở đằng sau
        '''
        self.results = np.zeros((int((self.input.shape[0] - self.kernel.shape[1])/self.stride) + 1,
                                 int((self.input.shape[1] - self.kernel.shape[2])/self.stride) + 1,
                                 self.kernel.shape[0]))

    def getROI(self):
        '''
            Region Of Interesting
            Hàm này dựa trên tấm hình và chọn ra vùng để tính toán
        '''
        for row in range(int((self.input.shape[0] - self.kernel.shape[1])/self.stride) + 1):
            for column in range(int((self.input.shape[1] - self.kernel.shape[2])/self.stride) + 1):
                roi = self.input[row*self.stride: row*self.stride + self.kernel.shape[1],
                                 column*self.stride: column*self.stride + self.kernel.shape[2]]
                yield row, column, roi

    def operate(self):
        '''
            Tính toán trên nhiều layer
        '''
        for layer in range(self.kernel.shape[0]):
            for row, column, roi in self.getROI():
                self.results[row, column, layer] = np.sum(roi * self.kernel[layer, :, :])
        return self.results


class ReLU:
    def __init__(self, input):
        '''
        input = result of convolution
        '''
        self.input = input
        self.result = np.zeros((self.input.shape[0],
                                self.input.shape[1],
                                self.input.shape[2]))

    def operate(self):
        for layer in range(self.input.shape[2]):
            for row in range(self.input.shape[0]):
                for column in range(self.input.shape[1]):
                    self.result[row, column, layer] = 0 if self.input[row, column, layer] < 0 else self.input[row, column, layer]
        return self.result


class LeakyReLU:
    def __init__(self, input):
        self.input = input
        self.result = np.zeros((self.input.shape[0],
                                self.input.shape[1],
                                self.input.shape[2]))

    def operate(self):
        for layer in range(self.input.shape[2]):
            for row in range(self.input.shape[0]):
                for column in range(self.input.shape[1]):
                    self.result[row, column, layer] = 0.1*self.input[row, column, layer] if self.input[row, column, layer] < 0 else self.input[row, column, layer]
        return self.result


class MaxPooling:
    def __init__(self, input, poolingSize=2):
        self.input = input
        self.poolingSize = poolingSize
        self.result = np.zeros((int(self.input.shape[0]/self.poolingSize),
                                int(self.input.shape[1]/self.poolingSize),
                                self.input.shape[2]))

    def operate(self):
        for layer in range(self.input.shape[2]):
            for row in range(int(self.input.shape[0]/self.poolingSize)):
                for column in range(int(self.input.shape[1]/self.poolingSize)):
                    self.result[row, column, layer] = np.max(self.input[row*self.poolingSize: row*self.poolingSize + self.poolingSize,
                                                                 column*self.poolingSize: column*self.poolingSize + self.poolingSize,
                                                                 layer])
        return self.result

# img_gray_conv2d = Conv2d(input=img_gray,numberOfKernel=16,kernelSize= 3, padding=0, stride=2).operate()
# img_gray_conv2d_relu = ReLU(img_gray_conv2d).operate()
# img_gray_conv2d_leakyrelu = LeakyReLU(img_gray_conv2d).operate()
# img_gray_conv2d_leakyrelu_maxpooling = MaxPooling(img_gray_conv2d_leakyrelu, poolingSize=3).operate()
# fig = plt.figure(figsize=(8, 8))
# for i in range(16):
#     plt.subplot(4, 4, i+1)
#     plt.imshow(img_gray_conv2d_leakyrelu_maxpooling[:, :, i], cmap='gray')
#     plt.axis('off')
# plt.savefig('img_gray_conv2d_leakyrelu_maxpooling.jpg')
# plt.show()

# fig = plt.figure(figsize=(12, 12))
# for i in range(1, 10):
#     conv2d = Conv2d(input=img_gray,kernelSize= 3, padding=0, stride=2)
#     img_gray_conv2d = conv2d.operate()
#     conv2d_relu = ReLU(input=img_gray_conv2d)
#     img_gray_conv2d_relu = conv2d_relu.operate()

#     plt.subplot(3, 3, i)
#     plt.imshow(img_gray_conv2d_relu, cmap='gray')
#     plt.axis('off')

# plt.show()
