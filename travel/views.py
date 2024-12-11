from django.shortcuts import render, redirect, get_object_or_404
from .models import Tvl


def home(request):
    return render(request, 'index.html')


def travel_lis(request):
    travel = Tvl.objects.all()
    ctx = {'travel': travel}
    return render(request, 'travel/list.html', ctx)


def travel_create(request):
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        popular_season = request.POST.get('popular_season')
        if destination_name and country and description and popular_season:
            Tvl.objects.create(
                destination_name = destination_name,
                country = country,
                description = description,
                popular_season = popular_season

            )
            return redirect('travel:list')
    return render(request, 'travel/form.html')


def travel_detail(request, travel_id):
    tvl = get_object_or_404(Tvl, pk=travel_id)
    ctx = {'tvl': tvl}
    return render(request, 'travel/detail.html', ctx)


def travel_delete(request, travel_id):
    tvl = get_object_or_404(Tvl, pk=travel_id)
    tvl.delete()
    return redirect('travel:list')


def travel_update(request, travel_id):
    tvl = get_object_or_404(Tvl, pk=travel_id)
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        popular_season = request.POST.get('popular_season')
        if destination_name and country and description and popular_season:
            tvl.destination_name = destination_name
            tvl.country = country
            tvl.description = description
            tvl.popular_season = popular_season
            tvl.save()
            return redirect(tvl.get_detail_url())
    ctx = {'tvl': tvl}
    return render(request, 'travel/form.html', ctx)