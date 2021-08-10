# Generated by Django 3.2.5 on 2021-08-10 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_nickname_list_kakaoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='authentication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('authentication_date', models.DateField(auto_now_add=True)),
                ('authentication_email', models.CharField(max_length=100)),
                ('authentication_id', models.ForeignKey(db_column='authentication_id', on_delete=django.db.models.deletion.CASCADE, related_name='authentication_id', to='accounts.nickname_list')),
            ],
        ),
    ]
