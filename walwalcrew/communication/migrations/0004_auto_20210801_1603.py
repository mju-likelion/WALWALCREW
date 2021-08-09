# Generated by Django 3.2.5 on 2021-08-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_auto_20210801_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question_list',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question_list',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
