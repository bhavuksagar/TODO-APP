from django.shortcuts import render,redirect
# Create your views here.
from .models import art
from . forms import TodoForm
from django.views.decorators.http import require_POST

def index(request):
    model= art.objects.order_by('id')
    form = TodoForm()
    context={'model':model, 'form':form}
    return render(request, 'index.html',context)

@require_POST
def newTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        mod= art(task=request.POST['text'])
        mod.save()
    return redirect('index')

def completeTodo(request,todo_id):
    modd=art.objects.get(pk=todo_id)
    modd.complete=True
    modd.save()
    return redirect('index')

def deleteTodo(request):
    art.objects.filter(complete__exact=True).delete()
    return redirect('index')
