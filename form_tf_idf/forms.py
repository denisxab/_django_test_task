from django import forms

from form_tf_idf.models import Document


class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('document',)