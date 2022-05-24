# Generated by Django 4.0.4 on 2022-05-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plus500', '0005_traffic_trend'),
    ]

    operations = [
        migrations.DeleteModel(
            name='traffic_trend',
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_commodities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_crypto',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_finance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_forex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_leisure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settings_table',
            name='is_news',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='domain_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='domain_rating_priority',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='domain_traffic',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='domain_traffic_priority',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='email_template',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='organic_keywords',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='organic_keywords_priority',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='referringDomains_backlinks_ratio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='settings_table',
            name='referringDomains_backlinks_ratio_priority',
            field=models.IntegerField(null=True),
        ),
    ]