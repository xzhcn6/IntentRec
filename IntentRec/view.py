from django.shortcuts import render, HttpResponse
from DataModel.models import Field, Type


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def Index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def ShowModel(request):
    return render(request, 'showModel.html')


def UploadData(request):
    type_list = Type.objects.all()
    file_list = Field.objects.all()
    print(type_list)
    context = {'type_list':type_list}
    return render(request, 'uploadData.html', context)


def Recognition(request):
    return render(request, 'recognition.html', context)
#    return HttpResponse(json.dumps(context), content_type="application/json")







