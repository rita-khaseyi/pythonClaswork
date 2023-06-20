# Generated by Django 4.2.1 on 2023-06-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=32)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
