import xgboost as xgb

def train_xgboost(X_train, y_train, params):
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    return model
