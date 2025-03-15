from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, ResponseForm
from .models import Message

def home(request):
    return render(request, 'resume/home.html')

def skills(request):
    return render(request, 'resume/skills.html')

def projects(request):
    return render(request, 'resume/projects.html')

def about(request):
    return render(request, 'resume/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # ذخیره پیام در پایگاه داده
            message = Message(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            message.save()  # ذخیره پیام در پایگاه داده

            # بعد از ذخیره موفقیت‌آمیز، هدایت به صفحه موفقیت
            return render(request, 'resume/success.html')
    else:
        form = ContactForm()

    return render(request, 'resume/contact.html', {'form': form})


def response_to_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=message)
        if form.is_valid():
            form.save()  # ذخیره پاسخ به پیام
            return redirect('messages')  # بازگشت به صفحه پیام‌ها پس از ذخیره پاسخ
    else:
        form = ResponseForm(instance=message)

    return render(request, 'resume/response_to_message.html', {'form': form, 'message': message})

def messages(request):
    messages = Message.objects.all()
    response_form = ResponseForm()
    return render(request, 'resume/messages.html', {'messages': messages, 'response_form': response_form})
