from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
from ..pythons_core.decorators import groups_required



def index(req):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
        'current_page': 'home'
    }
    return render(req, 'index.html', context)

#@login_required(login_url='login user')
@groups_required(groups = ['Regular user'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        context = {
            'form': form,
            'current_page': 'create'
        }
        return render(request, 'create.html', context)
    else:

        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
