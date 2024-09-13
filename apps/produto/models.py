from django.db import models

class Produto(models.Model):
    
    nome = models.CharField(
        "Nome do Produto",
        max_length=100,
        blank=False,
    )
    
    descricao = models.TextField(
        "Descrição do Produto",
        blank=True,
    )
    
    custo = models.DecimalField(
        "Custo do Produto",
        max_digits=10,
        decimal_places=2,
        blank=False,
    )
    
    preco_venda = models.DecimalField(
        "Preço do Produto",
        max_digits=10,
        decimal_places=2,
        blank=False,
    )
    
    qtd = models.IntegerField(
        "Quantidade do Produto",
        default=0,
    )
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        
        return self.nome and self.descricao