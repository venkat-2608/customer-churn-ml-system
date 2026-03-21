from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def evaluate_model(y_test, preds):

    acc = accuracy_score(y_test, preds)
    print("Accuracy:", acc)

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, preds))

    print("\nClassification Report")
    print(classification_report(y_test, preds))