# Generated by Django 3.2.7 on 2021-09-18 10:51

from django.db import migrations, models
import form_tf_idf.models


class Migration(migrations.Migration):

    dependencies = [
        ('form_tf_idf', '0002_auto_20210918_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[form_tf_idf.models.validate_file_extension], verbose_name='Имя файла'),
        ),
    ]
