from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import UserRegistrationForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "website/index.html"

def index(request):
    return render(request, 'website/index.html')

@login_required
def profile(request):
    return render(request, 'website/profile.html')

@login_required
def dashboard(request):
    context = {
        'page_title': _('Dashboard'),
        'user': request.user,
    }
    return render(request, 'website/dashboard.html', context)

def register_workshop(request):
    if request.method == 'POST':
        # Handle form submission
        workshop_name = request.POST.get('workshop_name')
        owner_name = request.POST.get('owner_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        workshop_type = request.POST.get('workshop_type')
        services = request.POST.getlist('services[]')
        
        # Handle file uploads
        business_license = request.FILES.get('business_license')
        workshop_photos = request.FILES.getlist('workshop_photos')
        
        # TODO: Process the workshop registration
        # This is where you would save the data to your database
        # and handle file uploads
        
        messages.success(request, _('Workshop registration submitted successfully!'))
        return redirect('website:index')
        
    return redirect('website:index')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('Registration successful. Please log in.'))
            return redirect('website:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'website/auth/register.html', {'form': form})

def services(request):
    return render(request, 'website/services.html')

def workshops(request):
    return render(request, 'website/workshops.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # TODO: Process the contact form submission
        # This is where you would send emails or save to database
        
        messages.success(request, _('Thank you for your message. We will get back to you soon!'))
        return redirect('website:contact')
        
    return render(request, 'website/contact.html')

@login_required
def dashboard_content(request):
    """Handle loading role-specific dashboard content."""
    role = request.GET.get('role', 'car-owner')
    template = request.GET.get('template', 'car_owner_content.html')
    
    # Validate the template name for security
    allowed_templates = {
        'service_advisor_content.html',
        'team_leader_content.html',
        'technician_content.html',
        'warehouse_content.html',
        'car_owner_content.html',
        'admin_content.html'
    }
    
    if template not in allowed_templates:
        template = 'car_owner_content.html'
    
    template_path = f'website/dashboard/{template}'
    
    # Add any role-specific context data here
    context = {
        'user': request.user,
        'role': role,
    }
    
    return render(request, template_path, context)
