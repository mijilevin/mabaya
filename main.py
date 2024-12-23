def on_button_pressed_a():
    global דימר
    דימר += -50
    if דימר < 0:
        דימר = 0
    pins.analog_write_pin(AnalogPin.P0, דימר)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global דלוק
    if דלוק:
        דלוק = False
        pins.analog_write_pin(AnalogPin.P0, 0)
    else:
        דלוק = True
        pins.analog_write_pin(AnalogPin.P0, 1023)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global דימר
    דימר += 50
    if דימר < 1023:
        דימר = 1023
    pins.analog_write_pin(AnalogPin.P0, 1023)
input.on_button_pressed(Button.B, on_button_pressed_b)

דימר = 0
דלוק = False
pins.analog_write_pin(AnalogPin.P0, 0)
דלוק = False
דימר = 0