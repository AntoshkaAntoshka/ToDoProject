from django.db import models

class User(models.Model):
    user_name = models.CharField('Username', max_length=64)
    first_name = models.CharField('Firstname', max_length=64)
    last_name = models.CharField('Lastname', max_length=64)
    email = models.EmailField('E-mail', max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.last_name
