# Generated by Django 4.1.3 on 2022-12-30 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mosannaf", "0010_remove_printinghouse_branch_delete_printingbranch"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoverArtists",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="الاسم")),
            ],
            options={
                "verbose_name": "فنان غلاف",
                "verbose_name_plural": "فنانين الأغلفة",
            },
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.author",
                verbose_name="المؤلف",
            ),
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="checker",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.checker",
                verbose_name="المحقق",
            ),
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="m_form",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.forms",
                verbose_name="شكل المصنف",
            ),
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="measurement",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.measurement",
                verbose_name="قياس المصنف",
            ),
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="preparation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.preparation",
                verbose_name="إعداد",
            ),
        ),
        migrations.AlterField(
            model_name="mosannaf",
            name="cover_artist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="mosannaf.coverartists",
                verbose_name="فنان الغلاف",
            ),
        ),
    ]
