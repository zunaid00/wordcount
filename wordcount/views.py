from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    data = request.GET['fulltextarea']
    list_data = data.split()
    length = len(list_data)
    worddictionary = {}

    for word in list_data:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
        sorted_list = sorted(worddictionary.items(),key=operator.itemgetter(1))
            
    return render(request,'count.html',{'data':data,'length':length,'worddictionary':sorted_list})

def about(request):
    return render(request,'about.html')