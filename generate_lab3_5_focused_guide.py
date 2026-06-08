import html
import json
import re
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "LAB3_5_FOCUSED_PRESENTATION_GUIDE.html"


LABS = {
    "lab3": {
        "title": "Lab 3 - Regression Techniques",
        "path": ROOT / "Lab3" / "Lab3_Regression_Techniques.ipynb",
        "opening": (
            "Lab 3 của em tập trung vào các kỹ thuật hồi quy và Logistic Regression. "
            "Điểm chính là em tự viết các phần cốt lõi bằng NumPy: Gradient Descent cho Linear Regression, "
            "Polynomial Regression bằng cách tự tạo feature đa thức, và Softmax Logistic Regression cho bài toán Iris 3 lớp."
        ),
        "datasets": [
            {
                "name": "Auto MPG",
                "source": "UCI Machine Learning Repository",
                "file": "Lab3/data/auto-mpg.data",
                "what": (
                    "Bộ dữ liệu này mô tả thông tin xe hơi như mpg, cylinders, displacement, horsepower, weight, "
                    "acceleration, model_year, origin và tên xe. Trong lab này em dùng `mpg` làm giá trị cần dự đoán. "
                    "Vì `mpg` là số liên tục nên nó phù hợp cho bài hồi quy. Em dùng `horsepower` cho Linear Regression "
                    "và `weight` cho Polynomial Regression để minh họa quan hệ giữa đặc trưng xe và mức tiêu hao nhiên liệu."
                ),
            },
            {
                "name": "Iris",
                "source": "UCI Machine Learning Repository",
                "file": "Lab3/data/iris.data",
                "what": (
                    "Bộ Iris có 150 mẫu hoa, gồm 3 loài Setosa, Versicolor và Virginica. Mỗi mẫu có 4 đặc trưng hình học. "
                    "Trong lab này em dùng petal_length và petal_width để phân loại 3 lớp bằng Softmax Logistic Regression. "
                    "Hai đặc trưng này giúp vẽ decision boundary 2D rõ ràng khi trình bày."
                ),
            },
        ],
    },
    "lab5": {
        "title": "Lab 5 - Model Evaluation",
        "path": ROOT / "Lab5" / "Lab5_Model_Evaluation.ipynb",
        "opening": (
            "Lab 5 của em tập trung vào đánh giá mô hình trên dữ liệu mất cân bằng. "
            "Em dùng Credit Card Fraud Detection vì lớp fraud rất hiếm. Mục tiêu không chỉ là train model, "
            "mà là chứng minh vì sao accuracy chưa đủ, và vì sao cần nhìn thêm confusion matrix, precision, recall, F1, ROC và Precision-Recall."
        ),
        "datasets": [
            {
                "name": "Credit Card Fraud Detection",
                "source": "Kaggle - mlg-ulb/creditcardfraud",
                "file": "Lab1/data/creditcard.csv",
                "what": (
                    "Bộ dữ liệu này gồm các giao dịch thẻ tín dụng. Cột `Class` là nhãn: 0 là giao dịch bình thường, "
                    "1 là giao dịch gian lận. Dữ liệu phù hợp với Lab 5 vì fraud là lớp rất hiếm, nên nếu model dự đoán toàn normal "
                    "thì accuracy vẫn có thể cao nhưng thực tế lại bỏ sót fraud. Vì vậy lab này dùng nó để giải thích accuracy trap "
                    "và các metric quan trọng hơn như recall, precision và Precision-Recall curve."
                ),
            },
        ],
    },
}


