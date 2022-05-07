from django.shortcuts import render


def plug_page(request):
    return render(request, 'plug.html', {})