from webapp.forms.base_form import BaseForm
from webapp.models import Album


class AlbumForm(BaseForm):

    class Meta:
        model = Album
        fields = ('title', 'description', 'is_private')