# Generated by Django 3.0 on 2020-04-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fifth',
            name='File',
            field=models.FileField(default='', upload_to='media/fifth'),
        ),
        migrations.AddField(
            model_name='fifth',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='first',
            name='File',
            field=models.FileField(default='', upload_to='media/first'),
        ),
        migrations.AddField(
            model_name='first',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='fourth',
            name='File',
            field=models.FileField(default='', upload_to='media/fourth'),
        ),
        migrations.AddField(
            model_name='fourth',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='second',
            name='File',
            field=models.FileField(default='', upload_to='media/second'),
        ),
        migrations.AddField(
            model_name='second',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sixth',
            name='File',
            field=models.FileField(default='', upload_to='media/sixth'),
        ),
        migrations.AddField(
            model_name='sixth',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='third',
            name='File',
            field=models.FileField(default='', upload_to='media/third'),
        ),
        migrations.AddField(
            model_name='third',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
