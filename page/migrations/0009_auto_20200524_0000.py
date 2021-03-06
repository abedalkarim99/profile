# Generated by Django 3.0.3 on 2020-05-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_auto_20200520_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='CV',
            field=models.FileField(default='CV_files/default_CV.pdf', upload_to='CV_files'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, choices=[('High School', 'High School'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Doctoral', 'Doctoral')], default='High School', max_length=30, null=True),
        ),
    ]
