from django.shortcuts import render
import datetime
def home(request):
    name='srikanth'
    time=datetime.datetime.now()
    pydist={'name':name,'time':time}

    return render(request,'myapp/welcome.html',context=pydist)
