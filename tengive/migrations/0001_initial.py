# Generated by Django 4.0.3 on 2022-12-18 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiptype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('why_10', models.TextField(max_length=600)),
                ('more_information', models.TextField(max_length=600)),
                ('tip_date', models.DateField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('tip_giver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tiptype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tengive.tiptype')),
            ],
            options={
                'ordering': ['tip_date'],
            },
        ),
    ]