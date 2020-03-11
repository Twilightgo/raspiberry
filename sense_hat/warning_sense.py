from sense_hat import SenseHat
sense=SenseHat()
sense.set_rotation(90)
for i in range(0,10):
    t=sense.get_temperature()
    p=sense.get_pressure()
    h=sense.get_humidity()

    t=round(t,2)
    p=round(p,2)
    h=round(h,2)

    print("Temperature:"+str(t)+"Pressure:"+str(p)+"Humidity"+str(h))
    message="T:"+str(t)
    #sense.show_message(message,scroll_speed=0.05)
    red=[255,0,0]
    green=[0,255,0]
    if t>18.3 and t<35.4:
        bg=green
    else:
        bg=red
    sense.show_message(message,back_colour=bg,scroll_speed=0.05)

