# Generated by Django 4.1.2 on 2022-10-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footballapp", "0002_teammodel_upated_date_alter_teammodel_established"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammodel",
            name="established",
            field=models.DateField(default="1969-7-20"),
        ),
        migrations.AlterField(
            model_name="teammodel",
            name="hometown",
            field=models.CharField(
                choices=[
                    ("Hokkaido", "Hokkaido"),
                    ("Aomori", "Aomori"),
                    ("Iwate", "Iwate"),
                    ("Miyagi", "Miyagi"),
                    ("Akita", "Akita"),
                    ("Yamagata", "Yamagata"),
                    ("Fukushima", "Fukushima"),
                    ("Ibaraki", "Ibaraki"),
                    ("Tochigi", "Tochigi"),
                    ("Gunma", "Gunma"),
                    ("Saitama", "Saitama"),
                    ("Chiba", "Chiba"),
                    ("Tokyo", "Tokyo"),
                    ("Kanagawa", "Kanagawa"),
                    ("Nigata", "Nigata"),
                    ("Toyama", "Toyama"),
                    ("Ishikawa", "Ishikawa"),
                    ("Fukui", "Fukui"),
                    ("Yamanashi", "Yamanashi"),
                    ("Nagano", "Nagano"),
                    ("Gifu", "Gifu"),
                    ("Shizuoka", "Shizuoka"),
                    ("Aichi", "Aichi"),
                    ("Mie", "Mie"),
                    ("Shiga", "Shiga"),
                    ("Kyoto", "Kyoto"),
                    ("Osaka", "Osaka"),
                    ("Hyogo", "Hyogo"),
                    ("Nara", "Nara"),
                    ("Wakayama", "Wakayama"),
                    ("Tottori", "Tottori"),
                    ("Shimane", "Shimane"),
                    ("Okayama", "Okayama"),
                    ("Hiroshima", "Hiroshima"),
                    ("Yamaguchi", "Yamaguchi"),
                    ("Tokushima", "Tokushima"),
                    ("Kagawa", "Kagawa"),
                    ("Ehime", "Ehime"),
                    ("Kochi", "Kochi"),
                    ("Fukuoka", "Fukuoka"),
                    ("Saga", "Shiga"),
                    ("Nagasaki", "Nagasaki"),
                    ("Kumamoto", "Kumamoto"),
                    ("Oita", "Oita"),
                    ("Miyazaki", "Miyazaki"),
                    ("Kagoshima", "Kagoshima"),
                    ("Okinawa", "Okinawa"),
                ],
                max_length=26,
                verbose_name="prefecture",
            ),
        ),
    ]