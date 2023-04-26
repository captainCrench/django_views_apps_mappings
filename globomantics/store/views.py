from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, PageNotAnInteger

def index(request):
    return HttpResponse("Hello")

def detail(request):
    return HttpResponse("Hello details")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple iPhone")
    if request.method == "GET":
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    elif request.method == "POST":
        return HttpResponseNotFound("Page Not Found")


class ElectronicView(View):
    def get(self, request):
        items = ("Windows PC", "Apple Mac", "Apple iPhone")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        self.process()
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    
    def process(self):
        print("We are processing Electronics")
    

class ElectronicView2(TemplateView):
    template_name = 'store/list.html'
    def get_context_data(self, **kwargs):
        items = ("Windows PC", "Apple Mac", "Apple iPhone")
        context = {'items': items}
        return context

class ElectronicView3(ListView):
    template_name = 'store/list2.html'
    queryset = ("Windows PC", "Apple Mac", "Apple iPhone")
    context_object_name = 'items'
    paginate_by = 2

class ComputersView(ElectronicView):
    def process(self):
        print("We are processing Computers")

class MobileView():
    def process(self):
        print("We are processing Mobile phones")

class EquipmentView(MobileView, ComputersView):
    pass