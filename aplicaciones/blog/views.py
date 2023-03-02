from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Categoria, Post
from django.core.paginator import Paginator

def home (request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(estado=True)
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset)   
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page)  
    return render(request,'index.html', {'posts': posts})

def detallePost(request, slug):
    
    post= Post.objects.get(slug= slug)
    post=get_object_or_404(Post, slug=slug)
    return render  (request, 'post.html', {'detalle_post': post})

def grupos (request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(
        estado=True, 
        categoria= Categoria.objects.get(nombre__iexact='Grupos')
    )
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset), 
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact='Grupos'),            
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page) 
    return render(request,'grupos.html',{'posts': posts})


def estadios(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(
        estado=True, 
        categoria= Categoria.objects.get(nombre__iexact='Estadios')
    )
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset), 
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact='Estadios'),            
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page) 
    return render (request, 'estadios.html', {'posts': posts})
    

def calendario(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(
        estado=True, 
        categoria= Categoria.objects.get(nombre__iexact='Calendario')
    )
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset), 
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact='Calendario'),
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page) 
    return render (request, 'calendario.html', {'posts': posts})

def anfitriones(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(
        estado=True, 
        categoria= Categoria.objects.get(nombre__iexact='Anfitriones')
    )
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset), 
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact='Anfitriones'),
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page) 
    return render (request, 'anfitriones.html', {'posts': posts})

def torneos(request):
    queryset= request.GET.get('buscar')
    posts= Post.objects.filter(
        estado=True, 
        categoria= Categoria.objects.get(nombre__iexact='Torneos')
    )
    if queryset:  
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset)|
            Q(descripcion__icontains= queryset), 
            estado= True,
            categoria= Categoria.objects.get(nombre__iexact='Torneos'), 
        ).distinct() 
    paginator= Paginator(posts,2) #para paginar 2 por pagina
    page = request.GET.get('page')
    posts= paginator.get_page(page) 
    return render (request, 'torneos.html', {'posts': posts})