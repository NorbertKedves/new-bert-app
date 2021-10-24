from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    temp_index = loader.render_to_string('test/test.html')

    rendered = render(
        request,
        'test/test.html',
        {
            'cica': 'kutya'
        }
    )
    return HttpResponse(rendered)
