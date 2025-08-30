from webapp.forms.base_form import BaseForm
from webapp.models import Photo


class PhotoForm(BaseForm):

    class Meta:
        model = Photo
        fields = ('image', 'description', 'album', 'is_private')
