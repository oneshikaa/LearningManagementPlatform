from django.shortcuts import render
from .models import Certificate
from django.shortcuts import render, redirect
from .models import Certificate
from .forms import CertificateForm  

# Create your views here.
def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates/certificate_list.html', {'certificates': certificates})


def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.uploader = request.user  
            certificate.save()
            return redirect('certificates:certificate_list')  
    else:
        form = CertificateForm()

    return render(request, 'certificates/add_certificate.html', {'form': form})

def delete_certificate(request,certificate_id):
    certificate = Certificate.objects.get(pk=certificate_id)
    certificate.delete()
    return redirect('certificates:certificate_list')
