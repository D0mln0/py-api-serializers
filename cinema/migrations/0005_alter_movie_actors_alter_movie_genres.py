# Generated by Django 4.0.4 on 2024-11-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0004_alter_genre_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(related_name="movies", to="cinema.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(related_name="movies", to="cinema.genre"),
        ),
    ]
