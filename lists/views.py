from django.shortcuts import render, redirect

from lists.models import TodoItem, List


# Create your views here.
def home_page(request):
    return render(
        request,
        'lists/home_page.html'
    )


def view_list(request, list_id):
    todo_list = List.objects.get(id=list_id)
    return render(
        request,
        'lists/list.html',
        {'todos': TodoItem.objects.filter(list=todo_list)}
    )


def new_list(request):
    if request.method == 'POST':
        todo_list = List.objects.create()
        new_item = request.POST.get('new-item', '')
        TodoItem.objects.create(
            text=new_item,
            list=todo_list
        )
    return redirect(f'/lists/{todo_list.id}/')
