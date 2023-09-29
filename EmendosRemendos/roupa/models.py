from django.db import models
from PIL import Image
import os
from django.conf import settings


class Roupa(models.Model):
    categoria = models.CharField(
        default='calca',
        max_length=8,
        choices=(
        ('calca', 'Calça'),
        ('short', 'Short'),
        ('camisa', 'Camisa'),
        ('camiseta', 'Camiseta'),
        ('moletom', 'Moletom'),
        ('saia', 'Saia'),
        ('vestido', 'Vestido'),
        ('blusa', 'Blusa'),
        ('bermuda', 'Bermuda'),
        )
    )
    cor = models.CharField(
        default='branco',
        max_length=8,
        choices=(
        ('branco', 'Branco'),
        ('preto', 'Preto'),
        ('cinza', 'Cinza'),
        ('verde', 'Verde'),
        ('azul', 'Azul'),
        ('marrom', 'Marrom'),
        ('amarelo', 'Amarelo'),
        ('rosa', 'Rosa'),
        ('roxo', 'Roxo'),
        ('laranja', 'Laranja'),
        ('bege', 'Bege'),
        ('lilas', 'Lilás'),
        ('verazu', 'Verde-Azulado'),
        )
    )
    reparo = models.CharField(
        default='barra',
        max_length=8,
        choices=(
        ('ajuste', 'Ajuste'),
        ('barra', 'Barra'),
        ('reforma', 'Reforma'),
        ('folgar', 'Folgar'),
        ('trocar', 'Trocar'),
        )
    )
    lugar = models.CharField(
        default='cos',
        max_length=8,
        choices=(
        ('cos', 'Cós'),
        ('barra', 'Barra'),
        ('manga', 'Manga'),
        ('lados', 'Lados'),
        ('gola', 'Gola'),
        ('bolso', 'Bolso'),
        ('ziperc', 'Zíper Comum'),
        ('ziperi', 'Zíper Invisível'),
        ('ziperr', 'Zíper Reforçado'),
        )
    )
    observacao = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.categoria
    

