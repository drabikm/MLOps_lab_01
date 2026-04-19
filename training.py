import joblib
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_data():
    data = load_iris()
    print(f"Target names: {data.target_names}")
    return data.data, data.target


def train_model(data, target):
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2, random_state=42
    )
    svm_model = svm.SVC(kernel="linear")
    svm_model.fit(x_train, y_train)
    y_pred_svm = svm_model.predict(x_test)
    print("Accuracy:", accuracy_score(y_test, y_pred_svm))
    return svm_model


def save_model(model) -> None:
    joblib.dump(model, filename="trained_model.joblib")


iris_dataset = load_data()

if __name__ == "__main__":
    X, y = load_data()
    m = train_model(X, y)
    save_model(m)
