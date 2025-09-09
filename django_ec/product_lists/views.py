from django.shortcuts import render

# Create your views here.
def listsfunction(request):
    return render(request, 'lists.html', {})

def detailsfunction(request):
    return render(request, 'product_details/details.html', {})