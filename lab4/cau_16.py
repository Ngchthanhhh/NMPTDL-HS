# -*- coding: utf-8 -*-
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

def run(data=None):
    print("\n--- CÂU 16: TỐI ƯU HÓA SIÊU THAM SỐ (GRID SEARCH) ---")
    if data is None:
        import cau_10
        data = data = cau_10.run()
    X_train, X_test, y_train, y_test = data
    
    param_grid = {
        'n_estimators': [10, 50],
        'max_depth': [None, 5, 10]
    }
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    print(f"Tham số tốt nhất tối ưu được: {grid_search.best_params_}")
    print(f"Độ chính xác tốt nhất trên Cross-Validation: {grid_search.best_score_:.4f}")
    return grid_search.best_estimator_

if __name__ == "__main__":
    run()
