from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File


def compress_image(img, file_format='webp', new_width=None, new_height=None):
    image = Image.open(img)
    width, height = image.size
    if new_width and new_height:
        image = image.resize((new_width, new_height))

    elif new_width:
        new_height = int(new_width / width * height)
        image = image.resize((new_width, new_height))

    elif new_height:
        new_width = int(new_height / height * width)
        image = image.resize((new_width, new_height))

    image_io = BytesIO()
    image.save(image_io, format=file_format, optimize=True)
    new_image = File(image_io, name=f"{img.name.split('.')[0]}.{file_format}")
    return new_image


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    main_image = models.ImageField(upload_to='images', verbose_name='Изображение', null=True, blank=True)
    weight = models.FloatField(default=1, verbose_name='Вес')

    def save(self, *args, **kwargs):
        try:
            self.main_image = compress_image(self.main_image, new_width=200)
            super().save(*args, **kwargs)
        except:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
