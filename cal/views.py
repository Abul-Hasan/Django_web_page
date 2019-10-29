from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'Everyone'})

def add(request):
    val1 = int(request.POST['num1'])
    val2= int(request.POST['num2'])
    res1 = val1 +val2
    res2 = val1 - val2
    res3 = val1 * val2

    if val2 == 0:
        res4="Denomiator should not be zero"
        
    else:
        res4 = val1 / val2
        

    return render(request, "result.html", {"result1":res1,"result2":res2,"result3":res3,"result4":res4})