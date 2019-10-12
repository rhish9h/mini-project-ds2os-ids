from django.shortcuts import render
import pickle
import os
# import pandas as pd
# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.

# load drop down dictionary pickle
modulePath = os.path.dirname(__file__) #path name of current directory
filePath = os.path.join(modulePath, 'drop_down_pickle')
drop_file = open(filePath, 'rb')
ddown = pickle.load(drop_file)
drop_file.close()

# load knn model pickle
knn_path = os.path.join(modulePath, 'knn_model_pickle')
knn_file = open(knn_path, 'rb')
knn_model = pickle.load(knn_file)
knn_file.close()

def index(request):

  if request.method == 'POST': # --------------------------- post -------

    form_data = {
      'model': request.POST.get('modelChosen', ''),   # user ip
      'sourceID_ip': request.POST.get('sourceID', ''),
      'sourceAddress_ip': request.POST.get('sourceAddress', ''),
      'sourceType_ip': request.POST.get('sourceType', ''),
      'sourceLocation_ip': request.POST.get('sourceLocation', ''),
      'destinationServiceAddress_ip': request.POST.get('destinationServiceAddress', ''),
      'destinationServiceType_ip': request.POST.get('destinationServiceType', ''),
      'destinationLocation_ip': request.POST.get('destinationLocation', ''),
      'accessedNodeAddress': request.POST.get('accessedNodeAddress', ''),
      'accessedNodeType_ip': request.POST.get('accessedNodeType', ''),
      'operation_ip': request.POST.get('operation', ''),
      'value_ip': request.POST.get('value', ''),
      'timestamp_ip': request.POST.get('timestamp', '')
    }

    # convert form data to array of integers for processing in model
    ip_values = []
    for key, value in form_data.items():
      temp_split = value.split()
      if len(temp_split) > 1:
          ip_values.append(int(temp_split[1]))
      else:
        try: # for blank values
          ip_values.append(int(temp_split[0]))
        except:
          ip_values.append(0)
    ip_values.pop(0)

    # predict
    prediction = knn_model.predict([ip_values])
    prediction = [key for key, value in ddown['normality'].items() if value==prediction[0]][0] #reverse lookup in normality dictionary (7=normal)
    
    return render(request, 'ids_app/index.html', {'ip_values': ip_values, 'ddown': ddown, 'form_data': form_data, 'prediction': prediction})
  # template = loader.get_template('ids_app/index.html')
  # return HttpResponse(template.render())

# ------------------------------------------------------- basic get ----- display only form with drop downs

  return render(request, 'ids_app/index.html', {'ddown': ddown})