
from django.shortcuts import render, redirect, get_object_or_404
from django_countries import countries
from .models import Bank,Country
from .forms import BankForm

def bank_list(request):
    """ Display the first bank entry by default. """
    banks = list(Bank.objects.all().order_by("id"))
    total_banks = len(banks)
    
    if total_banks == 0:
        return redirect("bank_create")

    index = int(request.GET.get("index", 0))
    index = max(0, min(index, total_banks - 1))

    bank = banks[index]
    form = BankForm(instance=bank)
    return render(request, "bank_form.html", {
        "form": form,
        "banks": banks,
        "index": index,
        "total_banks": total_banks,
        "bank_id": bank.id,
        "is_add_mode": False, 
        
    })



def bank_create(request):
    countries = Country.objects.all()

    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bank_list")
    else:
        form = BankForm()

    return render(request, "bank_form.html", {
        "form": form,
        "countries": countries,
        "is_add_mode": True,
    })


def bank_edit(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    
    if request.method == "POST":
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('bank_list') 
    else:
        form = BankForm(instance=bank)

    return render(request, "bank_form.html", {
        "form": form,
        "is_edit_mode": True, 
        "bank_id": bank.id,
    })



def bank_delete(request, bank_id):
    """ Delete an existing bank entry. """
    bank = get_object_or_404(Bank, id=bank_id)
    bank.delete()
    return redirect("bank_list")

def navigate(request, direction):
    banks = list(Bank.objects.all().order_by("id"))
    total_banks = len(banks)  # Total number of records
    index = int(request.GET.get("index", 0)) if banks else 0  # Get current index

    # Navigation logic
    if direction == "first":
        index = 0
    elif direction == "prev":
        index = max(0, index - 1)
    elif direction == "next":
        index = min(total_banks - 1, index + 1)
    elif direction == "last":
        index = total_banks - 1

    return redirect(f"/?index={index}") 

        