CHUNKS = {
    ("lab3", 1): [
        ("Import thư viện dùng cho toàn Lab 3", 1, 5, "Đây là bước chuẩn bị công cụ. Em dùng `os` để xử lý đường dẫn, NumPy để tự viết thuật toán, pandas để đọc dữ liệu, và matplotlib để vẽ biểu đồ.")
    ],
    ("lab3", 2): [
        ("Khai báo cột và đọc Auto MPG", 1, 10, "Đoạn này lấy dữ liệu Auto MPG từ file ngoài, đặt tên cột, đọc file bằng pandas và bỏ dòng thiếu dữ liệu."),
        ("Tách X/y và chia train-test", 12, 23, "Đoạn này chọn horsepower làm đầu vào, mpg làm target, rồi tự xáo trộn index để chia train và test."),
        ("Chuẩn hóa và thêm bias", 24, 27, "Đoạn này chuẩn hóa horsepower theo mean/std của train và thêm cột bias 1 để mô hình học được hệ số chặn."),
        ("Viết hàm Batch Gradient Descent", 29, 42, "Đây là phần cốt lõi: mỗi vòng lặp dùng toàn bộ tập train để tính lỗi, tính gradient của MSE, rồi cập nhật theta."),
        ("Thử nhiều learning rate", 44, 52, "Đoạn này chạy lại Gradient Descent với nhiều learning rate để so sánh tốc độ giảm lỗi."),
        ("Vẽ biểu đồ hội tụ", 54, 58, "Đoạn này vẽ MSE theo số iteration, giúp quan sát learning rate nào hội tụ nhanh hoặc chậm."),
    ],
    ("lab3", 3): [
        ("Tạo feature đa thức thủ công", 1, 8, "Đoạn này tự tạo các cột 1, x, x^2,...,x^degree thay vì dùng PolynomialFeatures của sklearn."),
        ("Fit bằng Normal Equation", 10, 16, "Đoạn này giải trực tiếp theta bằng công thức ma trận, có regularization nhỏ để tránh lỗi nghịch đảo."),
        ("Chuẩn bị dữ liệu weight và mpg", 18, 27, "Đoạn này lấy weight làm X và mpg làm y, chuẩn hóa weight và tạo lưới điểm để vẽ đường hồi quy mượt."),
        ("Train nhiều bậc đa thức và vẽ đường hồi quy", 29, 43, "Đoạn này thử nhiều degree, fit theta, dự đoán đường cong và vẽ lên biểu đồ để so sánh độ phức tạp."),
    ],
    ("lab3", 4): [
        ("Hàm softmax và one-hot", 1, 12, "Đoạn này chuẩn bị toán cho Logistic Regression đa lớp: softmax đổi score thành xác suất, one-hot đổi nhãn thành vector."),
        ("Class LogisticRegressionScratch", 14, 53, "Đoạn này tự viết model softmax regression: khởi tạo tham số, tính xác suất, tính gradient và cập nhật weights/bias."),
        ("Hàm đánh giá tự viết", 55, 73, "Đoạn này tự tính accuracy và classification report, không dùng sklearn metrics."),
        ("Đọc Iris và chọn feature", 75, 84, "Đoạn này đọc Iris từ file ngoài, map tên lớp thành số và chọn petal_length/petal_width để vẽ được 2D."),
        ("Chia train-test stratified", 86, 101, "Đoạn này chia train/test thủ công nhưng vẫn giữ đủ tỷ lệ từng lớp hoa."),
        ("Chuẩn hóa, train và đánh giá", 103, 113, "Đoạn này chuẩn hóa dữ liệu, train Logistic Regression viết tay và in kết quả phân loại."),
        ("Vẽ decision boundary", 91, 105, "Đoạn này tạo lưới điểm 2D, dự đoán toàn bộ lưới và tô màu vùng dự đoán của từng lớp."),
    ],
    ("lab5", 1): [
        ("Import thư viện dùng cho Lab 5", 1, 4, "Đoạn này chuẩn bị công cụ đọc file, xử lý mảng, xử lý bảng và vẽ biểu đồ.")
    ],
    ("lab5", 2): [
        ("Chia train-test stratified tự viết", 1, 14, "Đoạn này tự viết hàm chia dữ liệu theo từng lớp để lớp fraud hiếm vẫn có mặt trong cả train và test."),
        ("Chuẩn hóa train-test", 16, 21, "Đoạn này chuẩn hóa dữ liệu theo mean/std của train, tránh dùng thông tin từ test."),
        ("Hàm sigmoid", 23, 25, "Đoạn này định nghĩa sigmoid để đổi logit thành xác suất lớp 1 trong Logistic Regression."),
    ],
    ("lab5", 3): [
        ("Đọc Credit Card Fraud", 1, 6, "Đoạn này xác định đường dẫn và đọc dataset fraud từ file đã có ở Lab 1."),
        ("Lấy mẫu normal và giữ fraud", 7, 10, "Đoạn này lấy toàn bộ fraud và sample 20.000 normal để giữ bài toán mất cân bằng nhưng notebook chạy nhanh hơn."),
        ("Tạo X/y và in tỷ lệ fraud", 12, 15, "Đoạn này chọn các feature đầu vào, lấy Class làm y và in tỷ lệ fraud để thấy dữ liệu mất cân bằng."),
    ],
    ("lab5", 4): [
        ("Khai báo class Logistic Regression", 1, 7, "Đoạn này tạo class model và lưu các tham số như learning rate, số epoch, class_weight."),
        ("Hàm fit: thêm bias và tạo trọng số lớp", 9, 18, "Đoạn này thêm cột bias, khởi tạo theta và nếu dùng balanced thì tăng trọng số cho lớp fraud hiếm."),
        ("Hàm fit: vòng lặp gradient descent", 19, 27, "Đây là phần train: tính xác suất, tính lỗi có trọng số, tính gradient và cập nhật theta."),
        ("Predict probability và predict nhãn", 29, 34, "Đoạn này dùng theta đã học để tính xác suất rồi đổi thành nhãn 0/1 theo threshold."),
        ("Train baseline và balanced", 36, 38, "Đoạn này chia dữ liệu, chuẩn hóa và train hai mô hình để so sánh ảnh hưởng của class_weight."),
    ],
    ("lab5", 5): [
        ("Tính TP, TN, FP, FN", 1, 6, "Đoạn này tự đếm 4 ô của confusion matrix để làm nền cho các metric."),
        ("Tính accuracy, precision, recall, F1", 7, 13, "Đoạn này tính các metric quan trọng, đặc biệt precision/recall cho lớp fraud."),
        ("In metric cho hai mô hình", 15, 15, "Đoạn này chạy metric cho baseline và balanced để so sánh."),
    ],
    ("lab5", 6): [
        ("Hàm vẽ confusion matrix", 1, 12, "Đoạn này biến các metric TP/TN/FP/FN thành ma trận 2x2 và ghi số lên hình."),
        ("Vẽ baseline và balanced cạnh nhau", 14, 16, "Đoạn này vẽ hai confusion matrix để nhìn trực quan model nào bắt fraud tốt hơn."),
    ],
    ("lab5", 7): [
        ("Tự tính điểm ROC và PR theo threshold", 1, 15, "Đoạn này quét nhiều threshold, mỗi threshold tạo dự đoán mới rồi tính FPR, TPR, precision, recall."),
        ("Vẽ ROC và Precision-Recall", 17, 30, "Đoạn này lấy xác suất của hai model rồi vẽ ROC và Precision-Recall để so sánh."),
    ],
}


