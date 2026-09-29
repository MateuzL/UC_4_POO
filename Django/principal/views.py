from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return HttpResponse(
        "<h1> Olá, turma! </h1>"
        "<h2> Nosso primeiro projeto com Django </h2>"
        "<p> Python agora está respondendo pelo navegador! </p>"
    )


def sobre(request):
    return HttpResponse(
        "<h1> Sobre o projeto </h1>"
        "<p> Aplicação desenvolvida pelos alunos"
        "do Técnico em Desenvolvimento de Sistemas. </p>"
    )

def cursos(request):
    return HttpResponse(
        "<h1> Cursos disponíveis: </h1>"
        "<p> Engenharia Civil </p>"
        "<p> Medicina </p>"
        "<p> Fisioterapia </p>"
        "<p> Engenharia de Software </p>"
    )

# Create your views here.
