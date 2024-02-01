from django.shortcuts import render
from django.core.mail import send_mail
from .models import Price
from .forms import Form_Help

def index(request):
    prices = Price.objects.all()
    if request.method == "POST":
        forma = Form_Help(request.POST)
        if forma.is_valid():
            name = forma.cleaned_data["name"]
            pochta = forma.cleaned_data["pochta"]
            message = forma.cleaned_data["message"]
            send_mail(
                f"",
                f"Сообщение от пользователя - {name}:\n{message}\nПочта отправителя - {pochta} ",
                from_email="267179@bk.ru",
                recipient_list=["267179@bk.ru"],
                fail_silently=False
            )
    else:
        forma = Form_Help()
    data = {
        'prices': prices,
        'forma': forma
    }
    return render(request,'index.html', context=data)