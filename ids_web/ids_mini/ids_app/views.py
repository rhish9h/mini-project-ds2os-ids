from django.shortcuts import render
import pickle
import os
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.

def index(request):

  # load pickle
  modulePath = os.path.dirname(__file__) #path name of current directory
  filePath = os.path.join(modulePath, 'drop_down_pickle')
  drop_file = open(filePath, 'rb')
  ddown = pickle.load(drop_file)
  drop_file.close()


  if request.method == 'POST':
    model = request.POST.get('modelChosen', '')
    prediction = 'predicted value'
    return render(request, 'ids_app/index.html', {'model': model, 'ddown': ddown})
  # template = loader.get_template('ids_app/index.html')
  # return HttpResponse(template.render())

  return render(request, 'ids_app/index.html', {'ddown': ddown})