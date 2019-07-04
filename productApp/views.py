from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    pr = Product.objects.all()
    return render(request, 'index.html', {'pr':pr})


def create(request):
    form = ProductForm(request.POST)
    if request.method == 'POST':
        form.save()
        return redirect('index')

    return render(request, 'create.html', {'form': form})


