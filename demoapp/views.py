from django.shortcuts import render

# Create your views here.
def load_homepage(request):
    return render(request,'homepage.html')
def load_subpage(request):
    return render(request,'sub.html')

def mul_two_nos(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    mul=n1*n2
    return render(request,'result.html',{'res':mul})