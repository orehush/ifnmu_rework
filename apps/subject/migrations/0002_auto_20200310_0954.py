# Generated by Django 3.0.3 on 2020-03-10 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rework',
            name='officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_reworks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rework',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_reworks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rework',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Subject'),
        ),
        migrations.AddField(
            model_name='rework',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_reworks', to=settings.AUTH_USER_MODEL),
        ),
    ]