from django.shortcuts import render



def administrativa(request):

    return render(request, "Gerencia.html")

def almace(request):

    return render(request, "Almace.html")

def compras(request):

    return render(request, "Compras.html")