from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    regitime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-regitime']
        verbose_name = 'User'
        verbose_name_plural = 'User'

        