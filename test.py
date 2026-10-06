from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Learn mean and standard deviation from training data
scaler.fit(X_train_filled)

# Apply the same scaling to both datasets
X_train_scaled = scaler.transform(X_train_filled)
X_test_scaled = scaler.transform(X_test_filled)