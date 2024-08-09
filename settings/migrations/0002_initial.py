# Generated by Django 5.0.7 on 2024-08-09 05:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        ('system', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', related_query_name='creator_query', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='setting',
            name='dept_belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', related_query_name='dept_belong_query', to='system.deptinfo',
                                    verbose_name='Data ownership department'),
        ),
        migrations.AddField(
            model_name='setting',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+', related_query_name='modifier_query', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Modifier'),
        ),
    ]
