import joblib


class Inference:
    def __init__(self, model):
        self.model = model
        self.feature_names = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ]

    @classmethod
    def load_model(cls):
        model = joblib.load("trained_model.joblib")
        return cls(model)

    def predict(self, predict_request):
        input_data = [float(predict_request[name]) for name in self.feature_names]
        result = self.model.predict([input_data])

        match result[0]:
            case 0:
                return "setosa"
            case 1:
                return "versicolor"
            case 2:
                return "virginica"
        return None
