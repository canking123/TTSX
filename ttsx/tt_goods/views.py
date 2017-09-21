from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'search_bar': 1}
    return render(request, 'tt_goods/index.html', context)
