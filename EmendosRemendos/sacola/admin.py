from django.contrib import admin
from . import models

class ProdutoSacolaInline(admin.TabularInline):
    model = models.ProdutoSacola
    extra = 1

class SacolaAdmin(admin.ModelAdmin):
    inlines = [
        ProdutoSacolaInline
    ]




admin.site.register(models.Sacola, SacolaAdmin)
admin.site.register(models.ProdutoSacola)

