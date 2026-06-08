import html
import json
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "LAB3_7_PRESENTATION_GUIDE_MOBILE.html"

LABS = [
    {
        "id": "lab3",
        "title": "Lab 3 - Regression Techniques",
        "path": ROOT / "Lab3" / "Lab3_Regression_Techniques.ipynb",
        "intro": "Trong lab này em làm các kỹ thuật hồi quy và phân loại logistic. Phần quan trọng là em không dùng sẵn Linear Regression, PolynomialFeatures hay LogisticRegression cho thuật toán chính, mà tự viết bằng NumPy để hiểu công thức cập nhật tham số.",
        "datasets": [
            ("Auto MPG", "UCI Machine Learning Repository", "Lab3/data/auto-mpg.data", "Bộ này gồm thông tin xe như mpg, số xy-lanh, dung tích, horsepower, weight, acceleration, năm sản xuất và origin. Nó phù hợp với hồi quy vì target mpg là giá trị liên tục, nên có thể dùng để dự đoán mức tiêu hao nhiên liệu từ horsepower hoặc weight."),
            ("Iris", "UCI Machine Learning Repository", "Lab3/data/iris.data", "Bộ này có 150 mẫu hoa Iris, 3 loài, mỗi mẫu có 4 số đo cánh/đài hoa. Nó phù hợp với Logistic Regression vì target là nhãn phân loại, và khi dùng petal length/petal width thì có thể vẽ decision boundary rất dễ giải thích."),
        ],
    },
    {
        "id": "lab4",
        "title": "Lab 4 - Classification Techniques",
        "path": ROOT / "Lab4" / "Lab4_Classification_Techniques.ipynb",
        "intro": "Trong lab này em làm các mô hình phân loại cổ điển: KNN, Naive Bayes, Decision Tree và SVM RBF. Ý chính khi trình bày là mỗi thuật toán được viết tay để thấy rõ cách model ra quyết định: KNN dựa vào khoảng cách, Naive Bayes dựa vào xác suất từ, Decision Tree dựa vào Gini, SVM RBF dùng kernel để tách dữ liệu phi tuyến.",
        "datasets": [
            ("Iris", "UCI Machine Learning Repository", "Lab4/data/iris.data", "Dùng cho KNN vì dữ liệu nhỏ, sạch, có nhãn rõ ràng và dùng 2 đặc trưng petal length/petal width để vẽ decision boundary khi thay đổi K."),
            ("SMS Spam Collection", "UCI, file TSV tải qua GitHub raw", "Lab4/data/sms.tsv", "Bộ này gồm tin nhắn SMS gắn nhãn ham/spam. Nó phù hợp với Naive Bayes vì bài toán spam filter thường biểu diễn văn bản bằng Bag-of-Words rồi tính xác suất từ theo từng lớp."),
            ("WDBC Breast Cancer", "UCI Machine Learning Repository", "Lab4/data/wdbc.data", "Bộ này gồm 569 mẫu khối u với 30 đặc trưng số học và nhãn benign/malignant. Nó phù hợp với Decision Tree vì cây có thể tách theo ngưỡng từng feature và visualize được đường ra quyết định."),
            ("Two-moons", "Tự tạo bằng NumPy", "không có file riêng", "Dữ liệu hai hình mặt trăng dùng để kiểm tra SVM RBF trên dữ liệu phi tuyến. Em tự tạo bằng NumPy để không dùng sklearn.make_moons."),
        ],
    },
    {
        "id": "lab5",
        "title": "Lab 5 - Model Evaluation",
        "path": ROOT / "Lab5" / "Lab5_Model_Evaluation.ipynb",
        "intro": "Trong lab này em tập trung vào đánh giá mô hình trên dữ liệu mất cân bằng. Điểm cần nhấn mạnh là accuracy có thể gây hiểu nhầm, nên em tự tính thêm confusion matrix, precision, recall, F1, ROC và Precision-Recall để đánh giá đúng lớp fraud hiếm.",
        "datasets": [
            ("Credit Card Fraud Detection", "Kaggle - mlg-ulb/creditcardfraud", "Lab1/data/creditcard.csv", "Bộ này có giao dịch thẻ tín dụng, nhãn Class=1 là gian lận và Class=0 là bình thường. Dữ liệu cực kỳ mất cân bằng nên rất phù hợp cho Lab 5: nếu chỉ nhìn accuracy thì model có thể dự đoán toàn bình thường vẫn cao, nhưng recall fraud lại kém."),
        ],
    },
    {
        "id": "lab6",
        "title": "Lab 6 - Ensemble Learning",
        "path": ROOT / "Lab6" / "Lab6_Ensemble_Learning.ipynb",
        "intro": "Trong lab này em dùng đúng yêu cầu đề là Random Forest và XGBoost để tối ưu độ chính xác. Em có thêm Decision Tree đơn làm baseline, rồi so sánh với hai ensemble để thấy ensemble thường ổn định và chính xác hơn.",
        "datasets": [
            ("Wine Recognition", "UCI Machine Learning Repository", "Lab6/data/wine.data", "Bộ này có 178 mẫu rượu, 13 đặc trưng hóa học và 3 lớp rượu. Nó phù hợp với classification và ensemble vì số feature vừa đủ để cây quyết định, Random Forest và XGBoost học được feature importance để giải thích model."),
        ],
    },
    {
        "id": "lab7",
        "title": "Lab 7 - Clustering Techniques",
        "path": ROOT / "Lab7" / "Lab7_Clustering_Techniques.ipynb",
        "intro": "Trong lab này em làm clustering và anomaly detection. Em viết tay K-Means, Mean Shift, DBSCAN và GMM. Khi trình bày, nên nói rõ K-Means hợp cụm tròn/lồi, DBSCAN và Mean Shift hợp cụm theo mật độ, còn GMM học phân phối Gaussian để phát hiện điểm bất thường.",
        "datasets": [
            ("Mall Customers", "GitHub raw dataset phổ biến cho customer segmentation", "Lab7/data/Mall_Customers.csv", "Bộ này có CustomerID, Gender, Age, Annual Income và Spending Score. Nó phù hợp với K-Means vì mục tiêu là phân khúc khách hàng theo thu nhập và mức chi tiêu."),
            ("Two-moons", "Tự tạo bằng NumPy", "không có file riêng", "Dữ liệu có hình cụm cong, dùng để chứng minh K-Means khó xử lý cụm phi tuyến, còn DBSCAN/Mean Shift dựa vào mật độ nên hợp hơn."),
            ("Credit Card Fraud Detection", "Kaggle - mlg-ulb/creditcardfraud", "Lab1/data/creditcard.csv", "Dùng cho GMM anomaly detection: fit GMM trên giao dịch bình thường, sau đó điểm có log-likelihood thấp được xem là bất thường hoặc nghi ngờ fraud."),
        ],
    },
]

