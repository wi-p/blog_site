# Generated by Django 4.0.4 on 2022-11-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(null=True),
        ),
    ]