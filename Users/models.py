from django.db import models

class Register_Method(models.Model):
    method = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.method

class User(models.Model):
    registered = models.DateTimeField(auto_now_add=True)
    f_name = models.CharField(max_length=100, null=False)
    s_name = models.CharField(max_length=100, null=True, blank=True)
    l_name = models.CharField(max_length=100, null=True, blank=True)
    sl_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    register_method = models.ForeignKey(Register_Method, on_delete=models.CASCADE, default=None)
    password = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['registered', 'l_name', 'sl_name', 'f_name', 's_name']

    def __str__(self):
        return f"{self.f_name} - {self.email}"  # Changed the return statement to include only f_name and email
