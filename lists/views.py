from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(
        request,
        'lists/home_page.html',
        {'new_item': request.POST.get('new-item', '')}
    )

