from django.shortcuts import render, redirect
# Create your views here.

from .forms import TextForm
from .models import *

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            # get datas from the news
            title = form.cleaned_data["title"]
            url = form.cleaned_data["url"]

            # get result from model
            if(prediction(title, url) == 1):
                result = "This is not fake news !"
            else:
                result = "It's a Fake News !!!"

            # reset form
            form = TextForm()

            return render(request, 'home.html', {'form':form, 'result':result})
    else:
        form = TextForm()
    return render(request, 'home.html', {'form': form})
