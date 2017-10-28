from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from Compressor.compress import CompressTree


# Create your views here.
def index(request):
    # return HttpResponse('Hello, world. You\'re at the polls index.')
    # template = loader.get_template('comp/index.html')
    # templ = loader.get_template('comp/index.html')
    # return HttpResponse(template.render(request))
    return render(request, 'comp/index.html')


def processed(request):

    # Processar texto
    # print(request)
    # return render(request, 'comp/processed.html')
    form = request.POST['text']
    print(form)

    comp_tree = CompressTree(form)
    print(comp_tree.dictionary)

    # return HttpResponseRedirect(reverse('comp:processed', args=(form,)))
    return render(request, 'comp/processed.html', {
            'tree': comp_tree,
        })


def congratz(request):
    return HttpResponse("Tnks 4 use us software.")
