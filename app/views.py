from django.shortcuts import render

# Create your views here.
def Download_bootstrap(request):
    return render(request,'Download_bootstrap.html')
def button(request):
    return render(request,'button.html')
def card(request):
    return render(request,'card.html')
def last(request):
    return render(request,'last.html')



