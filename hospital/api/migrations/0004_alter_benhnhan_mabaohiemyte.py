# Generated by Django 5.1.2 on 2024-11-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_benhnhan_socccd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benhnhan',
            name='maBaoHiemYTe',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]