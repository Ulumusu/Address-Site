# Generated by Django 2.0.7 on 2018-07-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_cv_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv_model',
            name='picture',
            field=models.ImageField(default='default.png', null=True, upload_to='chapters/%Y/%m/%D'),
        ),
    ]
