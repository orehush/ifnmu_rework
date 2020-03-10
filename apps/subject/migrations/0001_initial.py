# Generated by Django 3.0.3 on 2020-03-10 09:54

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('document', models.ImageField(upload_to='%Y/%m')),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Reworked'), (50, 'Expired')], default=10)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('courses', models.ManyToManyField(to='faculty.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Faculty')),
            ],
        ),
    ]
