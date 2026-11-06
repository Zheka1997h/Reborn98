from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ProductForm
from django.core.paginator import Paginator


class ProductListView(ListView):
    """Главная страница - список товаров с пагинацией"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6  # по 6 товаров на странице

    def get_queryset(self):
        """Лаконичный запрос по ТЗ"""
        return Product.objects.all()


class ProductDetailView(DetailView):
    """Страница с подробной информацией о товаре"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context


class ProductCreateView(CreateView):
    """Добавление нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')