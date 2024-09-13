from django.urls import path
from .views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto-list'),
    path('add/', ProdutoCreateView.as_view(), name='produto-add'),
    path('<int:pk>/edit/', ProdutoUpdateView.as_view(), name='produto-edit'),
    path('<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto-delete'),
]
