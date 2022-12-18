# Generated by Django 4.1.3 on 2022-12-14 05:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_footerinformation_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerinformation',
            name='icon',
            field=models.ImageField(null=True, upload_to='svg/', validators=[django.core.validators.FileExtensionValidator(['svg', 'pdf', 'doc'])]),
        ),
    ]