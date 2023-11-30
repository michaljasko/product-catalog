# Generated by Django 4.2.7 on 2023-11-30 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_productattributes_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='nazev_atributu',
            new_name='attribute_name',
        ),
        migrations.RenameField(
            model_name='attribute',
            old_name='hodnota_atributu',
            new_name='attribute_value',
        ),
        migrations.RenameField(
            model_name='attributename',
            old_name='kod',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='attributename',
            old_name='zobrazit',
            new_name='is_visible',
        ),
        migrations.RenameField(
            model_name='attributename',
            old_name='nazev',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='hodnota',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='obrazek',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='nazev',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='obrazek',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='nazev',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='mena',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nazev',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cena',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='obrazek',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='nazev',
            new_name='name',
        ),
    ]