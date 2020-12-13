import keyboard

# Key bindings
TAKEOFF_KEY = "enter"
LAND_KEY = "space"
ASCEND_KEY = "w"
DESCEND_KEY = "s"
ROTATE_CW_KEY = "d"
ROTATE_CCW_KEY = "a"
FORWARD_KEY = "up"
BACKWARD_KEY = "down"
LEFT_KEY = "left"
RIGHT_KEY = "right"
FLIP_KEY = "f"

# Sensitivities of different types of commands
HORIZONTAL_TRANSLATION_MAGNITUDE = 80
ROTATION_MAGNITUDE = 40
VERTICAL_TRANSLATION_MAGNITUDE = 100

def check_key_press(takeoff, 
                    land, 
                    ascend,
                    descend,
                    yaw_right,
                    yaw_left,
                    roll_right,
                    roll_left,
                    pitch_forward,
                    pitch_backward,
                    flip):

    # Throttle controls
    if keyboard.is_pressed(TAKEOFF_KEY):
        takeoff()
    if keyboard.is_pressed(LAND_KEY):
        land()
    if keyboard.is_pressed(ASCEND_KEY):
        ascend(VERTICAL_TRANSLATION_MAGNITUDE)
    if keyboard.is_pressed(DESCEND_KEY):
        descend(VERTICAL_TRANSLATION_MAGNITUDE) 

    # Yaw controls
    if keyboard.is_pressed(ROTATE_CW_KEY):
        yaw_right(ROTATION_MAGNITUDE)
    if keyboard.is_pressed(ROTATE_CCW_KEY):
        yaw_left(ROTATION_MAGNITUDE)

    # Roll and pitch controls
    if keyboard.is_pressed(RIGHT_KEY):
        roll_right(HORIZONTAL_TRANSLATION_MAGNITUDE)
    if keyboard.is_pressed(LEFT_KEY):
        roll_left(HORIZONTAL_TRANSLATION_MAGNITUDE)
    if keyboard.is_pressed(FORWARD_KEY):
        pitch_forward(HORIZONTAL_TRANSLATION_MAGNITUDE)
    if keyboard.is_pressed(BACKWARD_KEY):
        pitch_backward(HORIZONTAL_TRANSLATION_MAGNITUDE)

    # Miscellaneous controls
    if keyboard.is_pressed(FLIP_KEY):
        flip()
