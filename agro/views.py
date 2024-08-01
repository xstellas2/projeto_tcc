from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def base(request):
    return render(request, 'base.html')

def agrotoxico(request):
    return render(request, 'agrotoxico.html')

def deletar_sugestao(request):
    return render(request, 'deletar_sugestao.html')

def editar_sugestoes(request):
    return render(request, 'editar_sugestoes.html')

def formulario(request):
    return render(request, 'formulario.html')

def gafanhotos(request):
    return render(request, 'gafanhotos.html')

def lagartas(request):
    return render(request, 'lagartas.html')

def listagem_sugestoes(request):
    return render(request, 'listagem_sugestoes.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')