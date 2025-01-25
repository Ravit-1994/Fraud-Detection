def calculate_metrics(y_true, y_pred):
    from sklearn.metrics import precision_score, recall_score, f1_score
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return precision, recall, f1
