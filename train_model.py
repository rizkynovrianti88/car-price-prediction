import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("clean_car_data.csv")

# ======================
# CLEANING
# ======================
df = df.drop(columns=["Car_ID"], errors="ignore")
# ======================
# SPLIT FITUR & TARGET
# ======================
X = df.drop("Price", axis=1)
y = df["Price"]

# ======================
# CATEGORICAL & NUMERICAL
# ======================
cat_cols = X.select_dtypes(include=["object"]).columns
num_cols = X.select_dtypes(exclude=["object"]).columns

# ======================
# PREPROCESSOR
# ======================
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ("num", "passthrough", num_cols)
])

# ======================
# PIPELINE MODEL
# ======================
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# ======================
# TRAIN MODEL
# ======================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)

# ======================
# SAVE MODEL
# ======================
joblib.dump(model, "model.pkl")

print("✅ model.pkl berhasil dibuat!")