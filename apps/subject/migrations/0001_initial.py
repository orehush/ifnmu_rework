# Generated by Django 3.0.3 on 2020-02-18 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.Faculty')),
            ],
        ),
    ]