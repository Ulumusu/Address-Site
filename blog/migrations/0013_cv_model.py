# Generated by Django 2.0.7 on 2018-07-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='cv_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=250)),
                ('born_date', models.CharField(max_length=250)),
                ('adress', models.CharField(max_length=250)),
                ('post_office_code', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('experience', models.TextField()),
                ('education', models.TextField()),
                ('skills', models.TextField()),
                ('interests', models.TextField()),
                ('links', models.TextField()),
            ],
        ),
    ]
