from django.shortcuts import get_object_or_404, render, redirect
from task import models as tmodels
from category import models as cmodels

def Home(request):
    tasks = tmodels.Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def Addtask(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        categories = request.POST.getlist('categories')
        

        task = tmodels.Task.objects.create(
            task_title=task_title,
            task_description=task_description,
        )

        for category in categories:
            cat = cmodels.Category.objects.get(category_name=category)
            cat.tasks.add(task)

        return redirect('home')
    else:
        categories = cmodels.Category.objects.all()
        return render(request, 'addtask.html', {'categories':categories})

def Edittask(request):
    titleid = request.GET.get('id')
    task = get_object_or_404(tmodels.Task, id=titleid)

    if request.method == 'POST':
        task.task_title = request.POST.get('task_title', task.task_title)
        task.task_description = request.POST.get('task_description', task.task_description)
        task.save()
        return redirect('home')
    else:
        return render(request, 'edittask.html', {'task': task})

def Addcategory(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        category = cmodels.Category.objects.create(
            category_name=cname
        )
        return redirect('home')
    else:
        return render(request, 'addcategory.html', {})
    

def Deletetask(request):
    titleid = request.GET.get('id')
    task = get_object_or_404(tmodels.Task, id=titleid)
    task.delete()
    return redirect('home')

def Completetask(request):
    titleid = request.GET.get('id')
    task = get_object_or_404(tmodels.Task, id=titleid)
    task.is_completed = True
    task.save()
    return redirect('home')