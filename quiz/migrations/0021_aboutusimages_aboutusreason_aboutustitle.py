# Generated by Django 4.1.3 on 2022-12-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_privacypolicy_termsofservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_title', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
    ]
