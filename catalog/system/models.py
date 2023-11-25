from django.db import models


class AttributeName(models.Model):
    nazev = models.CharField(max_length=100)
    kod = models.CharField(max_length=100, null=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=100)

    def __str__(self):
        return self.hodnota


class Attribute(models.Model):
    nazev_atributu = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nazev_atributu} - {self.hodnota_atributu}'


class Product(models.Model):
    nazev = models.CharField(max_length=255)
    description = models.TextField(null=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    mena = models.CharField(max_length=10, default="CZK")
    published_on = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.attribute}'

    class Meta:
        verbose_name_plural = "Product attributes"


class Image(models.Model):
    nazev = models.CharField(max_length=100, null=True)
    obrazek = models.URLField(max_length=255)

    def __str__(self):
        if self.nazev:
            return f'{self.obrazek} ({self.nazev})'
        return self.obrazek


class ProductImage(models.Model):
    nazev = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.nazev}'


class Catalog(models.Model):
    nazev = models.CharField(max_length=100)
    obrazek = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product, blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.nazev
