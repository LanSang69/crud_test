from django.db import models

class User(models.Model):
    registered = models.DateTimeField(auto_now_add=True)
    f_name = models.CharField(max_length=100, null=False)
    s_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    sl_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['registered', 'l_name', 'sl_name', 'f_name', 's_name']

    def __str__(self):
        return self.f_name, self.email, self.password
