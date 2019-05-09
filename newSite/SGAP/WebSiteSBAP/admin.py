from django.contrib import admin
from SGAP.WebSiteSBAP.models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    model:Funcionario
    list_display = ['fun_nome','fun_sobrenome', 'fun_salario']
    list_filter = ['fun_salario']
    search_fields = ['fun_nome']
    save_on_top = True

admin.site.register(Funcionario,FuncionarioAdmin)
