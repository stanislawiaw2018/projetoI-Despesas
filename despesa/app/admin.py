from django.contrib import admin
from .models import *
# Register your models here.


class DespesaAdmin(admin.ModelAdmin):
    list= display = ('Data_criacao','forma_pagamento','descricao',
                     'vencimento', 'quitacao')

admin.site.register(Despesa, DespesaAdmin)


