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

<img src="/imagesMarkdown/ReLU-activation-function.png" width="" height="">

*   ReLU (Rectified Linear Unit) là một hàm kích hoạt được sử dụng trong các lớp convolutional neural network (CNN) để giảm thiểu hiện tượng vanishing gradient (mất mát độ dốc) và tăng tính phi tuyến tính của mô hình.

*   Hàm ReLU có công thức đơn giản: f(x) = max(0,x), trong đó x là giá trị đầu vào và max(0,x) trả về giá trị của x nếu x lớn hơn hoặc bằng 0, ngược lại trả về 0.

*   ReLU được sử dụng như một hàm kích hoạt sau các lớp convolutional và pooling để thực hiện một số chức năng quan trọng trong mạng CNN, bao gồm:

    1.  Tính phi tuyến tính: ReLU giúp giảm thiểu tính tuyến tính của mô hình bằng cách đưa vào không gian phi tuyến tính cho đầu ra.

    2.  Loại bỏ giá trị âm: ReLU loại bỏ giá trị âm và giữ lại giá trị không âm, giúp tăng tốc độ tính toán và giảm sự phụ thuộc vào các tham số.

    3.  Không độc quyền (non-exclusive): ReLU là một hàm không độc quyền, nghĩa là nhiều giá trị đầu vào có thể trả về cùng một giá trị đầu ra. Điều này giúp giảm thiểu hiện tượng overfitting (quá khớp) trong mô hình.

*   Với những lợi ích trên, ReLU đã trở thành một lựa chọn phổ biến để sử dụng trong các mạng CNN.

---

<img src="/imagesMarkdown/Screenshot 2023-03-03 033013.png" width="" height="">
