# Generated by Django 5.0.6 on 2024-07-02 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ketquahoctap', '0004_ketquahoctap_diemthilai_ketquahoctap_hesotongket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ketquahoctap',
            name='DiemThiLai1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ketquahoctap',
            name='DiemThiLai2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ketquahoctap',
            name='DiemThiLai3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ketquahoctap',
            name='DiemThiLai4',
            field=models.FloatField(blank=True, null=True),
        ),
    ]