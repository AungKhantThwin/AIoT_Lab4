import hal.hal_input_switch as SWITCH
import hal.hal_led as LED
import time


def blink_LED():
    
    blink_duration = 5  
    blink_interval = 0.1  
    end_time = time.time() + blink_duration

    while time.time() < end_time:
        LED.set_output(24, 1)  
        time.sleep(blink_interval)  
        LED.set_output(24, 0)  
        time.sleep(blink_interval)  

def main():
    SWITCH.init()
    LED.init()

    while True:
        switchPosition = SWITCH.read_slide_switch()
        
       
        if switchPosition == 0:
            blink_LED()  
            LED.set_output(24, 0)  
            break
        else:
            time.sleep(0.1) 

if __name__ == "__main__":
    main()