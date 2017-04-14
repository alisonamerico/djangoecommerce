# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.contrib import messages

from catalog.models import Product

from .models import CartItem


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug = self.kwargs['slug'])
        cart_item = CartItem.objects.add_item(
        self.request.session.session_key, product
        )
        messages.success(self.request, 'Produto adicionado com sucesso')
        return product.get_absolute_url()


create_cartitem = CreateCartItemView.as_view()
