# Generated by Django 4.2.11 on 2024-04-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_recommendation_holiday_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='over_view',
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='sites',
            field=models.TextField(),
        ),
    ]
