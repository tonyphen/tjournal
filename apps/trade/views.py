from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from apps.trade import models, forms
from apps.main.utilities import created_updated


def journal_list(request):
    obj = models.Journal.objects.filter(trader=request.user)
    return render(request, 'trade/journal_list.html', {'items': obj})


def journal_create(request):
    form = forms.JournalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.trader = request.user
            form.save()
            # created_updated(models.Journal, request)
            return redirect('journal_list')

    return render(request, 'trade/journal_create.html', {'form': form})


def journal_update(request, id):
    obj = get_object_or_404(models.Journal, id=id)
    form = forms.JournalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('journal_list')
    return render(request, 'trade/journal_update.html', {'form': form})


def journal_delete(request, id):
    obj = get_object_or_404(models.Journal, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('journal_list')
    return render(request, 'trade/journal_delete.html', {'item': obj})