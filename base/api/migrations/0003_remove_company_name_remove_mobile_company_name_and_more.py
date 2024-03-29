# Generated by Django 4.0.2 on 2022-02-28 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_mobile_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='company_name',
        ),
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='by', to='api.mobile'),
        ),
        migrations.AddField(
            model_name='mobile',
            name='name',
            field=models.CharField(default=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='description',
            field=models.TextField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='mobile_name',
            field=models.CharField(default=True, max_length=120),
        ),
    ]
