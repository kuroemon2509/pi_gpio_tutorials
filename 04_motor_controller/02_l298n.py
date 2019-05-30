import time

import RPi.GPIO as GPIO

import control_utils as cu

if __name__ == "__main__":
    # Components
    # - Raspberry Pi Model B+ (Pi)
    # - L298N Motor Controller (L298N) (not remove 5V regulator jumper)
    # - 2x DC 6V motors
    # - 4x 1.2V AA batteries
    #
    # Wiring
    # - 4.8V+ (Power supply) <-> VCC (L298N)
    # - 4.8V-(Power supply) <-> GRN (L298N) <-> 330 Ohms resistor <-> Ground 39 (Pi)
    # - IN1 (L298N) <-> GPIO (Pi)
    # - IN2 (L298N) <-> GPIO (Pi)
    # - IN3 (L298N) <-> GPIO (Pi)
    # - IN4 (L298N) <-> GPIO (Pi)

    GPIO.setmode(GPIO.BCM)

    IN1 = 5  # 6th PIN from BOTTOM on the LEFT
    IN2 = 6  # 5th PIN from BOTTOM on the LEFT
    IN3 = 13  # 4th PIN from BOTTOM on the LEFT
    IN4 = 26  # 2th PIN from BOTTOM on the LEFT

    controller = cu.L298N(IN1, IN2, IN3, IN4)

    try:
        while True:
            cmd = input('Enter command (up, down, left, right, exit):')

            if cmd == 'up':
                controller.forward()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'down':
                controller.backward()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'left':
                controller.left()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'right':
                controller.right()
                time.sleep(0.5)
                controller.stop()
            elif cmd == 'exit':
                break
    except:
        pass

    controller.stop()
    GPIO.cleanup()