G = {
("lab3",1):("Import thư viện","Ở cell đầu tiên, em chỉ chuẩn bị thư viện. os dùng để nối đường dẫn file, NumPy để tính toán ma trận, pandas để đọc dataset dạng bảng, còn matplotlib để vẽ biểu đồ loss và decision boundary.",[(1,5,"Cụm này là phần import. Nó chưa train model, chỉ chuẩn bị công cụ cho các cell sau.")],"Nếu cô hỏi vì sao dùng NumPy, em trả lời: vì các thuật toán viết tay cần thao tác vector, ma trận và gradient nên NumPy là thư viện nền tảng phù hợp.","Cell này không vẽ hình."),
("lab3",2):("Linear Regression bằng Gradient Descent trên Auto MPG","Ở cell này, em đọc bộ Auto MPG, lấy horsepower làm biến đầu vào và mpg làm giá trị cần dự đoán. Sau đó em tự chia train-test, tự chuẩn hóa dữ liệu, rồi viết Batch Gradient Descent để học hai tham số của đường hồi quy tuyến tính. Cuối cell em chạy nhiều learning rate để so sánh tốc độ hội tụ.",[(1,13,"Đọc dataset Auto MPG từ file ngoài, bỏ dòng thiếu dữ liệu, chọn X là horsepower và y là mpg."),(15,27,"Chia train-test thủ công bằng cách xáo trộn index, sau đó chuẩn hóa horsepower theo mean/std của tập train. Việc chuẩn hóa giúp Gradient Descent ổn định hơn."),(29,42,"Định nghĩa hàm Gradient Descent. Trong mỗi vòng lặp, code tính sai số, tính gradient của MSE theo theta, rồi cập nhật theta theo learning rate."),(44,52,"Chạy thử nhiều learning rate. Với mỗi learning rate, em train theta, dự đoán trên test và in test MSE."),(54,58,"Vẽ loss theo iteration bằng thang log để nhìn learning rate nào hội tụ nhanh hoặc chậm.")],"Nếu cô hỏi learning rate là gì, em nói: learning rate quyết định bước nhảy khi cập nhật tham số; nhỏ quá thì học chậm, lớn quá thì dễ dao động hoặc không hội tụ.","Biểu đồ loss: đường nào giảm nhanh và mượt là learning rate tốt. Nếu đường giảm rất chậm thì learning rate nhỏ. Nếu loss dao động hoặc không giảm ổn định thì learning rate quá lớn."),
("lab3",3):("Polynomial Regression viết tay","Cell này mở rộng hồi quy tuyến tính thành hồi quy đa thức. Em tự tạo feature x, x^2, ..., x^degree, rồi dùng Normal Equation để tìm tham số. Em dùng weight để dự đoán mpg, vì quan hệ giữa cân nặng xe và mức tiêu hao nhiên liệu thường không hoàn toàn tuyến tính.",[(1,5,"Phần tiêu đề nhấn mạnh không dùng PolynomialFeatures hoặc LinearRegression của sklearn."),(7,13,"Hàm create_polynomial_features tự tạo cột bias và các lũy thừa của X."),(15,20,"Hàm Normal Equation giải trực tiếp theta bằng công thức ma trận, có regularization nhỏ để tránh lỗi nghịch đảo."),(22,30,"Chuẩn bị dữ liệu: lấy weight làm X, mpg làm y, chuẩn hóa weight và tạo lưới X mới để vẽ đường cong."),(32,47,"Lặp qua các bậc đa thức, fit theta, dự đoán trên lưới và vẽ từng đường hồi quy lên scatter plot.")],"Nếu cô hỏi khác gì Linear Regression, em nói: bản chất vẫn là hồi quy tuyến tính theo tham số theta, nhưng đầu vào đã được biến đổi thành các lũy thừa nên mô hình biểu diễn được đường cong.","Hình scatter và các đường degree cho thấy bậc thấp đơn giản hơn, bậc cao bám dữ liệu tốt hơn nhưng nếu quá cao có thể overfit."),
("lab3",4):("Softmax Logistic Regression trên Iris","Ở cell này, em viết Logistic Regression đa lớp bằng softmax. Em định nghĩa softmax, one-hot label, class model có fit và predict, rồi đọc Iris từ file UCI. Sau khi train, em in classification report và vẽ decision boundary trên hai feature petal length/petal width.",[(1,15,"Khai báo các hàm toán học: softmax để đổi score thành xác suất, one-hot để biểu diễn nhãn nhiều lớp."),(17,55,"Định nghĩa class LogisticRegressionScratch. Trong fit, model tính score, tính xác suất, lấy sai số so với one-hot label, rồi cập nhật weights và bias bằng gradient descent."),(57,75,"Tự viết hàm accuracy và classification report để không phụ thuộc sklearn metrics."),(77,86,"Đọc Iris từ file ngoài, map tên loài hoa thành số, chọn hai feature petal length/petal width."),(88,103,"Chia train-test stratified thủ công để mỗi lớp đều có mặt trong train và test."),(105,114,"Chuẩn hóa dữ liệu, train model, dự đoán và in báo cáo phân loại."),(116,109,"Tạo lưới điểm 2D và vẽ decision boundary để thấy vùng dự đoán của từng lớp.")],"Nếu cô hỏi vì sao dùng softmax, em nói: vì Iris có 3 lớp, sigmoid chỉ phù hợp nhị phân; softmax cho ra xác suất của tất cả các lớp và chọn lớp có xác suất cao nhất.","Decision boundary thể hiện mỗi vùng màu là một lớp Iris mà model dự đoán. Các điểm thật nằm trong vùng cùng màu càng nhiều thì model phân loại càng tốt."),
("lab4",1):("KNN viết tay và decision boundary","Cell này em viết KNN từ đầu. KNN không học tham số như hồi quy, mà lưu tập train. Khi dự đoán một điểm mới, model tính khoảng cách Euclidean tới tất cả điểm train, lấy K điểm gần nhất và bỏ phiếu nhãn nhiều nhất.",[(1,7,"Import thư viện và công cụ cần dùng cho xử lý file, mảng, bảng, biểu đồ và đếm phiếu."),(9,31,"Định nghĩa class KNN: fit lưu dữ liệu train, _euclidean_distance tính khoảng cách, predict dự đoán nhiều điểm, _predict_one bỏ phiếu K láng giềng."),(33,43,"Đọc Iris, map nhãn loài hoa thành số, lấy petal length/petal width và chuẩn hóa thủ công."),(45,59,"Với K = 1, 5, 15, code tạo lưới điểm, dự đoán từng điểm trên lưới và vẽ decision boundary.")],"Nếu cô hỏi K ảnh hưởng gì, em nói: K nhỏ thì biên quyết định gồ ghề và dễ nhạy với nhiễu; K lớn thì biên mượt hơn nhưng có thể làm mất chi tiết cục bộ.","Ba hình decision boundary cho thấy khi K thay đổi, vùng phân loại cũng đổi. Đây là phần quan trọng nhất để giải thích trực quan KNN."),
("lab4",2):("Naive Bayes cho SMS Spam","Cell này em xây dựng bộ lọc spam. Đầu tiên em biến tin nhắn thành các từ bằng tokenizer, sau đó tạo vocabulary và vector Bag-of-Words. Với mỗi lớp spam/ham, em tính xác suất xuất hiện của từng từ có Laplace smoothing, rồi dùng log probability để dự đoán.",[(1,8,"Phần tiêu đề nói rõ đây là Naive Bayes viết tay, không dùng MultinomialNB hay CountVectorizer."),(10,78,"Định nghĩa class NaiveBayesScratch: tokenize văn bản, xây vocabulary, đổi text thành vector đếm từ, tính prior và likelihood cho từng lớp."),(80,99,"Đọc SMS dataset, đổi nhãn spam thành 1 và ham thành 0, chia train-test stratified thủ công."),(101,111,"Train Naive Bayes, dự đoán test set, rồi tính accuracy, spam precision và spam recall.")],"Nếu cô hỏi vì sao dùng log, em nói: vì nhân nhiều xác suất nhỏ dễ bị underflow; lấy log biến tích thành tổng nên ổn định số hơn.","Cell này không vẽ hình; kết quả chính là accuracy, precision và recall của spam filter."),
("lab4",3):("Decision Tree Gini trên WDBC","Cell này em tự viết Decision Tree. Ý tưởng là ở mỗi node, cây thử nhiều feature và threshold, chọn cách tách làm giảm Gini impurity nhiều nhất. Sau đó cây đệ quy xây node trái/phải cho tới khi đạt max_depth hoặc node đủ thuần.",[(1,12,"Khai báo phần Decision Tree và class TreeNode để lưu thông tin một node trong cây."),(14,105,"Định nghĩa DecisionTreeScratch: tính Gini, tìm split tốt nhất, build cây đệ quy, dự đoán một điểm và nhiều điểm."),(107,162,"Các hàm visualize dùng để in cây dạng text và vẽ cây bằng matplotlib."),(164,188,"Đọc WDBC từ file ngoài, tách X/y, chia train-test stratified thủ công."),(190,203,"Train cây, tính accuracy, in cấu trúc cây và vẽ cây quyết định.")],"Nếu cô hỏi Gini là gì, em nói: Gini đo độ lẫn lộn của nhãn trong node. Nếu node toàn một lớp thì Gini thấp, nếu trộn nhiều lớp thì Gini cao. Cây chọn split làm Gini giảm nhiều nhất.","Hình cây: mỗi node là một điều kiện feature <= threshold. Đi nhánh True/False đến leaf sẽ ra class benign hoặc malignant."),
("lab4",4):("SVM RBF viết tay trên two-moons","Cell này em dùng SVM với RBF kernel để phân loại dữ liệu phi tuyến. Vì two-moons không tách được tốt bằng đường thẳng, RBF kernel giúp đo độ giống nhau phi tuyến giữa các điểm và tạo decision boundary cong.",[(1,12,"Phần tiêu đề nhấn mạnh không dùng sklearn SVC."),(14,70,"Định nghĩa SVMScratch: RBF kernel, fit bằng cập nhật alpha và bias, predict bằng kernel giữa điểm mới và điểm train."),(76,90,"Tự tạo dữ liệu two-moons bằng NumPy, không dùng sklearn.make_moons."),(92,108,"Train SVM, tạo lưới điểm 2D, dự đoán trên lưới và vẽ decision boundary.")],"Nếu cô hỏi RBF kernel làm gì, em nói: RBF biến bài toán sang không gian tương đồng, điểm gần nhau có kernel lớn, điểm xa nhau có kernel nhỏ, nhờ vậy model tạo được biên cong.","Decision boundary cong ôm theo hai cụm mặt trăng. Đây là minh chứng SVM RBF phù hợp dữ liệu phi tuyến."),
("lab5",1):("Import thư viện","Cell này chỉ import thư viện cơ bản: os để lấy đường dẫn, NumPy để tính toán, pandas để đọc dữ liệu và matplotlib để vẽ confusion matrix, ROC, Precision-Recall.",[(1,4,"Import công cụ nền tảng cho toàn bộ Lab 5.")],"Nếu cô hỏi vì sao không import sklearn metrics, em nói: vì trong lab này em tự tính các metric để hiểu rõ công thức đánh giá.","Cell này không vẽ hình."),
("lab5",2):("Hàm tiện ích train-test, chuẩn hóa, sigmoid","Cell này em viết các hàm phụ trợ. train_test_split_np chia dữ liệu theo từng lớp để giữ tỷ lệ fraud/normal. standardize_train_test chuẩn hóa theo tập train. sigmoid dùng trong Logistic Regression để đổi logit thành xác suất.",[(1,14,"Hàm chia train-test stratified thủ công, đảm bảo lớp fraud hiếm vẫn xuất hiện trong cả train và test."),(16,21,"Hàm chuẩn hóa dữ liệu bằng mean/std của train để tránh rò rỉ thông tin từ test."),(23,25,"Hàm sigmoid có clip để tránh overflow khi số quá lớn hoặc quá nhỏ.")],"Nếu cô hỏi vì sao chuẩn hóa theo train, em nói: vì test phải giả lập dữ liệu chưa biết; nếu dùng thống kê của test để chuẩn hóa thì bị data leakage.","Cell này không vẽ hình."),
("lab5",3):("Đọc Credit Card Fraud và tạo tập mất cân bằng","Ở cell này em đọc dataset credit card từ Lab1. Vì dữ liệu gốc rất lớn, em lấy mẫu 20.000 giao dịch normal và giữ toàn bộ fraud, sau đó trộn lại. Cách này vẫn giữ tính mất cân bằng nhưng giúp notebook chạy nhanh hơn.",[(1,5,"Kiểm tra file creditcard.csv có tồn tại không; nếu không có thì báo lỗi rõ ràng."),(7,11,"Đọc dữ liệu, lấy toàn bộ fraud và sample một phần normal để giảm kích thước."),(13,15,"Tạo X gồm Time, Amount và V1-V28; y là cột Class. In kích thước và tỷ lệ fraud để thấy dữ liệu mất cân bằng.")],"Nếu cô hỏi vì sao dùng dataset này, em nói: vì fraud là lớp rất hiếm, nên nó rất phù hợp để minh họa accuracy trap và các metric như recall/Precision-Recall.","Cell này chưa vẽ hình; kết quả cần nói là tỷ lệ fraud nhỏ hơn nhiều so với normal."),
("lab5",4):("Logistic Regression viết tay có class_weight","Cell này em tự viết Logistic Regression nhị phân. Trong fit, model thêm bias, tính xác suất bằng sigmoid, tính gradient và cập nhật theta. Em train hai bản: baseline bình thường và balanced có class weight để phạt lỗi lớp hiếm mạnh hơn.",[(1,6,"Khai báo class LogisticRegressionScratch và các tham số learning rate, số epoch, class_weight."),(8,27,"Hàm fit: thêm bias, khởi tạo theta, tạo sample_weight nếu dùng balanced, rồi lặp gradient descent để cập nhật theta."),(29,34,"Hàm predict_proba trả xác suất, hàm predict đổi xác suất thành nhãn theo threshold 0.5."),(36,38,"Chia train-test, chuẩn hóa, train hai mô hình baseline và balanced.")],"Nếu cô hỏi class_weight balanced là gì, em nói: nó tăng trọng số cho lớp fraud hiếm, để model không chỉ tối ưu cho lớp normal chiếm đa số.","Cell này không vẽ hình; kết quả được dùng ở các cell đánh giá phía sau."),
("lab5",5):("Tự tính metric đánh giá","Cell này em tự tính các metric từ TP, TN, FP, FN. Accuracy cho biết tổng thể đúng bao nhiêu, precision cho biết dự đoán fraud thì đúng bao nhiêu, recall cho biết bắt được bao nhiêu fraud thật, F1 cân bằng precision và recall.",[(1,13,"Hàm classification_metrics tính TP, TN, FP, FN rồi suy ra accuracy, precision, recall và F1."),(15,15,"Lặp qua baseline và balanced, dự đoán test set rồi in metric để so sánh.")],"Nếu cô hỏi metric nào quan trọng với fraud, em nói: recall rất quan trọng vì bỏ sót fraud là rủi ro lớn; precision cũng cần để tránh báo động nhầm quá nhiều.","Cell này in số liệu, chưa vẽ hình."),
("lab5",6):("Vẽ confusion matrix","Cell này em vẽ confusion matrix cho hai mô hình. Confusion matrix giúp nhìn rõ model dự đoán đúng normal, đúng fraud, báo động nhầm và bỏ sót fraud bao nhiêu trường hợp.",[(1,12,"Hàm plot_confusion tạo ma trận 2x2 và ghi số lượng lên từng ô."),(14,16,"Vẽ song song baseline và balanced để so sánh trực quan.")],"Nếu cô hỏi đọc confusion matrix thế nào, em nói: hàng là nhãn thật, cột là nhãn dự đoán; ô fraud thật nhưng predicted 0 là FN, tức bỏ sót fraud.","Hình confusion matrix là phần nên chỉ rõ khi trình bày: balanced thường đổi trade-off, có thể tăng khả năng bắt fraud nhưng cũng có thể tăng false positive."),
("lab5",7):("ROC và Precision-Recall curve","Cell này em tự tạo nhiều threshold khác nhau. Với mỗi threshold, em đổi score thành nhãn rồi tính FPR, TPR, precision và recall. Sau đó em vẽ ROC và Precision-Recall cho baseline và balanced.",[(1,15,"Hàm roc_pr_points quét nhiều threshold và tính các điểm trên ROC/PR curve."),(17,30,"Lấy xác suất của từng model, vẽ ROC bên trái và Precision-Recall bên phải.")],"Nếu cô hỏi vì sao Precision-Recall quan trọng, em nói: vì dữ liệu fraud mất cân bằng, PR curve tập trung vào lớp dương hiếm nên phản ánh khả năng bắt fraud rõ hơn accuracy hoặc đôi khi rõ hơn ROC.","ROC thể hiện TPR theo FPR. Precision-Recall thể hiện khi cố tăng recall thì precision thay đổi thế nào. Với fraud, em ưu tiên nhìn PR curve."),
("lab6",1):("Đọc Wine và train Decision Tree baseline","Ở cell này em đọc Wine dataset từ file UCI, đặt tên cột, tách X và y, chia train-test có stratify. Sau đó em train một Decision Tree đơn làm baseline để lát nữa so sánh với Random Forest và XGBoost.",[(1,8,"Import thư viện cần dùng cho ensemble và đánh giá."),(10,20,"Đọc Wine dataset, đặt tên feature, target là class trừ 1 để nhãn về 0,1,2."),(22,33,"Chia train-test, train Decision Tree baseline, dự đoán và in classification report.")],"Nếu cô hỏi vì sao cần baseline, em nói: baseline cho mình mốc so sánh; nếu ensemble tốt hơn cây đơn thì chứng minh việc kết hợp nhiều cây có ích.","Cell này in report, chưa vẽ hình."),
("lab6",2):("Random Forest","Cell này train Random Forest. Random Forest là nhiều Decision Tree train trên các mẫu bootstrap và chọn ngẫu nhiên một phần feature khi tách node. Nhờ vậy nó giảm overfitting và variance so với một cây đơn.",[(1,1,"Import RandomForestClassifier từ sklearn vì đề Lab 6 yêu cầu dùng Random Forest."),(3,11,"Khởi tạo Random Forest với 300 cây, max_features=sqrt và class_weight balanced."),(12,16,"Train, predict, tính accuracy và in classification report.")],"Nếu cô hỏi Random Forest khác Decision Tree thế nào, em nói: Decision Tree là một cây nên dễ overfit; Random Forest lấy trung bình/bỏ phiếu nhiều cây nên ổn định hơn.","Cell này in metric, chưa vẽ hình."),
("lab6",3):("XGBoost","Cell này train XGBoost. Khác Random Forest train nhiều cây độc lập, XGBoost train cây tuần tự; cây sau cố gắng sửa lỗi còn lại của các cây trước. Vì vậy nó thường đạt accuracy cao nếu tham số phù hợp.",[(1,1,"Import XGBClassifier từ thư viện xgboost."),(3,13,"Khởi tạo XGBoost với số cây, độ sâu, learning rate, subsample và colsample_bytree."),(14,18,"Train model, predict test set, in accuracy và classification report.")],"Nếu cô hỏi learning_rate trong XGBoost là gì, em nói: nó điều chỉnh mức đóng góp của mỗi cây mới; nhỏ hơn thì học chậm nhưng thường ổn định hơn.","Cell này in metric, chưa vẽ hình."),
("lab6",4):("Feature importance","Cell này lấy feature importance từ Random Forest và XGBoost rồi vẽ biểu đồ thanh ngang. Mục tiêu là không chỉ xem model đúng bao nhiêu, mà còn xem model dựa nhiều vào feature nào để phân biệt các loại rượu.",[(1,5,"Lấy mảng importance của hai model và sắp xếp thứ tự feature."),(7,23,"Vẽ hai biểu đồ thanh ngang: bên trái Random Forest, bên phải XGBoost.")],"Nếu cô hỏi feature importance dùng để làm gì, em nói: nó giúp giải thích model, biết feature nào ảnh hưởng mạnh đến quyết định phân loại.","Biểu đồ thanh càng dài thì feature càng quan trọng theo model. Có thể so sánh hai mô hình xem chúng ưu tiên feature giống hay khác nhau."),
("lab7",1):("K-Means customer segmentation","Cell này em viết K-Means từ đầu rồi áp dụng vào Mall Customers. K-Means hoạt động bằng cách khởi tạo centroid, gán mỗi điểm vào centroid gần nhất, cập nhật centroid bằng trung bình các điểm trong cụm, rồi lặp đến khi hội tụ.",[(1,8,"Import thư viện và khai báo phần K-Means viết tay."),(10,40,"Định nghĩa class KMeansScratch gồm khởi tạo centroid, gán cụm, cập nhật centroid và vòng lặp fit_predict."),(42,51,"Đọc Mall Customers, lấy Age, Annual Income, Spending Score và chuẩn hóa."),(53,62,"Chạy K-Means 5 cụm, gán nhãn cluster vào DataFrame, vẽ Income vs Spending Score và in trung bình từng cụm.")],"Nếu cô hỏi vì sao cần chuẩn hóa, em nói: vì Age, Income và Spending Score có thang đo khác nhau; nếu không chuẩn hóa, feature có giá trị lớn hơn sẽ chi phối khoảng cách.","Biểu đồ phân khúc khách hàng: trục X là thu nhập, trục Y là điểm chi tiêu, màu là cụm. Có thể giải thích từng nhóm như thu nhập cao/chi tiêu cao, thu nhập thấp/chi tiêu thấp."),
("lab7",2):("Mean Shift và DBSCAN trên two-moons","Cell này so sánh K-Means với Mean Shift và DBSCAN trên dữ liệu two-moons. Dữ liệu này có cụm cong nên K-Means thường không tốt vì K-Means thích cụm dạng tròn/lồi. Mean Shift và DBSCAN dựa trên mật độ nên hợp hơn.",[(1,18,"Tự tạo dữ liệu two-moons bằng NumPy."),(20,51,"Định nghĩa MeanShiftScratch: mỗi điểm dịch về trung bình các điểm lân cận trong bandwidth, sau đó gộp các tâm gần nhau."),(53,88,"Định nghĩa DBSCANScratch: tìm láng giềng trong eps, nếu đủ min_samples thì mở rộng cụm theo mật độ."),(90,106,"Chạy K-Means, Mean Shift, DBSCAN và vẽ 3 biểu đồ cạnh nhau để so sánh.")],"Nếu cô hỏi DBSCAN có ưu điểm gì, em nói: không cần biết trước số cụm, phát hiện được noise và xử lý cụm hình dạng lạ tốt hơn K-Means.","Ba hình cạnh nhau là điểm chính: K-Means hay cắt cụm cong sai, còn DBSCAN/Mean Shift thường bám theo cấu trúc hai mặt trăng tốt hơn."),
("lab7",3):("GMM anomaly detection","Cell này em viết Gaussian Mixture Model bằng EM. GMM giả sử dữ liệu bình thường được tạo từ nhiều phân phối Gaussian. Em fit GMM trên giao dịch normal, rồi tính log-likelihood cho tất cả điểm; điểm nào có likelihood thấp hơn threshold thì xem là bất thường.",[(1,15,"Khai báo class GMMScratch và các tham số số component, số vòng lặp, sai số hội tụ."),(17,31,"Hàm Gaussian PDF tính mật độ xác suất của từng điểm theo mean và covariance."),(33,84,"Hàm fit là EM algorithm: E-step tính responsibility, M-step cập nhật weight, mean, covariance, rồi kiểm tra log-likelihood hội tụ."),(86,97,"Hàm score_samples tính log-likelihood của mỗi sample."),(101,120,"Đọc Credit Card Fraud, lấy normal và fraud, chọn một số feature, chuẩn hóa và lấy normal làm tập train cho GMM."),(122,146,"Fit GMM, đặt threshold theo percentile thấp của normal, đánh dấu anomaly, tính precision/recall và vẽ histogram score.")],"Nếu cô hỏi EM là gì, em nói: EM gồm E-step ước lượng xác suất mỗi điểm thuộc từng Gaussian, và M-step cập nhật tham số Gaussian dựa trên các xác suất đó.","Histogram log-likelihood: vùng score thấp là vùng bất thường. Đường threshold màu đỏ dùng để tách anomaly khỏi normal."),
}

