from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, Skill, Education, Experience, Certification, Achievement, Project
import os


def get_profile():
    return Profile.objects.first()


def home(request):
    context = {
        'profile': get_profile(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'achievements': Achievement.objects.all(),
        'projects': Project.objects.all()[:6],
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'profile': get_profile(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'achievements': Achievement.objects.all(),
    }
    return render(request, 'about.html', context)


def projects(request):
    context = {
        'profile': get_profile(),
        'projects': Project.objects.all(),
    }
    return render(request, 'projects.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'profile': get_profile(),
        'project': project,
    }
    return render(request, 'project_detail.html', context)


def contact(request):
    context = {
        'profile': get_profile(),
    }
    return render(request, 'contact.html', context)


@require_POST
def send_contact_email(request):
    """Handle contact form submission via SMTP."""
    name    = request.POST.get('name', '').strip()
    email   = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    # Basic validation
    if not all([name, email, subject, message]):
        return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

    receiver = getattr(settings, 'CONTACT_RECEIVER_EMAIL', None) or settings.EMAIL_HOST_USER
    if not receiver:
        return JsonResponse({'success': False, 'error': 'Email not configured on server.'}, status=500)

    full_message = (
        f"New contact message from your portfolio\n"
        f"{'─' * 40}\n"
        f"Name    : {name}\n"
        f"Email   : {email}\n"
        f"Subject : {subject}\n"
        f"{'─' * 40}\n\n"
        f"{message}\n"
    )

    try:
        send_mail(
            subject=f"[Portfolio] {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[receiver],
            reply_to=[email],
            fail_silently=False,
        )
        return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def download_resume(request):
    profile = get_profile()
    if profile and profile.resume_file:
        try:
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect(profile.resume_file.url)
        except Exception:
            raise Http404("Resume not found")
    raise Http404("Resume not found")
