import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Load data
df = pd.read_csv('breast_cancer.csv')

# Preprocess (example)
df = df.dropna()
df['priority'] = df['diagnosis'].map({'M': 'high', 'B': 'low'})  # Example mapping

# Encode labels
df['priority'] = df['priority'].map({'high': 2, 'medium': 1, 'low': 0})

# Split
X = df.drop(['priority', 'diagnosis'], axis=1)
y = df['priority']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred, average='weighted'))