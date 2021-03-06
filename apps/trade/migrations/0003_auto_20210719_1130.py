# Generated by Django 3.2.5 on 2021-07-19 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0002_journal_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='updater', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journal',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
