from django.shortcuts import render, get_object_or_404
from shop.models import Instrument, InstrumentDetail, Category
from management.forms import ReviewForm
from shop.models import Instrument
# Create your views here.
from shop.models import Instrument
import random
from shop.models import Instrument, Order, Review


def index(request):
    instruments = Instrument.objects.all()
    categories = Category.objects.all()
    for i in instruments:
        i.percentage = round(i.price * 100 / i.old_price, 2)
    return render(request, 'shop_templates/index2.html', {
        "instruments": instruments,
        "categories": categories
    })


def product_details(request, product_id):
    instrument = Instrument.objects.get(id=product_id)
    instrument_details = InstrumentDetail.objects.filter(instrument=instrument).first()
    all_instruments = Instrument.objects.all()
    related = []
    for i in range(5):
        num = random.randint(0, len(all_instruments) - 1)
        related.append(all_instruments[num])
    return render(request, 'shop_templates/product-detail-2.html', {
        "instrument": instrument,
        "discount": instrument.price * 100 / instrument.old_price,
        "instrument_details": instrument_details,
        "related": related
    })


def leave_review(request, order_id, instrument_id):
    return render(request, 'shop_templates/leave-review.html')


def confirm_submit(request):
    if request.method == "POST":
        rating = request.POST.get("rating-input", None)
        title = request.POST.get("title", None)
        review_text = request.POST.get("review", None)
        fileupload = request.POST.get("fileupload", None)
        check_selected = request.POST.get("check", None)
        print("rating: ", rating)
        print("title: ", title)
        print("review_text: ", review_text)
        print("fileupload: ", fileupload)
        print("check_selected: ", check_selected)
        # f = ReviewForm(request.POST, request.FILES)
        # if f.is_valid():
        #     f.save()
        # print(f.errors)
        new_review = Review(order_id=1, user_id=1, rating=rating, title=title,
                            review_text=review_text, fileupload=fileupload, check_selected=check_selected)
        new_review.save()
    return render(request, 'shop_templates/leave-review-2.html')


def leave_review2(request):
    print(request)
    return render(request, 'shop_templates/leave-review-2.html')


def model_view(request, product_id):
    instrument = get_object_or_404(Instrument, pk=product_id)
    return render(request, 'shop_templates/3d3.html', {
        "instrument": instrument,
    })


def checkout(request):
    return render(request, 'shop_templates/checkout.html')


def confirm(request):
    a_row = Order(user=request.user, name=request.POST['name'], last_name=request.POST['last_name'],
                  full_address=request.POST['full_address'], city=request.POST['city'],
                  postal_code=request.POST['postal_code'], country=request.POST['country'],
                  telephone=request.POST['telephone'], payment=request.POST['payment'],
                  shipping=request.POST['shipping'])
    a_row.save()
    return render(request, 'shop_templates/confirm.html')


def tes(request):
    return render(request, 'shop_templates/back/MODEL_green background.html')


def cart(request):
    return render(request, 'shop_templates/cart.html')
