from django.http import HttpResponse

def login(request):

    return HttpResponse("Esto es la parte de inicio donde se deben de logear dependiendo de su cargo")

def administrativa(request):

    return HttpResponse("Sección de gestión")

def almacen(request):

    return HttpResponse("Sección de Almacén")

def compras(request):

    return HttpResponse("Sección de compras")