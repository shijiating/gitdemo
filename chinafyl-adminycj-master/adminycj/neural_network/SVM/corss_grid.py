from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

time0=time()

gamma_range=gamma_range=np.logspace(-5,0.5,50)
C_range = np.linspace(0.01,10,50)

param_grid=dict(gamma=gamma_range
                ,C=C_range)

cv=StratifiedShuffleSplit(n_splits=10,test_size=0.2)
grid=GridSearchCV(SVC(kernel="rbf",cache_size=5000),param_grid=param_grid,cv=cv)

grid.fit(customer_data,target)
print("The best parameters are %s with a score of %0.5f" % (grid.best_params_,grid.best_score_))
print(datetime.datetime.utcfromtimestamp(time()-time0).strftime("%M:%S:%f"))