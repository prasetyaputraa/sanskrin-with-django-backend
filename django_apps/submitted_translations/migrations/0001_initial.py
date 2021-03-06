# Generated by Django 3.1.7 on 2021-04-04 15:29

from django.db import migrations, models
import django_apps.submitted_translations.models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentences', models.TextField()),
                ('maps', djongo.models.fields.ArrayField(model_container=django_apps.submitted_translations.models.TranslationMap)),
            ],
        ),
    ]
