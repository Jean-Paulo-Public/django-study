from django.db import models

class Fotografia(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    text = models.CharField(max_length=300, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.title}]"
