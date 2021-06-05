from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def cadastro(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogc:index')
    context = {'title': 'BloGC | cadastro', 'form': form}
    return render(request, 'registration/cadastro.html', context)
