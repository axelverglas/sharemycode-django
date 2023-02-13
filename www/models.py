from django.db import models

# les users sont gérés automatiquement par Django
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Code(models.Model):
    # champs auto - ne pas se soucier de l'id...
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
