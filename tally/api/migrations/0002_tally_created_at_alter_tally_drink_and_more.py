# Generated by Django 5.0.4 on 2024-04-27 16:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tally",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tally",
            name="drink",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tally",
                to="api.drink",
            ),
        ),
        migrations.AlterField(
            model_name="tally",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tally",
                to="api.person",
            ),
        ),
    ]
