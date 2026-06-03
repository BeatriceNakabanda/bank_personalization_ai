import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

from preprocessing import preprocess

# Load data
df = pd.read_csv("data/raw/Churn_Modelling.csv")

# Preprocess
df = preprocess(df)

# Features / Target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

#what drove churn
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print(feature_importance.head(10))

# Evaluate
predictions = model.predict(X_test)

print("Accuracy")
print(accuracy_score(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/churn_model.pkl")

print("Model saved.")