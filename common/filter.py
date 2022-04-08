"""
responsible for filtering registered cars with four options and combinations between them
"""

def filter_obj(obj, brand=None, model=None, mileage=None, year=None):
    objs = obj.objects.all()
    options = {
        "brand": brand,
        "model": model,
        "mileage": mileage,
        "year": year
    }

    objs = handle_filtering(objs, options)

    return objs


def handle_filtering(objs, params):
    if params["brand"]:
        brand = params["brand"]
        objs = objs.filter(car_brand__name=brand.lower().capitalize())
    if params["model"]:
        model = params["model"]
        objs = objs.filter(car_model=model.lower().capitalize())
    if params["mileage"]:
        mileage = params["mileage"]
        objs = check_year_or_mileage(objs, "mileage", mileage)
    if params["year"]:
        year = params["year"]
        objs = check_year_or_mileage(objs, "year", year)

    return objs


def check_year_or_mileage(objs, type, parameter):
    value = parameter[:-2]
    suffix = parameter[len(parameter)-2:]

    if suffix == "gt" and type == "year":
        objs = objs.filter(first_reg__year__gte=value)
    elif suffix == "lt" and type == "year":
        objs = objs.filter(first_reg__year__lte=value)
    elif type == "year":
        objs = objs.filter(first_reg__startswith=value)

    if suffix == "gt" and type == "mileage":
        objs = objs.filter(odometer__gte=value)
    elif suffix == "lt" and type == "mileage":
        objs = objs.filter(odometer__lte=value)
    elif type == "mileage":
        objs = objs.filter(odometer=value)

    return objs