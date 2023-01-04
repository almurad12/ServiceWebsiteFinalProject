# Generated by Django 4.0.2 on 2023-01-01 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0003_alter_sheba_servicecategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartanother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicetitle', models.CharField(max_length=300)),
                ('serviceprice', models.CharField(max_length=300)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.sheba')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]