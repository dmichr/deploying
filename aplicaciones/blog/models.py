from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class   Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField('Nombre',max_length=200, blank=False, null=False)
    estado= models.BooleanField('Categoría Activada/Categoría no  Activada',default=True)
    fecha_creacion = models.DateField('Fecha de cracion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name= 'Categoría'
        verbose_name_plural= 'Categorías'
        
        
    def __str__(self) -> str:
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres= models.CharField('Nombres de Autor',max_length=200, blank=False, null=False)
    apellidos= models.CharField('Apellidos de Autor',max_length=200, blank=False, null=False)
    facebook= models.URLField('Facebook', blank=True, null=True)
    twitter= models.URLField('Twitter', blank=True, null=True)
    instagram= models.URLField('Instagram', blank=True, null=True)
    web= models.URLField('Web', blank=True, null=True)
    correo= models.EmailField('E-mail', blank=False, null=False)
    estado= models.BooleanField('Autor Activo/Autor no Activo',default=True)
    fecha_creacion = models.DateField('Fecha de cracion', auto_now=False, auto_now_add=True)
    
    
    
    class Meta:
        verbose_name= 'Autor'
        verbose_name_plural= 'Autores'
        
        
    def __str__(self) -> str:
        return '{0}, {1}'.format(self.apellidos, self.nombres) 
    
    
class Post (models.Model):
    id = models.AutoField(primary_key=True)
    titulo= models.CharField('Titulo',max_length=100, blank=False, null=False)
    slug= models.CharField('Slug',max_length=100, blank=False, null=False)
    descripcion= models.CharField('Descripcion',max_length=100, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=250, blank=False,null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado= models.BooleanField('Publicado/No Publicado',default=True)
    fecha_creacion = models.DateField('Fecha de cracion', auto_now=False, auto_now_add=True)
    
    
    class Meta:
        verbose_name= 'Post'
        verbose_name_plural= 'Posts'
        
    # def get_absolute_url(self):
    #     return reverse ('blog:detalle_post', kwargs={"slug":self.slug}) 
         
    def __str__(self) -> str:
        return    self.titulo 