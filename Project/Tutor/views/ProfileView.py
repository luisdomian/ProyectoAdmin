from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
from django.contrib import messages

from Tutor.forms import ProfileForm, TutorProfileForm
from UserAuthentication.models import User
from django.shortcuts import render, redirect
from Tutor.models import Tutor
from Session.models import Session
from Modality.models import Modality
from Payment.models import Payment
from Region.models import Regions


def create_context(modality_form):
    context = {
        'modality_form': modality_form
    }
    return context


def edit_sessions(tutor, choices_session):
    tutor.session_type.clear()
    tutor.session_type.add(*choices_session)


def edit_modalities(tutor, choices_modality):
    tutor.modality_type.clear()
    tutor.modality_type.add(*choices_modality)


def edit_payments(tutor, choices_payment):
    tutor.payment_type.clear()
    tutor.payment_type.add(*choices_payment)

class ProfileView(generic.View):
    template_name = 'Tutor/tutorProfile.html'
    form_class: TutorProfileForm = TutorProfileForm

    def __init__(self, *args, **kwargs):
        super(ProfileView, self).__init__(*args, **kwargs)
        self.user = None

    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise Exception("User does not exist")

        profile_form = ProfileForm(request.GET or None, **{'user': user})

        user_to_edit = User.objects.get(id=request.user.id)
        form = self.form_class(instance=user_to_edit)
        selected_user = user_to_edit

        tutor = Tutor.objects.get(user_id=user.id)

        region = Tutor.objects.get(user_id=user.id).region

        tutorship_price = Tutor.objects.get(user_id=user.id).amount_per_person
        increment_half_hour = Tutor.objects.get(user_id=user.id).increment_per_half_hour
        sessions = Tutor.objects.get(user_id=user.id).session_type.all()
        modalities = Tutor.objects.get(user_id=user.id).modality_type.all()
        payments = Tutor.objects.get(user_id=user.id).payment_type.all()

        context = {
            'form': profile_form,
            'tutor_form': form,
            'selected_user': selected_user,
            'region': region,
            'tutorship_price': tutorship_price,
            'increment_half_hour': increment_half_hour,
            'sessions': sessions,
            'modalities': modalities,
            'payments': payments,
            'user': user,
            'title_page': "Perfil",
            'select_navbar_profile': 1
        }

        if user.is_tutor():
            return render(request, self.template_name, context)
        else:
            return redirect('index')

    def post(self, request):
        profile_form = ProfileForm(request.POST or None)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user_to_edit = User.objects.get(id=request.user.id)
            user_to_edit.name = form.cleaned_data['name']
            user_to_edit.lastname = form.cleaned_data['lastname']
            user_to_edit.save()
            messages.add_message(request, messages.SUCCESS, 'Perfil actualizado exitosamente')        
        elif profile_form.is_valid():
            tutor = Tutor.objects.get(user_id=request.user.id)
            tutor.region = Regions.objects.get(
                region_name=profile_form.cleaned_data['choices_region'])
            tutor.amount_per_person = profile_form.cleaned_data['tutorship_price']
            tutor.increment_per_half_hour = profile_form.cleaned_data['increment_half_hour']

            edit_payments(tutor, profile_form.cleaned_data['choices_payment'])
            edit_sessions(tutor, profile_form.cleaned_data['choices_session'])
            edit_modalities(tutor, profile_form.cleaned_data['choices_modality'])
            tutor.save()
            messages.add_message(request, messages.SUCCESS, 'Perfil actualizado exitosamente')
        else:
            messages.add_message(request, messages.ERROR, 'El perfil no ha sido actualizado')

        return redirect('tutor_profile')