def code_cells(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    out, order = [], 0
    for idx, c in enumerate(nb["cells"]):
        if c.get("cell_type") == "code":
            order += 1
            out.append((order, idx, "".join(c.get("source", []))))
    return out

def numbered_code(src):
    rows = []
    for i, line in enumerate(src.splitlines(), 1):
        rows.append(f"<div class='codeline'><span class='no'>{i}</span><code>{html.escape(line)}</code></div>")
    return "\n".join(rows)

def code_excerpt(src, start, end):
    lines = src.splitlines()
    rows = []
    for line_no in range(start, end + 1):
        line = lines[line_no - 1] if line_no - 1 < len(lines) else ""
        rows.append(
            f"<div class='mini-line'><span>{line_no}</span><code>{html.escape(line)}</code></div>"
        )
    return "\n".join(rows)

def infer_chunk_details(block):
    lower = block.lower()
    details = []
    if "pd.read_csv" in block:
        details.append("Đoạn này đọc dữ liệu từ file ngoài vào DataFrame. Khi trình bày, em nói rõ đây là bước lấy dữ liệu thật từ dataset, không phải tự tạo dữ liệu mẫu.")
    if "dropna" in block:
        details.append("Có xử lý giá trị thiếu bằng cách bỏ các dòng bị thiếu, để các phép tính phía sau không bị lỗi hoặc sinh ra NaN.")
    if "to_numpy" in block or ".astype" in block:
        details.append("Dữ liệu được đổi sang dạng số hoặc mảng NumPy để thuật toán viết tay có thể nhân ma trận, tính gradient, khoảng cách hoặc xác suất.")
    if "random" in lower or "permutation" in lower or "shuffle" in lower or "sample" in lower:
        details.append("Có bước xáo trộn hoặc lấy mẫu để dữ liệu train/test khách quan hơn, tránh lấy theo thứ tự ban đầu của file.")
    if "train" in lower and "test" in lower:
        details.append("Đoạn này tách dữ liệu thành phần train để học mô hình và phần test để kiểm tra mô hình trên dữ liệu chưa dùng khi học.")
    if "mean" in lower and "std" in lower:
        details.append("Có chuẩn hóa bằng mean và độ lệch chuẩn. Ý cần nói là đưa các feature về cùng thang đo để thuật toán ổn định hơn.")
    if "gradient" in lower or "theta" in lower or "learning_rate" in lower:
        details.append("Đây là phần tối ưu tham số: model tính lỗi, tính hướng giảm lỗi, rồi cập nhật tham số theo learning rate.")
    if "def " in block:
        details.append("Có định nghĩa hàm để gom một chức năng riêng. Khi cô hỏi, em chỉ cần nói hàm này nhận đầu vào gì, xử lý gì, và trả ra kết quả gì.")
    if "class " in block:
        details.append("Có định nghĩa class để đóng gói thuật toán. Các hàm bên trong class tương ứng với các bước như fit, predict, tính metric hoặc vẽ kết quả.")
    if "fit(" in block:
        details.append("Có bước huấn luyện model. Ở đây model dùng dữ liệu train để học tham số hoặc học cấu trúc cần thiết.")
    if "predict" in lower:
        details.append("Có bước dự đoán. Sau khi model học xong, đoạn này dùng model để sinh nhãn hoặc giá trị dự đoán.")
    if "accuracy" in lower or "precision" in lower or "recall" in lower or "f1" in lower:
        details.append("Có tính metric đánh giá. Khi nói với cô, em nên nêu metric đó đo điều gì chứ không chỉ đọc con số.")
    if "plt." in block or "ax." in block or "scatter" in lower or "plot(" in lower or "hist" in lower or "contourf" in lower or "imshow" in lower or "barh" in lower:
        details.append("Có phần trực quan hóa. Khi trình bày hình, em nói trục X/Y là gì, màu biểu diễn gì, và kết luận chính rút ra từ hình.")
    if "gini" in lower:
        details.append("Phần này liên quan Decision Tree: Gini dùng để đo độ lẫn nhãn trong node, split tốt là split làm Gini giảm nhiều.")
    if "kernel" in lower or "gamma" in lower:
        details.append("Phần này liên quan kernel RBF: kernel đo độ giống nhau phi tuyến giữa các điểm, giúp tạo biên quyết định cong.")
    if "eps" in lower or "min_samples" in lower:
        details.append("Phần này liên quan DBSCAN: eps là bán kính lân cận, min_samples là số điểm tối thiểu để một vùng được xem là đủ đặc.")
    if "likelihood" in lower or "responsibilities" in lower or "covariance" in lower or "gaussian" in lower:
        details.append("Phần này liên quan GMM/EM: model ước lượng phân phối Gaussian và dùng log-likelihood để xem điểm nào bình thường hay bất thường.")
    if not details:
        details.append("Đây là một cụm xử lý phụ trong cell. Khi trình bày, em nói nó phục vụ cho bước ngay phía sau, ví dụ chuẩn bị biến, lưu kết quả, hoặc hoàn tất cấu trúc code.")
    return details

def chunk_cards(chunks, max_lines, src, cell_order):
    lines = src.splitlines()
    cards = []
    for idx, (a, b, text) in enumerate(chunks, 1):
        a = max(1, min(a, max_lines))
        b = max(a, min(b, max_lines))
        block = "\n".join(lines[a - 1:b])
        first_line = lines[a - 1].strip() if lines else ""
        detail_items = "".join(f"<li>{html.escape(item)}</li>" for item in infer_chunk_details(block))
        cards.append(f"""
        <article class='chunk-card' id='cell-{cell_order}-chunk-{idx}'>
          <h5>Cụm {idx}: dòng {a}-{b}</h5>
          <p class='chunk-say'><b>Khi chỉ đoạn này, em nói:</b> {html.escape(text)}</p>
          <p class='find-tip'><b>Mốc để tìm trên code máy tính:</b> dòng đầu cụm là <code>{html.escape(first_line[:120])}</code></p>
          <div class='mini-code'>{code_excerpt(src, a, b)}</div>
          <div class='deep'>
            <b>Nói kỹ hơn nếu cô hỏi:</b>
            <ul>{detail_items}</ul>
          </div>
        </article>
        """)
    return "\n".join(cards)

def dataset_cards(lab):
    cards = []
    for name, source, file, desc in lab["datasets"]:
        cards.append(f"""
        <div class='dataset-card'>
          <h4>{html.escape(name)}</h4>
          <p><b>Nguồn:</b> {html.escape(source)}</p>
          <p><b>File:</b> <code>{html.escape(file)}</code></p>
          <p>{html.escape(desc)}</p>
        </div>""")
    return "\n".join(cards)

def lab_html(lab):
    cells = []
    for order, nb_idx, src in code_cells(lab["path"]):
        name, say, chunks, ask, visual = G[(lab["id"], order)]
        max_lines = len(src.splitlines())
        cells.append(f"""
        <details class='cell' open>
          <summary><span>Cell {order}</span> {html.escape(name)}</summary>
          <div class='cellbody'>
            <section class='say'><h4>Em trình bày với cô như sau</h4><p>{html.escape(say)}</p></section>
            <section class='chunks'><h4>Các cụm code cần chỉ khi nói</h4>{chunk_cards(chunks, max_lines, src, order)}</section>
            <section class='teacher'><h4>Nếu cô hỏi thêm</h4><p>{html.escape(ask)}</p></section>
            <section class='visual'><h4>Phân tích kết quả hoặc hình vẽ</h4><p>{html.escape(visual)}</p></section>
            <details class='codebox'>
              <summary>Code gốc của cell này - lấy đúng từ notebook ({max_lines} dòng)</summary>
              <div class='code'>{numbered_code(src)}</div>
            </details>
          </div>
        </details>""")
    return f"""
    <section class='lab' id='{lab["id"]}'>
      <h2>{html.escape(lab["title"])}</h2>
      <div class='speech'><h3>Mở đầu lab, em nói ngắn gọn</h3><p>{html.escape(lab["intro"])}</p></div>
      <div class='datasets'><h3>Dataset của lab này</h3>{dataset_cards(lab)}</div>
      {''.join(cells)}
    </section>"""

nav = "".join(f"<a href='#{lab['id']}'>{html.escape(lab['title'].replace(' - ', ': '))}</a>" for lab in LABS)
sections = "".join(lab_html(lab) for lab in LABS)

page = f"""<!doctype html>
<html lang='vi'>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Kịch bản trình bày Lab 3-7</title>
<style>
:root {{--bg:#f4f6f8;--paper:#fff;--ink:#17202a;--line:#d7dde6;--brand:#0f766e;--brand2:#1d4ed8;--warm:#92400e;--code:#0f172a;--codeText:#e5e7eb;}}
*{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.65}}
header{{background:#152232;color:white;padding:22px 18px 18px}} header h1{{margin:0 0 8px;font-size:26px;line-height:1.2}} header p{{margin:6px 0;color:#dbe4ee;max-width:1050px}}
.topnav{{position:sticky;top:0;z-index:20;display:flex;gap:8px;overflow-x:auto;padding:10px;background:#fff;border-bottom:1px solid var(--line)}} .topnav a{{flex:0 0 auto;text-decoration:none;color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:8px 12px;font-weight:700;font-size:14px;background:#f8fafc}}
main{{max-width:1180px;margin:0 auto;padding:16px}} .lab{{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:18px;margin:0 0 18px}} .lab h2{{margin:0 0 12px;font-size:24px;padding-bottom:10px;border-bottom:2px solid #e8edf3}}
.speech,.datasets,.say,.chunks,.teacher,.visual{{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:12px 0;background:#fbfcfe}} .speech{{border-left:5px solid var(--brand)}} .datasets{{border-left:5px solid var(--brand2)}}
.dataset-card{{background:white;border:1px solid #e2e8f0;border-radius:10px;padding:10px 12px;margin:10px 0}} .dataset-card h4{{margin:0 0 6px;color:#0f766e}} .dataset-card p{{margin:5px 0}}
.cell{{border:1px solid var(--line);border-radius:12px;margin:14px 0;overflow:hidden;background:white}} .cell>summary{{cursor:pointer;background:#eaf1f8;padding:13px 14px;font-weight:800;font-size:17px}} .cell>summary span{{display:inline-block;background:var(--brand);color:white;border-radius:7px;padding:2px 8px;margin-right:8px;font-size:13px}} .cellbody{{padding:12px}}
.say{{border-left:5px solid var(--brand);background:#f0fdfa}} .chunks{{border-left:5px solid var(--warm);background:#fff7ed}} .teacher{{border-left:5px solid #7c3aed;background:#faf5ff}} .visual{{border-left:5px solid #dc2626;background:#fff1f2}}
h3,h4{{margin:0 0 7px;line-height:1.3}} p{{margin:0 0 6px}} ul{{margin:6px 0 0;padding-left:21px}} li{{margin:7px 0}}
.codebox{{margin-top:12px;border:1px solid #cbd5e1;border-radius:10px;overflow:hidden}} .codebox>summary{{cursor:pointer;padding:11px 13px;background:#f8fafc;font-weight:800;color:#0f766e}}
.code{{background:var(--code);color:var(--codeText);overflow:auto;max-height:70vh;padding:10px 0;font-family:Consolas,Monaco,'Courier New',monospace;font-size:13px;line-height:1.55}} .codeline{{display:grid;grid-template-columns:52px max-content;min-width:max-content}} .no{{color:#94a3b8;text-align:right;padding:0 12px 0 8px;user-select:none;border-right:1px solid #334155}} .codeline code{{white-space:pre;padding-left:12px;padding-right:16px}}
.chunk-card{{background:#fff;border:1px solid #fed7aa;border-radius:10px;margin:12px 0;padding:11px}} .chunk-card h5{{margin:0 0 8px;font-size:16px;color:#92400e}} .chunk-say{{background:#fffbeb;border-left:4px solid #f59e0b;padding:9px;border-radius:7px}} .find-tip{{font-size:14px;color:#475569;background:#f8fafc;border:1px dashed #cbd5e1;border-radius:7px;padding:8px;margin-top:8px}} .find-tip code{{word-break:break-all}}
.mini-code{{background:#111827;color:#e5e7eb;border-radius:8px;overflow:auto;margin:10px 0;padding:8px 0;font-family:Consolas,Monaco,'Courier New',monospace;font-size:12.5px;line-height:1.5}} .mini-line{{display:grid;grid-template-columns:42px max-content;min-width:max-content}} .mini-line span{{color:#94a3b8;text-align:right;padding:0 10px 0 6px;border-right:1px solid #334155;user-select:none}} .mini-line code{{white-space:pre;padding-left:10px;padding-right:14px}} .deep{{background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;padding:9px;margin-top:8px}} .deep ul{{margin-top:6px}}
.note{{font-size:14px;color:#dbe4ee}} .controls{{margin-top:12px;display:flex;gap:8px;flex-wrap:wrap}} button{{border:1px solid #91a1b5;background:#fff;color:#17202a;border-radius:8px;padding:8px 10px;font-weight:700}}
@media(max-width:720px){{body{{font-size:17px;line-height:1.7}}header{{padding:18px 14px}}header h1{{font-size:22px}}main{{padding:10px}}.lab{{padding:12px;border-radius:10px}}.lab h2{{font-size:21px}}.cell>summary{{font-size:16px;padding:12px}}.speech,.datasets,.say,.chunks,.teacher,.visual{{padding:11px;margin:10px 0}}.code{{font-size:12px;max-height:62vh}}.codeline{{grid-template-columns:42px max-content}}.topnav{{padding:8px;gap:6px}}.topnav a{{font-size:13px;padding:7px 10px}}}}
</style>
</head>
<body>
<header>
  <h1>Kịch bản trình bày code Lab 3-7</h1>
  <p>File này được làm lại theo kiểu dễ đọc trên điện thoại: mỗi cell có phần <b>em trình bày với cô như sau</b>, các cụm code cần chỉ, câu trả lời nếu cô hỏi thêm, và code gốc để đối chiếu.</p>
  <p class='note'>Code trong mục “Code gốc” được lấy trực tiếp từ notebook hiện tại, không viết lại thuật toán khác.</p>
  <div class='controls'>
    <button onclick="document.querySelectorAll('details.cell').forEach(x=>x.open=true)">Mở tất cả cell</button>
    <button onclick="document.querySelectorAll('details.cell').forEach(x=>x.open=false)">Đóng tất cả cell</button>
    <button onclick="document.querySelectorAll('details.codebox').forEach(x=>x.open=!x.open)">Bật/tắt code gốc</button>
  </div>
</header>
<nav class='topnav'>{nav}</nav>
<main>{sections}</main>
</body>
</html>
"""

OUT.write_text(page, encoding="utf-8")
print(f"Wrote {OUT}")
print(f"Size: {OUT.stat().st_size} bytes")
