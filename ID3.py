import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('D:/Downloads/FinTech-master/test.csv')
y=np.array(df['GEI Score'])
features=list(df.columns[3:6])
x=np.array(df[features])
x_train, x_test, y_train, y_test = tts(x,y, test_size=0.33, random_state=42) 

regressor = DecisionTreeRegressor(random_state=42)
tree=regressor.fit(x_train, y_train)
y_pred=tree.predict(x_test)

score=tree.score(x_test,y_test)