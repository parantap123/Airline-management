# Generated by Django 2.0.3 on 2018-03-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airhostess',
            name='airport_name',
            field=models.CharField(default='kol', max_length=100),
            preserve_default=False,
        ),
    ]
