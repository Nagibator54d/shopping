from django.db import models
from django.urls import reverse

class Category(models.Model):
    
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category',args=[self.id])
    class Meta:
        ordering=('name',)
        verbose_name='Категория'
        verbose_name_plural='Категория'


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)


class Product(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB','Published'

    title = models.CharField(max_length=100)
    slug=models.SlugField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(max_length=100)
    available=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    
    object = models.Manager()

    published = PublishedManager()
   
    class Meta:
        verbose_name ='Товары'
        verbose_name_plural ='Товары'

    def __str__(self):
        return self.title


