# Generated by Django 4.2 on 2025-03-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='role',
            field=models.CharField(choices=[('pass', 'Password'), ('imp_info', 'Important information'), ('info', 'Information'), ('other', 'Other')], default='Information', max_length=30),
        ),
    ]