DEEP = {
    ("lab3", 2): "Cell này là phần quan trọng nhất của Linear Regression viết tay. Khi trình bày, em nhấn mạnh rằng Batch Gradient Descent dùng toàn bộ tập train trong mỗi lần cập nhật. MSE giảm theo iteration chứng minh model đang học dần tham số tốt hơn.",
    ("lab3", 3): "Ý cần nói là Polynomial Regression không phải model hoàn toàn khác Linear Regression; nó vẫn tuyến tính theo theta, nhưng X được mở rộng thành các lũy thừa nên đường dự đoán có thể cong.",
    ("lab3", 4): "Vì Iris có 3 lớp nên dùng softmax thay vì sigmoid. Softmax trả về xác suất cho từng lớp, sau đó lấy argmax để chọn lớp có xác suất cao nhất.",
    ("lab5", 2): "Các hàm tiện ích này giúp Lab 5 không phụ thuộc sklearn ở phần chia dữ liệu, chuẩn hóa và sigmoid. Đây là nền để nói rằng em hiểu rõ quy trình evaluation.",
    ("lab5", 4): "Điểm quan trọng là class_weight balanced. Vì fraud rất ít, nếu không tăng trọng số thì model dễ thiên về normal. Balanced làm lỗi fraud có ảnh hưởng lớn hơn khi cập nhật theta.",
    ("lab5", 5): "Metric cần nhấn mạnh là recall và precision. Recall cao nghĩa là bắt được nhiều fraud thật; precision cao nghĩa là các cảnh báo fraud ít bị nhầm.",
    ("lab5", 7): "ROC và Precision-Recall đều quét threshold. Với dữ liệu mất cân bằng, Precision-Recall thường dễ đọc hơn vì nó tập trung vào lớp fraud hiếm.",
}


CELL_OVERVIEW = {
    ("lab3", 1): (
        "Ở cell này, em chỉ import các thư viện cần dùng cho Lab 3. "
        "Cụ thể, `os` để xử lý đường dẫn dataset, `numpy` để tự viết các phép toán vector và ma trận, "
        "`pandas` để đọc dữ liệu dạng bảng, còn `matplotlib` để vẽ loss, đường hồi quy và decision boundary. "
        "Cell này chưa xử lý dữ liệu hay train mô hình, nó chỉ chuẩn bị môi trường cho các cell phía sau."
    ),
    ("lab3", 2): (
        "Ở cell này, em làm Linear Regression bằng Batch Gradient Descent trên bộ Auto MPG. "
        "Đầu tiên em đọc dữ liệu từ file UCI, lấy `horsepower` làm biến đầu vào và `mpg` làm giá trị cần dự đoán. "
        "Sau đó em tự chia train-test, tự chuẩn hóa dữ liệu, thêm bias, rồi viết hàm Gradient Descent để học tham số `theta`. "
        "Cuối cell, em chạy nhiều learning rate khác nhau để so sánh tốc độ hội tụ qua biểu đồ MSE."
    ),
    ("lab3", 3): (
        "Ở cell này, em làm Polynomial Regression viết tay. "
        "Ý tưởng là thay vì chỉ dùng một biến `weight`, em tự tạo thêm các biến lũy thừa như `weight^2`, `weight^3` để mô hình học được quan hệ cong giữa cân nặng xe và MPG. "
        "Sau đó em dùng Normal Equation để tìm tham số, không dùng `PolynomialFeatures` hay `LinearRegression` của sklearn. "
        "Cuối cùng em vẽ nhiều đường hồi quy với các bậc khác nhau để so sánh độ phức tạp của mô hình."
    ),
    ("lab3", 4): (
        "Ở cell này, em làm Logistic Regression đa lớp cho bộ Iris. "
        "Vì Iris có 3 loài hoa nên em dùng softmax thay vì sigmoid nhị phân. "
        "Em tự viết hàm softmax, one-hot label, class `LogisticRegressionScratch`, rồi train bằng gradient descent. "
        "Sau khi train, em tự in classification report và vẽ decision boundary để thấy mô hình chia vùng dự đoán cho từng loài hoa như thế nào."
    ),
    ("lab5", 1): (
        "Ở cell này, em import các thư viện cần dùng cho Lab 5. "
        "`os` dùng để lấy đường dẫn file credit card, `numpy` để tự tính metric và Logistic Regression, `pandas` để đọc dữ liệu, còn `matplotlib` để vẽ confusion matrix, ROC và Precision-Recall. "
        "Cell này chỉ là bước chuẩn bị."
    ),
    ("lab5", 2): (
        "Ở cell này, em tự viết các hàm tiện ích thay cho sklearn. "
        "Hàm `train_test_split_np` chia dữ liệu theo từng lớp để giữ tỷ lệ fraud và normal trong train/test. "
        "Hàm `standardize_train_test` chuẩn hóa dữ liệu theo thống kê của tập train để tránh data leakage. "
        "Hàm `sigmoid` dùng cho Logistic Regression để đổi đầu ra tuyến tính thành xác suất."
    ),
    ("lab5", 3): (
        "Ở cell này, em đọc bộ Credit Card Fraud Detection từ file của Lab 1. "
        "Vì dữ liệu gốc rất lớn và fraud là lớp hiếm, em lấy toàn bộ fraud nhưng chỉ sample 20.000 giao dịch normal để notebook chạy nhanh hơn mà vẫn giữ được tình huống mất cân bằng. "
        "Sau đó em tạo ma trận đặc trưng `X` gồm Time, Amount và V1 đến V28, còn `y` là nhãn Class."
    ),
    ("lab5", 4): (
        "Ở cell này, em tự viết Logistic Regression nhị phân để phân loại fraud và normal. "
        "Trong hàm `fit`, model thêm bias, khởi tạo theta, tính xác suất bằng sigmoid, tính lỗi và gradient rồi cập nhật theta qua nhiều epoch. "
        "Điểm quan trọng là em train hai phiên bản: baseline bình thường và bản `class_weight='balanced'` để xử lý lớp fraud hiếm."
    ),
    ("lab5", 5): (
        "Ở cell này, em tự tính các chỉ số đánh giá từ confusion matrix. "
        "Em đếm TP, TN, FP, FN rồi tính accuracy, precision, recall và F1. "
        "Với bài fraud detection, em nhấn mạnh recall và precision quan trọng hơn accuracy, vì fraud là lớp ít nhưng rất quan trọng."
    ),
    ("lab5", 6): (
        "Ở cell này, em vẽ confusion matrix cho baseline và balanced model. "
        "Mục đích là nhìn trực tiếp mô hình dự đoán đúng normal, đúng fraud, báo động nhầm và bỏ sót fraud bao nhiêu trường hợp. "
        "Phần này giúp giải thích vì sao chỉ nhìn accuracy là chưa đủ với dữ liệu mất cân bằng."
    ),
    ("lab5", 7): (
        "Ở cell này, em tự tính ROC curve và Precision-Recall curve bằng cách quét nhiều threshold. "
        "Mỗi threshold tạo ra một bộ dự đoán khác nhau, từ đó tính FPR, TPR, precision và recall. "
        "Em vẽ hai đường này để so sánh baseline và balanced model, trong đó Precision-Recall đặc biệt quan trọng vì tập trung vào lớp fraud hiếm."
    ),
}


