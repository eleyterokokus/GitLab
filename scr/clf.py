# Пример содержимого src/clf.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_model():
    # Загрузка данных
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2
    )

    # Обучение модели
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Оценка модели
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")


if __name__ == "__main__":
    train_model()