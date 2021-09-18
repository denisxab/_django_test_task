from django.shortcuts import render

# Create your views here.
from form_tf_idf.forms import DocumentForm
from form_tf_idf.logic import tf_idf


def form_tf_ide(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			# Сохранить в файл
			form.save()

			# Вычислить данные которые пришли из request формы
			request.FILES['document'].seek(0)
			my_uploaded_file: bytes = request.FILES['document'].read()
			my_uploaded_file: str = my_uploaded_file.decode("utf-8")
			my_uploaded_file: list[str] = my_uploaded_file.split()
			words = tf_idf(my_uploaded_file)
			return render(request,
			              template_name="home.html",
			              context={
				              "file_name": form.files['document'],
				              "title": "Данные приняты",
				              "words": words,
			              }, )
	else:
		form = DocumentForm()

	context = {
		"title": "Загрузите файла в формате .txt",
		"form": form,
	}
	return render(request,
	              template_name="form_tf_idf/form_tf_ide.html",
	              context=context, )
