# Generated by Django 5.0.3 on 2024-05-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_user_google_id'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(condition=models.Q(('google_id__isnull', False)), fields=('google_id',), name='unique_google_id_or_null'),
        ),
    ]