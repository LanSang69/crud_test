# Generated by Django 5.0.3 on 2024-05-07 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_register_method_user_register_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_method',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.register_method'),
        ),
    ]