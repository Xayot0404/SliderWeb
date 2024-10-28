from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import SlideForm
from django.http import FileResponse
import os
from django.conf import settings
from django.http import HttpResponse
import subprocess
from .models import Presentation
from django.core.files import File


def Web_DesignView(request):
    web_design = Web_Design.objects.all()
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('WebDesign')  
    else:
        form = SlideForm()
    ctx = {
            'web_design':web_design,
            
    }
    return render(request, 'index.html', ctx)




def all_web_designs(request):
    web_designs = Web_Design.objects.all()
      # Barcha web dizaynlarni olish
    ctx = {
        'web_designs': web_designs,
        
    }
    return render(request, 'all_web_designs.html', ctx)


def open_pptx(request, slide_id):
    web_design = get_object_or_404(Web_Design, id=slide_id)
    response = HttpResponse(web_design, content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(web_design.slide_file.name)
    return response


def design2_list(request):
    design2 = WebDesignModel2.objects.all()
    ctx = {
        'design2': design2  
    }
    return render(request, 'design_detail.html', ctx)


def design3_list(request):
    design3 = WebDesignModel3.objects.all()
    ctx = {
        'design3': design3  
    }
    return render(request, 'Web_Developer.html', ctx)


def design4_list(request):
    design4 = WebDesignModel4.objects.all()
    ctx = {
        'design4': design4  
    }
    return render(request, 'App_developing.html', ctx)


def design5_list(request):
    design5 = WebDesignModel5.objects.all()
    ctx = {
        'design5': design5  
    }
    return render(request, 'brading.html', ctx)

def design6_list(request):
    design6 = WebDesignModel6.objects.all()
    ctx = {
        'design6': design6  
    }
    return render(request, 'product.html', ctx)


def convert_ppt_to_html(ppt_file_path):
    html_output_path = ppt_file_path.replace('.pptx', '.html')  # HTML fayl nomi
    command = ['unoconv', '-f', 'html', ppt_file_path]
    subprocess.run(command)
    return html_output_path



def presentation_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        ppt_file = request.FILES['ppt_file']
        
        # Prezentatsiya yaratish
        presentation = Presentation(title=title, ppt_file=ppt_file)
        presentation.save()

        # PPT faylini HTMLga o'zgartirish
        ppt_file_path = presentation.ppt_file.path
        html_output_path = convert_ppt_to_html(ppt_file_path)

        # HTML faylini saqlash
        with open(html_output_path, 'r') as html_file:
            presentation.html_file.save(f"{presentation.title}.html", File(html_file))

        presentation.save()

        return redirect('presentation_view', presentation_id=presentation.id)  # Yangi sahifaga o'tish

    return render(request, 'presentation_upload.html')
def presentation_view(request, presentation_id):
    presentation = Presentation.objects.get(id=presentation_id)
    return render(request, 'presentation_view.html', {'presentation': presentation})

def presentation_list(request):
    presentations = Presentation.objects.all()
    return render(request, 'presentation_list.html', {'presentations': presentations})