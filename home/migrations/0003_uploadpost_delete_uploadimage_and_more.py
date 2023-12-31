# Generated by Django 4.0.5 on 2022-06-21 09:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(upload_to='images/')),
                ('title', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
        migrations.AlterField(
            model_name='uploadvideo',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