def load_code_cells(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    result = []
    order = 0
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "code":
            order += 1
            result.append((order, idx, "".join(cell.get("source", []))))
    return result


CELL_LABELS = {
    ("lab3", 1): "Cell 1 - Import thư viện",
    ("lab3", 2): "Cell 2 - Linear Regression và Batch Gradient Descent",
    ("lab3", 3): "Cell 3 - Polynomial Regression viết tay",
    ("lab3", 4): "Cell 4 - Logistic Regression Iris",
    ("lab5", 1): "Cell 1 - Import thư viện",
    ("lab5", 2): "Cell 2 - Hàm chia dữ liệu, chuẩn hóa và sigmoid",
    ("lab5", 3): "Cell 3 - Đọc Credit Card Fraud",
    ("lab5", 4): "Cell 4 - Logistic Regression cho dữ liệu mất cân bằng",
    ("lab5", 5): "Cell 5 - Tự tính confusion matrix và metric",
    ("lab5", 6): "Cell 6 - Vẽ confusion matrix",
    ("lab5", 7): "Cell 7 - ROC và Precision-Recall",
}


def cell_label(lab_id, order):
    return CELL_LABELS.get((lab_id, order), f"Cell {order}")


def comment_for_line(line):
    s = line.strip()
    low = s.lower()
    if not s:
        return "Dòng trống để tách các khối code cho dễ đọc."
    if s.startswith("#"):
        return "Chú thích mô tả mục đích của đoạn code ngay phía dưới."
    if s.startswith(("\"\"\"", "'''")):
        return "Docstring giải thích nhanh chức năng của hàm hoặc đoạn code."
    if s.startswith("import "):
        return "Import thư viện để dùng các hàm/class của thư viện đó."
    if s.startswith("from "):
        return "Import trực tiếp class hoặc hàm cần dùng từ một thư viện."
    if s.startswith("def "):
        name = s.split("(")[0].replace("def", "").strip()
        return f"Định nghĩa hàm `{name}` để gom một chức năng riêng và gọi lại nhiều lần."
    if s.startswith("class "):
        name = s.split(":")[0].replace("class", "").strip()
        return f"Định nghĩa class `{name}` để đóng gói thuật toán, tham số và các hàm fit/predict."
    if s.startswith("return "):
        return "Trả kết quả từ hàm về nơi gọi hàm."
    if s.startswith("for "):
        return "Bắt đầu vòng lặp để xử lý lần lượt từng phần tử hoặc từng giá trị."
    if s.startswith("if "):
        return "Kiểm tra điều kiện; nếu điều kiện đúng thì chạy khối code bên trong."
    if s.startswith("else"):
        return "Nhánh còn lại khi điều kiện phía trên không đúng."
    if s.startswith("raise "):
        return "Chủ động báo lỗi để dừng chương trình khi dữ liệu hoặc điều kiện không hợp lệ."
    if "pd.read_csv" in s:
        return "Đọc file dữ liệu vào DataFrame pandas để bắt đầu xử lý dataset."
    if "os.path.join" in s:
        return "Ghép các phần đường dẫn file theo cách an toàn trên hệ điều hành."
    if "delim_whitespace" in s:
        return "Báo cho pandas biết file được phân tách bằng khoảng trắng."
    if "names=" in s:
        return "Gán tên cột cho dataset vì file gốc không có header rõ ràng."
    if "na_values" in s:
        return "Quy định ký tự `?` là giá trị thiếu để pandas nhận diện NaN."
    if "dropna" in s:
        return "Bỏ các dòng có giá trị thiếu để tránh lỗi khi tính toán."
    if ".to_numpy" in s:
        return "Chuyển dữ liệu từ pandas sang NumPy array để thuật toán viết tay xử lý được."
    if "reshape" in s:
        return "Đưa mảng về đúng dạng cột/hàng để nhân ma trận không bị sai kích thước."
    if "default_rng" in s:
        return "Tạo bộ sinh số ngẫu nhiên có seed để kết quả chia dữ liệu lặp lại được."
    if "permutation" in s or "shuffle" in s:
        return "Xáo trộn chỉ số để train/test không phụ thuộc thứ tự dữ liệu ban đầu."
    if "split =" in s:
        return "Tính vị trí cắt để chia dữ liệu thành train và test."
    if "train_idx" in s or "test_idx" in s:
        return "Tạo hoặc dùng danh sách chỉ số cho tập train và tập test."
    if "mean" in low and ".mean" in low:
        return "Tính giá trị trung bình để chuẩn hóa dữ liệu."
    if "std" in low and ".std" in low:
        return "Tính độ lệch chuẩn để chuẩn hóa dữ liệu."
    if " / std" in s or "- mean" in s:
        return "Chuẩn hóa feature theo công thức (x - mean) / std."
    if "np.c_" in s:
        return "Ghép thêm cột hoặc ma trận, thường dùng để thêm bias hoặc tạo feature mới."
    if "np.ones" in s:
        return "Tạo mảng toàn số 1, thường dùng làm cột bias hoặc cột x^0."
    if "np.zeros" in s:
        return "Khởi tạo mảng toàn số 0 để lưu tham số, vector one-hot hoặc bộ đếm."
    if "dot(" in s or " @ " in s:
        return "Thực hiện nhân ma trận/vector, phần cốt lõi trong dự đoán và tính gradient."
    if "error =" in s:
        return "Tính sai số giữa dự đoán của model và giá trị thật."
    if "grad" in low:
        return "Tính gradient, tức hướng thay đổi của loss theo tham số."
    if "theta" in s and "=" in s:
        return "Khởi tạo hoặc cập nhật tham số theta của mô hình hồi quy/logistic."
    if "learning_rate" in s or "lr" in s:
        return "Thiết lập hoặc dùng learning rate, tức độ lớn bước cập nhật tham số."
    if "mse" in low or "cost" in low or "loss" in low:
        return "Tính hoặc lưu lỗi của mô hình để theo dõi quá trình học."
    if "softmax" in low:
        return "Tính hoặc dùng softmax để biến score nhiều lớp thành xác suất."
    if "one_hot" in low:
        return "Biểu diễn nhãn lớp thành vector one-hot cho bài toán nhiều lớp."
    if "sigmoid" in low:
        return "Dùng sigmoid để đổi logit thành xác suất lớp 1."
    if "class_weight" in s or "sample_weight" in s:
        return "Xử lý mất cân bằng lớp bằng cách tăng trọng số cho lớp hiếm."
    if "np.bincount" in s:
        return "Đếm số mẫu của từng lớp để tính trọng số hoặc thống kê nhãn."
    if "predict_proba" in s:
        return "Tính xác suất dự đoán thay vì chỉ trả nhãn 0/1."
    if "predict" in low:
        return "Dự đoán nhãn hoặc giá trị dựa trên tham số/model đã học."
    if "tp =" in low:
        return "Đếm true positive: fraud thật và model cũng dự đoán fraud."
    if "tn =" in low:
        return "Đếm true negative: normal thật và model dự đoán normal."
    if "fp =" in low:
        return "Đếm false positive: normal thật nhưng model báo fraud."
    if "fn =" in low:
        return "Đếm false negative: fraud thật nhưng model bỏ sót."
    if "precision" in low:
        return "Tính precision: trong các dự đoán fraud, có bao nhiêu dự đoán đúng."
    if "recall" in low:
        return "Tính recall: trong các fraud thật, model bắt được bao nhiêu."
    if "f1" in low:
        return "Tính F1-score, trung hòa giữa precision và recall."
    if "threshold" in low:
        return "Thiết lập hoặc quét ngưỡng để đổi xác suất thành nhãn dự đoán."
    if "fpr" in low or "tpr" in low:
        return "Tính điểm cho ROC curve: FPR là báo động nhầm, TPR là recall."
    if "plt." in s or "ax." in s:
        return "Lệnh matplotlib để vẽ hoặc chỉnh biểu đồ."
    if "meshgrid" in s:
        return "Tạo lưới điểm 2D để vẽ decision boundary."
    if "contourf" in s:
        return "Tô màu các vùng dự đoán trên mặt phẳng decision boundary."
    if "scatter" in s:
        return "Vẽ các điểm dữ liệu thật lên biểu đồ."
    if "=" in s:
        left = s.split("=", 1)[0].strip()
        return f"Gán kết quả bên phải vào `{left}` để dùng ở các bước sau."
    return "Thực hiện một bước xử lý trong cell; kết quả phục vụ cho đoạn code phía sau."


def code_with_comments(src, start, end):
    lines = src.splitlines()
    rows = []
    for line_no in range(start, end + 1):
        line = lines[line_no - 1] if line_no - 1 < len(lines) else ""
        rows.append(
            "<div class='code-row'>"
            f"<div class='ln'>{line_no}</div>"
            f"<pre><code>{html.escape(line)}</code></pre>"
            f"<div class='comment'>{html.escape(comment_for_line(line))}</div>"
            "</div>"
        )
    return "\n".join(rows)


def chunk_extra_notes_items(title, speech, src, start, end):
    block = "\n".join(src.splitlines()[start - 1:end]).lower()
    notes = []
    title_l = title.lower()
    if "đọc" in title_l or "khai báo cột" in title_l:
        notes.append("Đầu tiên em luôn nói rõ dữ liệu đi từ đâu vào: file nào, đọc bằng hàm nào, và sau khi đọc thì dữ liệu nằm trong biến nào.")
        notes.append("Nếu đoạn này có `dropna`, em giải thích là vì dữ liệu thô có thể bị thiếu, nên cần làm sạch trước khi đưa vào mô hình.")
    if "chia train" in title_l or "train-test" in title_l:
        notes.append("Điểm cần nhấn mạnh là train dùng để học tham số, test dùng để kiểm tra sau khi học xong. Không được dùng test để tính tham số chuẩn hóa hoặc train model.")
        notes.append("Việc xáo trộn index giúp dữ liệu test không bị lệ thuộc vào thứ tự ban đầu trong file.")
    if "chuẩn hóa" in title_l:
        notes.append("Chuẩn hóa giúp các giá trị đầu vào có thang đo gần nhau hơn. Với Gradient Descent, điều này làm quá trình giảm loss ổn định và nhanh hơn.")
        notes.append("Cột bias toàn số 1 giúp mô hình học được hệ số chặn, tức đường hồi quy không bắt buộc đi qua gốc tọa độ.")
    if "gradient descent" in title_l:
        notes.append("Batch Gradient Descent nghĩa là mỗi lần cập nhật theta, em dùng toàn bộ tập train để tính gradient. Vì dùng toàn bộ dữ liệu nên đường loss thường mượt và ổn định hơn.")
        notes.append("Công thức chính là: dự đoán -> tính lỗi -> tính gradient -> cập nhật theta. Learning rate quyết định bước cập nhật lớn hay nhỏ.")
    if "learning rate" in title_l:
        notes.append("Mỗi learning rate tạo ra một đường loss riêng. Đường nào xuống nhanh và không dao động thì learning rate đó tốt trong thí nghiệm này.")
        notes.append("Không nên nói learning rate lớn luôn tốt; phải nói nó tốt trong biểu đồ này vì loss giảm nhanh mà vẫn ổn định.")
    if "biểu đồ" in title_l or "vẽ" in title_l:
        notes.append("Khi trình bày hình, em nói rõ trục X là gì, trục Y là gì, mỗi màu/đường biểu diễn gì, và kết luận chính rút ra từ hình.")
    if "đa thức" in title_l or "polynomial" in title_l:
        notes.append("Polynomial Regression vẫn là Linear Regression theo tham số theta, nhưng dữ liệu đầu vào đã được mở rộng thành các lũy thừa để tạo đường cong.")
        notes.append("Bậc càng cao thì mô hình càng linh hoạt, nhưng nếu quá cao có thể bám nhiễu và overfit.")
    if "normal equation" in title_l:
        notes.append("Normal Equation là cách giải trực tiếp theta bằng công thức ma trận, không cần lặp như Gradient Descent.")
        notes.append("Regularization nhỏ được thêm vào để phép nghịch đảo ổn định hơn khi ma trận khó nghịch đảo.")
    if "softmax" in title_l or "one-hot" in title_l:
        notes.append("Softmax dùng cho bài toán nhiều lớp. Nó biến score của từng lớp thành xác suất, tổng xác suất bằng 1.")
        notes.append("One-hot biến nhãn số thành vector để so sánh với xác suất softmax khi tính lỗi.")
    if "logisticregressionscratch" in title_l or "class logistic" in title_l:
        notes.append("Trong class này, `weights` và `bias` là tham số model học được. `fit` là nơi học tham số, còn `predict` là nơi dùng tham số đã học để dự đoán.")
        notes.append("Gradient được tính từ chênh lệch giữa xác suất dự đoán và nhãn one-hot, rồi cập nhật weights/bias sau mỗi vòng lặp.")
    if "iris" in title_l:
        notes.append("Iris có 3 lớp nên phải dùng softmax thay vì sigmoid nhị phân. Chọn 2 feature petal giúp vẽ decision boundary trên mặt phẳng 2D.")
    if "credit card" in title_l or "fraud" in title_l:
        notes.append("Bộ credit card phù hợp vì lớp fraud rất hiếm. Đây là lý do Lab 5 không nên chỉ nhìn accuracy.")
        notes.append("Lấy mẫu normal giúp notebook chạy nhanh hơn nhưng vẫn giữ được tình huống mất cân bằng.")
    if "class_weight" in title_l or "trọng số" in title_l:
        notes.append("class_weight balanced làm mẫu fraud có trọng số lớn hơn trong loss. Nhờ vậy model chú ý hơn đến lỗi bỏ sót fraud.")
        notes.append("Baseline và balanced được train song song để so sánh xem xử lý mất cân bằng có cải thiện recall fraud không.")
    if "metric" in title_l or "tp" in block or "precision" in block:
        notes.append("TP, TN, FP, FN là nền của mọi metric phân loại. Với fraud, FN là nguy hiểm vì đó là fraud thật nhưng model bỏ sót.")
        notes.append("Precision trả lời: trong các cảnh báo fraud, bao nhiêu cái đúng. Recall trả lời: trong các fraud thật, bắt được bao nhiêu.")
    if "confusion" in title_l:
        notes.append("Confusion matrix giúp nhìn số lượng lỗi cụ thể, dễ giải thích hơn một con số accuracy.")
        notes.append("Khi chỉ hình, em đọc theo hàng là nhãn thật, cột là nhãn dự đoán.")
    if "roc" in title_l or "precision-recall" in title_l:
        notes.append("ROC và Precision-Recall được tạo bằng cách thay đổi threshold. Mỗi threshold cho một bộ precision/recall hoặc FPR/TPR khác nhau.")
        notes.append("Với dữ liệu mất cân bằng, Precision-Recall thường quan trọng hơn vì tập trung vào lớp fraud hiếm.")
    if not notes:
        notes.append("Khi trình bày cụm này, em nói theo thứ tự: đầu vào là gì, đoạn code xử lý gì, biến nào được tạo ra, và biến đó dùng cho bước nào tiếp theo.")
    return notes


def chunk_extra_notes(title, speech, src, start, end):
    notes = chunk_extra_notes_items(title, speech, src, start, end)
    return "".join(f"<li>{html.escape(note)}</li>" for note in notes)


def chunk_dialogue(title, speech, src, start, end):
    notes = chunk_extra_notes_items(title, speech, src, start, end)
    clean_notes = []
    for note in notes[:3]:
        text = note
        text = text.replace("Đầu tiên em luôn nói rõ", "Ở đây em xác định rõ")
        text = text.replace("Khi cô hỏi, em chỉ cần nói", "Hàm này cần hiểu theo ba ý:")
        text = text.replace("Khi trình bày hình, em nói rõ", "Ở biểu đồ này, em xác định")
        text = text.replace("Khi chỉ hình, em đọc theo", "Em đọc hình theo")
        text = text.replace("Khi trình bày cụm này, em nói theo thứ tự:", "Cụm này có thể hiểu theo thứ tự:")
        text = text.replace("Khi trình bày,", "")
        text = text.replace("em nói rõ thêm rằng", "")
        clean_notes.append(text.strip())
    detail = " ".join(clean_notes)
    return f"{speech} {detail}"


def dataset_html(lab):
    cards = []
    for ds in lab["datasets"]:
        cards.append(
            f"<article class='dataset'><h4>{html.escape(ds['name'])}</h4>"
            f"<p><b>Nguồn:</b> {html.escape(ds['source'])}</p>"
            f"<p><b>File:</b> <code>{html.escape(ds['file'])}</code></p>"
            f"<p>{html.escape(ds['what'])}</p></article>"
        )
    return "\n".join(cards)


def cell_html(lab_id, order, src):
    chunks = CHUNKS[(lab_id, order)]
    deep = DEEP.get((lab_id, order), "Cell này là một phần trong quy trình chính của lab. Khi trình bày, em nói nó nhận dữ liệu gì, xử lý gì và tạo ra kết quả gì cho bước sau.")
    overview = CELL_OVERVIEW[(lab_id, order)]
    label = cell_label(lab_id, order)
    cards = []
    max_line = len(src.splitlines())
    for idx, (title, start, end, speech) in enumerate(chunks, 1):
        start = max(1, min(start, max_line))
        end = max(start, min(end, max_line))
        cards.append(
            f"<article class='chunk'><h4>Cụm {idx}: {html.escape(title)}</h4>"
            f"<div class='dialogue'><h5>Đoạn thoại nên đọc khi tới cụm này</h5><p>{html.escape(chunk_dialogue(title, speech, src, start, end))}</p></div>"
            f"<details class='extra-help'><summary>Nếu cô hỏi sâu hơn về cụm này</summary><div class='more-talk'><ul>{chunk_extra_notes(title, speech, src, start, end)}</ul></div></details>"
            f"<details class='line-help'><summary>Nếu cô hỏi từng dòng code thì mở phần này</summary><div class='annotated'>{code_with_comments(src, start, end)}</div></details></article>"
        )
    return (
        f"<details class='cell' id='{lab_id}-cell-{order}' open><summary>{html.escape(label)}</summary>"
        f"<div class='cell-overview'><h3>Em trình bày với cô như sau</h3><p>{html.escape(overview)}</p></div>"
        f"<div class='deep'><b>Ý chính của cell:</b> {html.escape(deep)}</div>"
        + "\n".join(cards)
        + f"<details class='full'><summary>Code gốc toàn cell</summary><pre><code>{html.escape(src)}</code></pre></details>"
        + "</details>"
    )


def lab_html(lab_id, lab):
    cells = []
    for order, _idx, src in load_code_cells(lab["path"]):
        cells.append(cell_html(lab_id, order, src))
    return (
        f"<section class='lab' id='{lab_id}'><h2>{html.escape(lab['title'])}</h2>"
        f"<div class='opening'><h3>Mở đầu lab, em trình bày</h3><p>{html.escape(lab['opening'])}</p></div>"
        f"<div class='datasets'><h3>Dataset dùng trong lab</h3>{dataset_html(lab)}</div>"
        + "\n".join(cells)
        + "</section>"
    )


def nav_html():
    groups = []
    for lab_id, lab in LABS.items():
        links = [f"<a class='lab-top' href='#{lab_id}'>Đầu {html.escape(lab['title'])}</a>"]
        for order, _idx, _src in load_code_cells(lab["path"]):
            links.append(
                f"<a href='#{lab_id}-cell-{order}'>{html.escape(cell_label(lab_id, order))}</a>"
            )
        groups.append(
            f"<details class='nav-lab'><summary>{html.escape(lab['title'])}</summary>"
            f"<div class='nav-cells'>{''.join(links)}</div></details>"
        )
    return "".join(groups)


nav = nav_html()
content = "".join(lab_html(lab_id, lab) for lab_id, lab in LABS.items())

page = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hướng dẫn vấn đáp Lab 3 và Lab 5</title>
<style>
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:88px}}
body{{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;background:#f3f6f8;color:#17202a;line-height:1.65}}
header{{background:#142033;color:white;padding:18px 15px}}
header h1{{margin:0 0 8px;font-size:24px;line-height:1.2}}
header p{{margin:6px 0;color:#dce6f2}}
.switcher{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}}
.switcher a{{display:inline-block;text-decoration:none;border:1px solid #8fb5ff;border-radius:999px;padding:8px 12px;font-weight:900;background:#fff;color:#123a6f}}
.switcher a.active{{background:#0f766e;color:white;border-color:#0f766e}}
nav{{position:sticky;top:0;z-index:10;display:flex;gap:8px;overflow-x:auto;align-items:flex-start;background:white;border-bottom:1px solid #d7dde6;padding:9px}}
.nav-lab{{flex:0 0 auto;border:1px solid #cbd5e1;border-radius:999px;background:#f8fafc;max-width:88vw}}
.nav-lab[open]{{border-radius:14px;background:white;box-shadow:0 8px 22px rgba(15,23,42,.12)}}
.nav-lab>summary{{cursor:pointer;list-style:none;padding:8px 12px;color:#0f766e;font-weight:900;white-space:nowrap}}
.nav-lab>summary::-webkit-details-marker{{display:none}}
.nav-lab>summary::after{{content:" ▾";font-size:13px;color:#64748b}}
.nav-lab[open]>summary::after{{content:" ▴"}}
.nav-cells{{display:grid;gap:7px;padding:8px;min-width:260px;max-height:56vh;overflow:auto}}
.nav-cells a{{display:block;border:1px solid #cbd5e1;border-radius:9px;padding:9px 10px;text-decoration:none;color:#17202a;font-weight:800;background:#f8fafc;line-height:1.35}}
.nav-cells a.lab-top{{background:#ecfdf5;color:#0f766e;border-color:#99f6e4}}
main{{max-width:1180px;margin:0 auto;padding:12px}}
.lab{{background:white;border:1px solid #d7dde6;border-radius:13px;padding:14px;margin-bottom:16px}}
.lab,.cell{{scroll-margin-top:88px}}
.lab h2{{margin:0 0 12px;border-bottom:2px solid #e5eaf0;padding-bottom:8px}}
.opening,.datasets,.deep,.cell-overview{{border:1px solid #d7dde6;border-left:5px solid #0f766e;border-radius:10px;background:#f8fffd;padding:12px;margin:12px 0}}
.cell-overview{{background:#f0fdfa}}
.cell-overview h3{{margin:0 0 8px;font-size:16px}}
.dataset{{background:#fff;border:1px solid #d7dde6;border-radius:10px;padding:10px;margin:10px 0}}
.dataset h4{{margin:0 0 5px;color:#0f766e}}
.cell{{border:1px solid #cbd5e1;border-radius:12px;margin:14px 0;overflow:hidden;background:#fff}}
.cell>summary{{cursor:pointer;background:#eaf1f8;padding:13px;font-size:18px;font-weight:900}}
.chunk{{border:1px solid #fed7aa;border-radius:11px;background:#fffaf4;margin:12px;padding:12px}}
.chunk h4{{margin:0 0 8px;color:#92400e}}
.speech-line{{background:#fffbeb;border-left:4px solid #f59e0b;border-radius:8px;padding:9px;margin:8px 0}}
.dialogue{{background:#ecfdf5;border:1px solid #99f6e4;border-left:5px solid #0f766e;border-radius:10px;padding:11px;margin:9px 0}}
.dialogue h5{{margin:0 0 7px;font-size:16px;color:#065f46}}
.dialogue p{{margin:0;font-size:16px;line-height:1.75}}
.extra-help{{margin-top:10px;border:1px solid #bae6fd;border-radius:10px;overflow:hidden;background:#f0f9ff}}
.extra-help>summary{{cursor:pointer;padding:10px 12px;font-weight:900;color:#075985;background:#f0f9ff}}
.more-talk{{background:#f0f9ff;border:1px solid #bae6fd;border-radius:9px;padding:9px;margin:9px 0}} .more-talk ul{{margin:6px 0 0;padding-left:20px}}
.line-help{{margin-top:10px;border:1px solid #cbd5e1;border-radius:10px;overflow:hidden;background:#f8fafc}}
.line-help>summary{{cursor:pointer;padding:10px 12px;font-weight:900;color:#0f766e;background:#fff}}
.annotated{{border:1px solid #cbd5e1;border-radius:10px;overflow:visible;background:#0f172a;margin-top:10px}}
.code-row{{display:grid;grid-template-columns:44px minmax(0,1fr) minmax(320px,.9fr);border-bottom:1px solid #334155}}
.ln{{background:#111827;color:#94a3b8;text-align:right;padding:7px 8px;font-family:Consolas,monospace;user-select:none}}
.code-row pre{{margin:0;padding:7px 10px;overflow:auto;min-width:0;background:#0f172a;color:#e5e7eb;font-family:Consolas,Monaco,'Courier New',monospace;font-size:12.5px;line-height:1.45}}
.code-row code{{white-space:pre-wrap;word-break:break-word}}
.comment{{background:#f8fafc;color:#17202a;padding:7px 10px;font-size:14px;border-left:1px solid #cbd5e1}}
.comment::before{{content:"Dòng này làm gì: ";font-weight:800;color:#0f766e}}
.full{{margin:12px;border:1px solid #cbd5e1;border-radius:10px;overflow:hidden}}
.full summary{{cursor:pointer;padding:10px;background:#f8fafc;color:#0f766e;font-weight:800}}
.full pre{{margin:0;max-height:65vh;overflow:auto;background:#0f172a;color:#e5e7eb;padding:12px;font-size:12px}}
@media(max-width:760px){{
 body{{font-size:17px;line-height:1.72}}
 header h1{{font-size:21px}}
 main{{padding:9px}}
 .lab{{padding:10px;border-radius:10px}}
 .cell>summary{{font-size:17px}}
 .chunk{{margin:10px 0;padding:10px}}
 .code-row{{display:block;border-bottom:2px solid #334155}}
 .ln{{text-align:left;padding:5px 8px}}
 .code-row pre{{font-size:12px;max-width:100%;border-top:1px solid #334155}}
 .comment{{font-size:15px;border-left:0;border-top:1px solid #cbd5e1}}
}}
</style>
</head>
<body>
<header>
<h1>Hướng dẫn vấn đáp Lab 3 và Lab 5</h1>
<p>Bản này chỉ tập trung vào hai lab bạn sẽ trả lời. Code gốc trong notebook không bị sửa. Các comment từng dòng chỉ nằm trên web này để bạn đọc theo khi trình bày.</p>
<div class="switcher">
  <a class="active" href="LAB3_5_FOCUSED_PRESENTATION_GUIDE.html">Bản chi tiết Lab 3 & 5</a>
  <a href="LAB3_7_PRESENTATION_GUIDE_MOBILE.html">Bản đầy đủ Lab 3-7</a>
</div>
</header>
<nav>{nav}</nav>
<main>{content}</main>
<script>
document.querySelectorAll('.nav-cells a').forEach((link) => {{
  link.addEventListener('click', () => {{
    document.querySelectorAll('.nav-lab[open]').forEach((item) => item.removeAttribute('open'));
  }});
}});
</script>
</body>
</html>
"""

OUT.write_text(page, encoding="utf-8")
print(f"Wrote {OUT}")
print(f"Size: {OUT.stat().st_size} bytes")
