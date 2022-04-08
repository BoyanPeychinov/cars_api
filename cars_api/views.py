from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def overview_page(request):
    auth_urls = {
        "List": "/auth/",
        "Get-Update-Delete": "/auth/<int:pk>",
        "Login": "/auth/login",
        "Register": "/auth/register",
        "Filter-User-by-Car-Brand": "/auth/?brand={brand}",
        "Filter-User-by-Car-Model": "/auth/?model={model}",
        "Filter-User-by-Age-gt-or-lt": "/auth/?age={age}gt/lt",
        "Filter-User-by-Brand-and-Model": "/auth/?brand={brand}&model={model}",
        "Filter-User-by-Brand-and-Age": "/auth/?brand={brand}&age={age}gt/lt",
        "Filter-User-by-Model-and-Age": "/auth/?model={model}&age={age}gt/lt",
        "Filter-User-by-Brand-and-Model-and-Age": "/auth/?brand={brand}&model={model}&age={age}gt/lt"
    }

    user_car_urls = {
        "List-Create": "/cars/",
        "Get-Update-Delete": "/cars/<int:car_id>",
        "Filter-by-Car-Brand": "/cars/?brand={brand}",
        "Filter-by-Car-Model": "/cars/?model={model}",
        "Filter-by-Mileage-gt-lt-eq": "/cars/?odometer={odometer}gt/lt/eq",
        "Filter-by-FirstReg-gt-lt-eq": "/cars/?year={year}gt/lt/eq",
        "Filter-by-Brand-and-Model": "/cars/?brand={brand}&model={model}",
        "Filter-by-Brand-and-Mileage-gt-lt-eq": "/cars/?brand={brand}&odometer={odometer}gt/lt/eq",
        "Filter-by-Brand-and-FirstReg-gt-lt-eq": "/cars/?brand={brand}&year={year}gt/lt/eq",
        "Filter-by-Model-and-Mileage-gt-lt-eq": "/cars/?model={model}&odometer={odometer}gt/lt/eq",
        "Filter-by-Model-and-FirstReg-gt-lt-eq": "/cars/?model={model}&year={year}gt/lt/eq",
        "Filter-by-Mileage-and-FirstReg-gt-lt-eq": "/cars/?odometer={odometer}gt/lt/eq&year={year}gt/lt/eq",
        "Filter-by-Brand-and-Model-and-Mileage-gt-lt-eq": "/cars/?brand={brand}&model={model}&odometer={odometer}gt/lt/eq",
        "Filter-by-Brand-and-Model-and-FirstReg-gt-lt-eq": "/cars/?brand={brand}&model={model}&year={year}gt/lt/eq",
        "Filter-by-Brand-and-Model-and-Mileage-and-FirstReg-gt-lt-eq":
            "/cars/?brand={brand}&model={model}&odometer={odometer}gt/lt/eq&year={year}gt/lt/eq",
    }

    car_brands_urls = {
        "List-Create": "/brands/",
        "Get-Update-Delete": "/brands/<int:brand_id>"
    }

    car_models_urls = {
        "List-Create": "/models/",
        "Get-Update-Delete": "/models/<int:model_id>"
    }

    api_urls = {
        "Auth_urls": auth_urls,
        "User_Cars_urls": user_car_urls,
        "Car_Brands_urls": car_brands_urls,
        "Car_Models_urls": car_models_urls
    }
    return Response(api_urls)