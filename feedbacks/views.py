from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    form = TourFeedbackform()
    if request.method == 'POST':
        form = TourFeedbackform(request.POST)
        if form.is_valid():
            data = TourFeedback()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.tour_start_date = form.cleaned_data['tour_start_date']
            data.vehicle_condition = form.cleaned_data['vehicle_condition']
            data.driver_support = form.cleaned_data['driver_support']
            data.guide_support = form.cleaned_data['guide_support']
            data.hotels_chosen = form.cleaned_data['hotels_chosen']
            data.ground_support_team = form.cleaned_data['ground_support_team']
            data.destination_rating = form.cleaned_data['destination_rating']
            data.tour_services_rating = form.cleaned_data['tour_services_rating']
            data.improve_services = form.cleaned_data['improve_services']
            data.save()
            print(data)
            # form.save()
            # Handle successful form submission
            return redirect('thankpage')

    contest = {
        'form': form
    }
    return render(request, 'tourfeedback.html', contest)


def thankpage(request):
    return render(request, 'thankpage.html')

# def submit_review(request, product_id):
#     url = request.META.get('HTTP_REFERER')
#     if request.method == 'POST':
#         try:
#             reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
#             form = ReviewRatingForm(request.POST, instance=reviews)
#             form.save()
#             messages.success(request,"Thank you! Your review is updated")
#             return redirect(url)
            
#         except ReviewRating.DoesNotExist:
#             form = ReviewRatingForm(request.POST)
#             if form.is_valid():
#                 data = ReviewRating()
#                 data.subject = form.cleaned_data['subject']
#                 data.rating = form.cleaned_data['rating']
#                 data.review = form.cleaned_data['review']
#                 data.ip = request.META.get('REMOTE_ADDR')
#                 data.product_id = product_id
#                 data.user_id = request.user.id
#                 data.save()
#                 messages.success(request,"Thank you! Your review is submited")
#                 return redirect(url)
            