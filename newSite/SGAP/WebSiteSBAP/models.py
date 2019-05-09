from django.db import models

# Create your models here.
class Funcionario(models.Model):

    fun_nome = models.CharField(
        max_length = 45,
        null = False,
        blank = False
    )

    fun_sobrenome = models.CharField(
        max_length = 45,
        null = False,
        blank = False
    )

    fun_cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )


    fun_salario = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        null = False,
        blank = False
    )
