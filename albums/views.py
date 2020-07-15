from django.shortcuts import render 
from .models import Album
from django.shortcuts import render, redirect, get_object_or_404
from .forms import album_info_Form

# Create your views here.

def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', context={'albums': albums})

def add_albums(request):
    if request.method == 'GET':
        form = album_info_Form()
    else:
        form = album_info_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_albums.html", {"form": form})

def delete_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_albums.html",
                  {"albums": album})