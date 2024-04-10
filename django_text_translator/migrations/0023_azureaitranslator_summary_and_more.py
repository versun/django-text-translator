# Generated by Django 5.0.3 on 2024-04-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("translator", "0022_alter_geminitranslator_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="azureaitranslator",
            name="summary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="azureaitranslator",
            name="summary_prompt",
            field=models.TextField(
                default="Summarize the following text in {target_language}:\n{text}"
            ),
        ),
        migrations.AddField(
            model_name="claudetranslator",
            name="summary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="claudetranslator",
            name="summary_prompt",
            field=models.TextField(
                default="Summarize the following text in {target_language}:\n{text}"
            ),
        ),
        migrations.AddField(
            model_name="geminitranslator",
            name="summary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="geminitranslator",
            name="summary_prompt",
            field=models.TextField(
                default="Summarize the following text in {target_language}:\n{text}"
            ),
        ),
        migrations.AddField(
            model_name="moonshotaitranslator",
            name="summary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="moonshotaitranslator",
            name="summary_prompt",
            field=models.TextField(
                default="Summarize the following text in {target_language}:\n{text}"
            ),
        ),
        migrations.AddField(
            model_name="openaitranslator",
            name="summary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="openaitranslator",
            name="summary_prompt",
            field=models.TextField(
                default="Summarize the following text in {target_language}:\n{text}"
            ),
        ),
        migrations.AlterField(
            model_name="googletranslatewebtranslator",
            name="base_url",
            field=models.URLField(
                default="https://translate.googleapis.com/translate_a/single",
                verbose_name="URL",
            ),
        ),
    ]
