import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

data = pd.read_csv("ds2os_coded1.csv")


feature=['accessedNodeAddress_code','accessedNodeType_code','timestamp','sourceID_code','sourceAddress_code','sourceType_code','sourceLocation_code','destinationServiceAddress_code','destinationServiceType_code','destinationLocation_code']
y=data['normality_code']
print(data.normality_code.unique())
x=data[feature]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)

gnb=GaussianNB()
gnb.fit(x_train,y_train)

y_pred=gnb.predict(x_test)

print(y_pred)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


