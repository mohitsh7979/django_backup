from django.shortcuts import render,redirect
from .models import DataRecord
import pickle
import pandas as pd


import numpy as np
import pandas as pd
import sklearn
import pickle   

data = pd.read_csv("Social_Network_Ads.csv")
print(data.head())

x = data.iloc[:, 2:4].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

knn_ans = knn.fit(x_train, y_train)


# @app.route('/')

def home(request):
    return render(request,'index.html')

# @app.route('/predict' , method = ['POST'])
def predict(request):

    if request.method == "POST":
        a = request.POST.get('age')
        age = int(a)
        s = request.POST.get('salary')
        salary = int(s)
        print(type(salary))
        result = knn_ans.predict([[age , salary]])[0]
        DataRecord(user = request.user , age=age,salary=s,result=result).save()

        print(result,'>>>>>>>>>>>>>>')

        if result==1:
            return render(request,'index.html' , {'label':1})
        else:
            return render(request,'index.html' , {'label':-1})
    
    else:
        return redirect('/')



