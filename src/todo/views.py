from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Todo


def index(request):
    template = loader.get_template('todo/index.html')
    return HttpResponse(template.render({
        'todo_list': Todo.objects.all(),
    }, request))


def detail(request, todo_id):
    template = loader.get_template('todo/detail.html')
    return HttpResponse(template.render({
        'todo': get_object_or_404(Todo, pk=todo_id),
    }, request))
