# Generated by Django 5.0.3 on 2024-05-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_user_unique_google_id_or_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='google_id',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
    ]
