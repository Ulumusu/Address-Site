# Generated by Django 2.0.7 on 2018-07-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_cv_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='links',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]