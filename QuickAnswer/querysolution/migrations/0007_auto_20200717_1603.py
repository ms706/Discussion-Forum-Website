# Generated by Django 3.0.7 on 2020-07-17 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('querysolution', '0006_auto_20200713_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solution',
            options={'ordering': ['-created_at']},
        ),
    ]
