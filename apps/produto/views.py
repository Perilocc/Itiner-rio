from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto

# View para listar todos os produtos
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'  # Nome do template para listar produtos
    context_object_name = 'produtos'

# View para criar um novo produto
class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto_form.html'  # Nome do template para criar um produto
    fields = ['nome', 'descricao', 'custo', 'preco_venda', 'qtd']
    success_url = reverse_lazy('produto-list')

# View para atualizar um produto existente
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'  # Nome do template para editar um produto
    fields = ['nome', 'descricao', 'custo', 'preco_venda', 'qtd']
    success_url = reverse_lazy('produto-list')

# View para excluir um produto
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'  # Nome do template para confirmar exclusão
    success_url = reverse_lazy('produto-list')
