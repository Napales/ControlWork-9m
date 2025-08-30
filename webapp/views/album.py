from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumDetailView(LoginRequiredMixin, DetailView):
    template_name = 'album/album_detail.html'
    model = Album
    context_object_name = 'album'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_private=False) | queryset.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        if self.request.user == album.author:
            context['photos'] = album.photos.all().order_by('-created_at')
        else:
            context['photos'] = album.photos.filter(is_private=False).order_by('-created_at')
        return context

class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = 'album/album_create.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'album/album_update.html'
    form_class = AlbumForm
    model = Album
    permision_required = 'webapp.change_album'

    def has_permission(self):
        object = self.get_object()
        return object.author == self.request.user or super().has_permission()

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'album/album_delete.html'
    model = Album
    success_url = reverse_lazy('webapp:photo_list')
    permission_required = 'webapp.delete_album'

    def has_permission(self):
        object = self.get_object()
        return object.author == self.request.user or super().has_permission()