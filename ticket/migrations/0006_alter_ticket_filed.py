# Generated by Django 3.2.3 on 2021-05-25 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0005_alter_ticket_filed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='filed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Filed', to=settings.AUTH_USER_MODEL),
        ),
    ]
