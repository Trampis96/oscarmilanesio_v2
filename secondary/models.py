from django.db import models

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=100,verbose_name='Título')
    image=models.ImageField(default='null',verbose_name='Miniatura',upload_to='secondary/static/images')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Imagen'
        verbose_name_plural='Imagenes'
        ordering=['-created_at']

    def __str__(self):
        return self.title