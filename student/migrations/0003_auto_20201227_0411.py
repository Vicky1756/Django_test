# Generated by Django 3.1.4 on 2020-12-26 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20201226_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='max_student',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='student.school'),
        ),
    ]