input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    דימר += -50
    if (דימר < 0) {
        דימר = 0
    }
    
    pins.analogWritePin(AnalogPin.P0, דימר)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (דלוק) {
        דלוק = false
        pins.analogWritePin(AnalogPin.P0, 0)
    } else {
        דלוק = true
        pins.analogWritePin(AnalogPin.P0, 1023)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    דימר += 50
    if (דימר < 1023) {
        דימר = 1023
    }
    
    pins.analogWritePin(AnalogPin.P0, 1023)
})
let דימר = 0
let דלוק = false
pins.analogWritePin(AnalogPin.P0, 0)
דלוק = false
דימר = 0
