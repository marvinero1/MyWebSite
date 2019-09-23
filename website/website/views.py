from django.http import HttpResponse

def saludo(request):
    
    return HttpResponse("Hola, mi primera pagina aprendiendo django")

def despedida(request):

    return HttpResponse("ajora me despido en otra pagina")
