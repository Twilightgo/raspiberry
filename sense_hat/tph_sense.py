from sense_hat import SenseHat
sense=SenseHat()
sense.set_rotation(90)
while True:
    t=sense.get_temperature()
    p=sense.get_pressure()
    h=sense.get_humidity()

    t=round(t,2)
    p=round(p,2)
    h=round(h,2)

    print("Temperature:"+str(t)+"Pressure:"+str(p)+"Humidity"+str(h))
    message="Temperature:"+str(t)+"Pressure:"+str(p)+"Humidity"+str(h)
    sense.show_message(message,scroll_speed=0.05)

