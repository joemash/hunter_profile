from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Category, Product


class CategoryDetail(DetailView):
    model = Category


class ProductList(ListView):
    model = Product
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['signages'] = Product.objects.filter(
            category__name='Signage'
        )
        context['vihicles'] = Product.objects.filter(
            category__name='Vihicle Branding'
        )
        return context

class ProductCatalogue(ListView):
    model = Product
    template_name = 'store/catalogue.html'


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        context['main_image'] = self.object.images.first()
        context['specs'] = self.object.specs.all()
        context['related'] = Product.objects.filter(
            category=self.object.category).exclude(
            id__exact=self.object.id)[:3]
        return context
