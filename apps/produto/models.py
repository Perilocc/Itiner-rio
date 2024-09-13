from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

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
    
    lucro = models.DecimalField(
        "Lucro por Produto",
        editable=False,
        max_digits=10, 
        decimal_places=2,
        blank=True
    )
    
    margem_liquida = models.DecimalField(
        "Margem Líquida",
        max_digits=3, 
        decimal_places=0, 
        default=Decimal(0), 
        validators=PERCENTAGE_VALIDATOR,
        editable=False,
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        
        return self.nome and self.descricao
    
    def save(self, *args, **kwargs):
        self.lucro = self.preco_venda - self.custo
        self.margem_liquida = (self.lucro/self.preco_venda) * 100
        super(Produto, self).save(*args, **kwargs)