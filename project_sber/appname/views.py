from django.shortcuts import render
def personal(request):
    return render(request, 'personal.html')
def support(request):
    return render(request, 'support.html')
def transport(request):
    return render(request, 'transport.html')
# Create your views here.
