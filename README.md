# Convolutional Neural Network (CNN)

<img src="/imagesMarkdown/Screenshot 2023-03-02 024303.png" width="" height="">

## Convolution

<img src="/imagesMarkdown/conv-full-layer.gif" width="" height="">


*   Ma trận bên trái nhất tượng trưng cho tấm hình của mình, mỗi một ô là 1 pixel

*   Ma trận hình vuông ở giữa (3*3) gọi là kernel và nó chỉ có kích thước lẻ ví dụ như 3\*3, 5\*5, 7\*7, ..không bao giờ lấy số chẵn.

*   Ma trận bên trái là ma trận kết quả sau khi lấy mt bên trái chập với ma trận 3\*3 ở giữa.


<img src="/imagesMarkdown/Screenshot 2023-03-02 042049.png" width="" height="">

## CNN no padding 

<img src="/imagesMarkdown/Convolution_arithmetic_-_No_padding_strides.gif" width="" height="">

## Stride

*   Mỗi lần chập thì kernel sẽ di chuyển với bước nhảy = stride.

*   Stride càng lớn có thể làm thông tin bị mất

<img src="/imagesMarkdown/Stride_convolution.gif" width="" height="">

## CNN with padding 

*   Các pixel ở viền sẽ được tính toán vài lần so với chỉ được tính toán một lần khi no padding.

<img src="/imagesMarkdown/Convolution_arithmetic_-_Padding_strides.gif" width="" height="">

## ReLU (Rectified Linear Unit)

*   ReLU (Rectified Linear Unit) là một hàm kích hoạt được sử dụng trong các lớp convolutional neural network (CNN) để giảm thiểu hiện tượng vanishing gradient (mất mát độ dốc) và tăng tính phi tuyến tính của mô hình.

*   Hàm ReLU có công thức đơn giản: f(x) = max(0,x), trong đó x là giá trị đầu vào và max(0,x) trả về giá trị của x nếu x lớn hơn hoặc bằng 0, ngược lại trả về 0.

*   ReLU được sử dụng như một hàm kích hoạt sau các lớp convolutional và pooling để thực hiện một số chức năng quan trọng trong mạng CNN, bao gồm:

    1.  Tính phi tuyến tính: ReLU giúp giảm thiểu tính tuyến tính của mô hình bằng cách đưa vào không gian phi tuyến tính cho đầu ra.

    2.  Loại bỏ giá trị âm: ReLU loại bỏ giá trị âm và giữ lại giá trị không âm, giúp tăng tốc độ tính toán và giảm sự phụ thuộc vào các tham số.

    3.  Không độc quyền (non-exclusive): ReLU là một hàm không độc quyền, nghĩa là nhiều giá trị đầu vào có thể trả về cùng một giá trị đầu ra. Điều này giúp giảm thiểu hiện tượng overfitting (quá khớp) trong mô hình.

*   Với những lợi ích trên, ReLU đã trở thành một lựa chọn phổ biến để sử dụng trong các mạng CNN.

<img src="/imagesMarkdown/ReLU-activation-function.png" width="" height="">

## Leaky ReLU

*   Leaky ReLU là một hàm kích hoạt được sử dụng trong các mô hình mạng neural, bao gồm các mô hình Convolutional Neural Network (CNN). Hàm Leaky ReLU tương tự như Rectified Linear Unit (ReLU) với hàm kích hoạt phi tuyến tính, nhưng thay vì có giá trị 0 khi đầu vào âm, nó sẽ trả về giá trị nhỏ hơn 0 một lượng nhỏ được xác định trước đó.

*   Cụ thể, hàm Leaky ReLU được định nghĩa bởi công thức:

    f(x) = x nếu x > 0

    f(x) = ax nếu x <= 0 (với a là một hằng số nhỏ dương)

*   Trong các mô hình CNN, hàm Leaky ReLU thường được sử dụng thay cho ReLU vì nó giúp tránh hiện tượng "neuron chết" (dead neurons), khi một số neuron không hoạt động do có giá trị đầu vào âm quá lớn và đưa về giá trị 0. Bằng cách cho phép một lượng nhỏ giá trị âm đi qua, hàm Leaky ReLU giúp duy trì tính phi tuyến tính của mô hình và tăng tính linh hoạt trong việc học các đặc trưng của ảnh.

<img src="/imagesMarkdown/LeakyReLU-activation-function.png" width="" height="">

---
### *img gray conv2d*

<img src="/img_gray_conv2d.jpg" width="" height="">

### *img gray conv2d relu*

<img src="/img_gray_conv2d_relu.jpg" width="" height="">

### *img gray conv2d leaky relu*

<img src="/img_gray_conv2d_leakyrelu.jpg" width="" height="">

## Max Pooling 

*   Max Pooling là một kỹ thuật được sử dụng trong Convolutional Neural Network (CNN) để giảm kích thước của đầu vào thông qua việc lấy giá trị lớn nhất (max) của mỗi vùng đặc trưng (feature map) được chia thành các ô nhỏ.

*   Cụ thể, trong quá trình max pooling, ta chia vùng đặc trưng thành các ô nhỏ, và lấy giá trị lớn nhất trong mỗi ô để tạo thành một feature map mới có kích thước nhỏ hơn. Quá trình này giúp giảm số lượng tham số của mô hình, đồng thời giúp giảm khả năng overfitting và làm giảm độ phức tạp của mô hình.

*   Điều quan trọng cần lưu ý là kích thước và bước nhảy (stride) của max pooling cần phải được chọn sao cho feature map được giảm kích thước một cách hợp lý, nhưng vẫn giữ được độ chi tiết của thông tin trong ảnh. Ví dụ, nếu ta chọn kích thước và stride quá lớn, ta sẽ mất mát quá nhiều thông tin trong quá trình max pooling, dẫn đến việc giảm độ chính xác của mô hình.

*   Max pooling thường được sử dụng sau các lớp Convolution và ReLU để giảm kích thước của feature map và giúp cho mô hình trở nên nhẹ hơn và dễ dàng xử lý hơn.

<img src="/imagesMarkdown/MaxpoolSample2.png" width="" height="">

### *img gray conv2d leaky relu maxpooling*

<img src="/img_gray_conv2d_leakyrelu_maxpooling.jpg" width="" height="">

