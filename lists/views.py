from django.shortcuts import render, redirect

from lists.models import TodoItem


# Create your views here.
def home_page(request):
    new_item = ''
    if request.method == 'POST':
        new_item = request.POST.get('new-item', '')
        TodoItem.objects.create(
            text=new_item
        )
        return redirect('/')

    return render(
        request,
        'lists/home_page.html',
        {'todos': TodoItem.objects.all()}
    )
