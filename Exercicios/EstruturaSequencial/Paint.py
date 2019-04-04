roomSquareMeters = float(input("Square meters of the room to be painted: "))
litersPaint = roomSquareMeters / 3.0
cansPaint = litersPaint / 18
priceCanPaint = cansPaint * 80.0
print("Liters paint: {:.2f}\nCan of paint: {:.2f}\nPrice per can of paint: ${:.2F}".format(litersPaint, cansPaint, priceCanPaint))