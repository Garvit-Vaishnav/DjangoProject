from django.shortcuts import render

def create_certificate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        certificate = Certificate.objects.create(title=title, content=content)
        
    else:
        return render(request, 'create_certificate.html')


def verify_certificate(request):
    if request.method == 'POST':
        certificate_code = request.POST.get('certificate_code')
        try:
            certificate = Certificate.objects.get(pk=certificate_code)

            return render(request, 'certificate_verification.html', {'certificate': certificate})
        except Certificate.DoesNotExist:
            return render(request, 'certificate_verification.html', {'error': 'Certificate not found'})
    else:
        return render(request, 'certificate_verification.html')