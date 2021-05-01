# Plant-Vision
Plant Vision là một ứng dụng web sử dụng AI để xác định được các bệnh của cây thông qua các hình ảnh.


# Cảm hứng

Quản lí bệnh cây trồng là một trong những yếu tố hết sức quan trọng trong đảm bảo chất lượng nông nghiệp và bảo tồn đa dạng sinh học. Tuy thế, các phương pháp để xác định bệnh của cây vẫn còn chậm và không hiệu quả. Plant Vision được sinh ra từ ý tưởng rằng nếu có thể tạo ra công cụ chẩn đoán bệnh ngay trên các thiết bị của chúng ta thì việc xác định bệnh cây trồng sẽ rất nhanh, hiệu quả và cá nhân hóa. Sử dụng convolutional neural network để phân loại ảnh, Plant Vision có khả năng trở thành giải pháp nhanh gọn đối với các nông dân, nhà nghiên cứu, học sinh,... để có thể phát hiện ra các bệnh câu trồng ngay từ những tấm ảnh.

# Tầm quan trong

Số liệu cho thấy răng hàng tỉ đo được tri cho việc quản lí bệnh cây trồng nhưng do chất lượng kĩ thuật kém và thủ công nên phương pháp này thường không hiệu quả. Thiệt hại về sản lượng do không thể xác định các bệnh cây trồng hiệu quả không chỉ tác động đến nền nông nghiệp mà còn rất nhiều cộng động dựa dẫm vào các nguồn thức ăn bị lây nhiễm. Chính vì thế, với khả năng tự động hóa việc chẩn đoán bệnh cây, Plant Vision có tiềm năng trở thành công cụ quan trọng trong việc quản lý nông nghiệp nhanh chóng và xác định được bệnh sớm để phòng ngừa, bảo vệ đa dạng sinh học. 

# Cấu trúc

  
  ## a. Dataset: 
  
  Được train bằng dataset gồm hơn 200000 ảnh của các loại lá của Plant Village (3 loại: Potato, Tomato và Pepperbell) với 15 trạng thái. Do hạn chế về thời gian và computing power nên model mới được train bằng dataset này. Trong những bản update sắp tới, dự định sẽ có hơn 50000 ảnh của 6 loại cây với 38 trạng thái.
  
  Link tới dataset: [PlantVillage](https://www.kaggle.com/emmarex/plantdisease)
  
  
  ## b. Mô hình AI: 
  Sequential, bao gồm  convolutional layers, 1 layer flatten, 2 layer Dense với Dropout để giảm overfitting, và optimizer Adam.
  
  Link tới Kaggle Notebook dùng để train model: [Kaggle](https://www.kaggle.com/bachchan1232313/plant-vision)
  
  Sau khi được train, model đat độ accuracy chính xác nhất là 91%.
  

# Web App

Plant Vision được xây dựng bằng Vue.js, Flask và MySQL. Trên Vue.js là những giao diện để người dùng có thể input ảnh và giao tiếp với các REST APIs sử dụng model để chẩn đoán bệnh. Ngoài ra, Plant Vision còn có database MySQL để người dùng có thể query các thông tin về từng loại bệnh như là tên bệnh, nguyên nhân, triệu chứng và giải pháp.

Demo Home Page: [HOME](https://drive.google.com/file/d/1gD7T8lx0DXE4P_XaecNYOLHChFJWDgFZ/view?usp=sharing)

Demo Library Page: [LIBRARY](https://drive.google.com/file/d/1Zhg0gBhBIvApnxLCpnEW7cPB9NAw0e8D/view?usp=sharing)

Demo Identification Page: [PREDICTION](https://drive.google.com/file/d/1VQQjGVBDkr8rRRnefvFfCzMhdIbbNsMh/view?usp=sharing)

Do giới hạn về thời gian, một server để deploy app vẫn đang trong quá trình setup. Một bản test public sẽ được release sau.


# Các điểm mạnh

01. Dễ tiếp cận, chức năng đơn giản và dễ hiểu
02. Model AI lightweight (<5MB), có thể được scale nhanh chóng
03. Tương thích với cả điện thoại và máy tính
04. Model AI có thể áp dụng cho các vấn đề classification khác

# Một số các điểm sẽ được cải thiện:

01. Mở rộng datasets để có thể xác định được nhiều bệnh hơn
02. Tích hợp các chức năng người dùng như login/signup, search về các bệnh, lịch sử các bệnh người dùng đã xác định,...
03. Tích hợp chức năng feedback để cải thiện model
04. Tạo thêm các thông tin về các loại thuốc, order thuốc để trị bệnh
05. Tạo thêm model để filter các ảnh không phải là cây
06. Sử dụng transfer lên một số pre-trained model cho image classification nổi tiếng như là VGG16 hay InceptionV3
07. Tích hợp chatbot để hỗ trợ người 

# Một giải pháp khác để tiếp cận vấn đề về classifying các loại bệnh:

Một giải phát khác tiếp cận vấn đề này là sử dụng Bag of Visual Words để phân loại các loại bệnh. Đây là một giải pháp tuy nhanh và chính xác nhưng chỉ phù hợp với lượng data bé (2-3 loại bệnh). 

# Một số các thư viện, frameworks được sử dụng:
 
 01. Vue.js
 02. Flask
 03. SQLAlchemy
 04. Tensorflow + Keras
 05. Pandas
 06. Seaborn
 07. Matplotlib
 08. Numpy
 09. Opencv
 10. PIL
 11. SKlearn
 

# References:

https://www.mdpi.com/journal/agriculture/special_issues/plant_disease

https://insightsimaging.springeropen.com/articles/10.1007/s13244-018-0639-9

https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53

https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb

https://www.sciencedirect.com/science/article/pii/S2214317316300154

https://towardsdatascience.com/wtf-is-image-classification-8e78a8235acb

https://www.analyticsvidhya.com/blog/2020/02/learn-image-classification-cnn-convolutional-neural-networks-3-datasets/


 











