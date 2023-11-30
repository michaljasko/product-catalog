from django.db import models


class AttributeName(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class Attribute(models.Model):
    attribute_name = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.attribute_name} - {self.attribute_value}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default="CZK")
    published_on = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.attribute}'

    class Meta:
        verbose_name_plural = "Product attributes"


class Image(models.Model):
    name = models.CharField(max_length=100, null=True)
    image_url = models.URLField(max_length=255)

    def __str__(self):
        if self.name:
            return f'{self.image_url} ({self.name})'
        return self.image_url


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.name}'


class Catalog(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product, blank=True)
    attributes = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.name
