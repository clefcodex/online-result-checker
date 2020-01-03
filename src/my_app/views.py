from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, ComplainForm
from django.contrib.auth.decorators import login_required



def index(request):
    context = {

    }

    return render(request, 'index.html', context)


@login_required
def result(request):
	if request.method == "POST":
		form = ComplainForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("result")
		else:
			print(form.error_messages)
			form = ComplainForm(request.POST)
	else:
		form = ComplainForm()

	context = {
		'form': form
	}
	return render(request, 'result.html', context)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            matric_number = form.cleaned_data.get('matric_number')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(matric_number=matric_number, password=raw_password)
            login(request, account)

            return redirect("result")
        else:
            print(form.error_messages)
            form = RegistrationForm(request.POST)

    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)


def logout_view(request):
	logout(request)
	return redirect("index")

def login_view(request):

	user = request.user
	if user.is_authenticated:
		return redirect("result")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			matric_number = request.POST['matric_number']
			password = request.POST['password']
			user = authenticate(matric_number=matric_number, password=password)

			if user:
				login(request, user)
				return redirect("result")

	else:
		form = AccountAuthenticationForm()

	context = { 'form': form }

	return render(request, 'login.html', context)
