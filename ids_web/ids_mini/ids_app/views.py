from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.

def index(request):
  # template = loader.get_template('ids_app/index.html')
  # return HttpResponse(template.render())
  return render(request, 'ids_app/index.html')