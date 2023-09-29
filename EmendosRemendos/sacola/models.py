from django.db import models
from django.contrib.auth.models import User
from roupa.models import Roupa

class Sacola(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    status = models.CharField(
        default='afazer',
        max_length=8,
        choices=(
            ('pronto', 'Pronto'),
            ('proent', 'Pronto e Entregue'),
            ('afazer', 'A Fazer'),
        )
    )
    situacao = models.CharField(
        default='naopago',
        max_length=8,
        choices=(
            ('pago', 'Pago'),
            ('naopago', 'Não Pago'),
            ('ptpago', 'Pagou uma parte'),
        )
    )
    observecao_sacola = models.TextField(max_length=255, blank=True, null=True)
    total = models.FloatField()

def __str__(self):
    return f'Sacola N. {self.pk}'



class ProdutoSacola(models.Model):
    sacola = models.ForeignKey(Sacola, on_delete=models.CASCADE)
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    preco = models.FloatField()

    def __str__(self):
        return f'Item da sacola. {self.sacola}'
    
    class Meta: 
        verbose_name = 'Item da sacola'
        verbose_name_plural = 'Itens da sacola'
