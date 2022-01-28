from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome 

    class Meta:
        verbose_name = 'Autor'
