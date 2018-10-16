from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Pessoal(models.Model):
    sexo_list = (
        ('0', 'Masculino'),
        ('1', 'Feminino'),
        ('2', 'Indefinido'),

    )

    cor_list = (
        ('0', 'Negro'),
        ('1', 'Branco'),
        ('2', 'Amarelo'),
        ('3', 'Pardo'),
    )

    sexo = models.CharField(max_length=1, choices=sexo_list)
    cor = models.CharField(max_length=1, choices=cor_list)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    idade = models.IntegerField()
    datadenacimento = models.DateField()
    endereco = models.CharField(max_length=200)