# Generated by Django 5.1.6 on 2025-02-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enrollment", "0002_alter_enrollment_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="password",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
