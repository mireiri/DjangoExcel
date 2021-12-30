from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import FileUploadForm
from myapp.models import File
from django.http import FileResponse
from myapp.excelpy import excelpy
import os


def index(request):
    all_data = File.objects.all()
    context = {
        'title': 'Excel集計ツール',
        'all_data': all_data,
    }
    return render(request, 'index.html', context)

def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
        
    context = {
        'title': 'アップロード画面',
        'form': form,
    }
        
    return render(request, 'upload.html', context)

def download(request, id):
    download_data = get_object_or_404(File, pk=id)
    file_path = download_data.file.url
    result = excelpy(file_path[1:])
    return FileResponse(open(result, "rb"), as_attachment=True)


def delete(request, id):
    delete_data = get_object_or_404(File, pk=id)
    delete_file =  delete_data.file.url
    #os.remove(delete_file[1:])
    delete_data.delete()
    return redirect('index')

