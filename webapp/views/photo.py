from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 6
    ordering = ['-created_at']

class PhotoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_queryset(self):
        queryser = super().get_queryset()
        return queryser.filter(is_private=False) | queryser.filter(author=self.request.user)

    def get_object(self, queryset=None):
        token = self.kwargs.get('token')
        if token:
            return get_object_or_404(Photo, token=token)
        else:
            return super().get_object(queryset)

    def post(self, request, *args, **kwargs):
        photo = self.get_object()
        if not photo.token and photo.author == request.user:
            photo.generate_token()
        return redirect(photo.get_absolute_url())

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('webapp:photo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    model = Photo
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        object = self.get_object()
        return object.author == self.request.user or super().has_permission()



class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:photo_list')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        object = self.get_object()
        return object.author == self.request.user or super().has_permission()

