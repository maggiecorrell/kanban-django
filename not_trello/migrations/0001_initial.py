# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=500)),
<<<<<<< HEAD
                ('description', models.TextField()),
                ('status', models.CharField(max_length=200)),
=======
>>>>>>> 93abfe67b413bec508aaa570636cbf2b0cac55c9
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='not_trello.Card')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='not_trello.Category'),
        ),
    ]
