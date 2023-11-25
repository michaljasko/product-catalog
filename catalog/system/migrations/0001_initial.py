# Generated by Django 4.2.7 on 2023-11-25 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('kod', models.CharField(max_length=100, null=True)),
                ('zobrazit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodnota', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100, null=True)),
                ('obrazek', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('cena', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('mena', models.CharField(default='CZK', max_length=10)),
                ('published_on', models.DateTimeField(null=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('obrazek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.product')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('attributes', models.ManyToManyField(blank=True, to='system.attribute')),
                ('obrazek', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.image')),
                ('products', models.ManyToManyField(blank=True, to='system.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='hodnota_atributu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.attributevalue'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='nazev_atributu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.attributename'),
        ),
    ]
