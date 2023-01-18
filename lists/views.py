from django.shortcuts import render, redirect

from lists.models import TodoItem, List


# Create your views here.
def home_page(request):
    return render(
        request,
        'lists/home_page.html'
    )


def view_list(request):
    return render(
        request,
        'lists/list.html',
        {'todos': TodoItem.objects.all()}
    )


def new_list(request):
    if request.method == 'POST':
        new_item = request.POST.get('new-item', '')
        TodoItem.objects.create(
            text=new_item,
            list=List.objects.create()
        )
    return redirect('/lists/the-only-list-in-the-world/')
