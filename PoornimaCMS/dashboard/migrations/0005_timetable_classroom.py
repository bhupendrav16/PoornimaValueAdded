# Generated by Django 5.0.2 on 2024-03-11 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("classroom", "0002_alter_classroommodel_faculty"),
        ("dashboard", "0004_timetable_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="timetable",
            name="classroom",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="classroom.classroommodel",
            ),
            preserve_default=False,
        ),
    ]