# Generated by Django 4.1.6 on 2023-02-13 23:41

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to=myapp.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(null=True, upload_to=myapp.models.get_file_path)),
                ('quntitly', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorys')),
            ],
        ),
    ]
