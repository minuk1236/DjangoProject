from django.shortcuts import render, redirect

from .models import Portfolio
from .form import PortfolioUpload

# Create your views here.

def portfolio(request):

    portfolios = Portfolio.objects

    return render(request, 'portfolio.html', {'portfolios':portfolios})

def upload(request):
    if request.method == 'POST':
        form = PortfolioUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('/portfolio/')
    else:
        form = PortfolioUpload()
        return render(request, 'upload.html',{'form':form})