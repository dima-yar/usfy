from django.shortcuts import render, get_object_or_404
from core.models import Regions, Record

def region(request, pk):
    region = get_object_or_404(Regions, pk=pk)
    regional_records = Record.objects.filter(record_holders_region_id = pk)
    return render(request, 'region.html', {
        'region':region,
        'regrec':regional_records
    });