from django.shortcuts import render, redirect
# Create your views here.

from .forms import TextForm

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            url = form.cleaned_data["url"]
            return redirect("index")  # Rediriger vers une page d'accueil ou une autre vue
    else:
        form = TextForm()
    return render(request, 'home.html', {'form': form})
