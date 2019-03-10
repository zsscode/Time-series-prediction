
from xgboost.sklearn import XGBRegressor
import scipy.stats as st
from sklearn.model_selection import RandomizedSearchCV


xgb_params={
    'booster':'gbtree',
}

class Xgb(object):
    def __init__(self):
        pass

    def build(self):
        params_sk={
            'objective':'reg:linear',
            'subsample':0.8,
            'colsample_bytree':0.85,
            'seed':42
        }
        self.model=XGBRegressor(**params_sk)

    def train(self,x_train,y_train):
        self.build()
        self.model.fit(x_train,y_train)


    def eval(self):
        pass

    def predict(self,x):
        self.model.predict(x)

    def plot(self):
        pass

    def restore(self):
        pass

    def save(self):
        pass

    def feature_importance_plot(self):
        importance=self.model.get_fscore()

    def grid_search(self,x,y):
        params_grid={
            'n_estimator':st.randint(100,500),
            'max_depth':st.randint(6,20)
        }
        search_sk=RandomizedSearchCV(self.model,params_grid,cv=5,random_state=1,n_iter=20)
        search_sk.fit(x,y)

    def random_search(self):
        pass