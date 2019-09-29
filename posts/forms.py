from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post


class NewPostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('title', 'image', 'body')
