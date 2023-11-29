def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session.get("carro", {}).items():
            total = total + (float(value["precio_producto"])*value["cantidad_disponible"])
    
    return {"importe_total_carro":total}