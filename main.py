def on_button_pressed_a():
    if True:
        devices.tell_camera_to(MesCameraEvent.STOP_VIDEO_MODE)
        images.icon_image(IconNames.SQUARE).show_image(0)
        music.play_melody("C D E F G A B C5 ", 136)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    images.icon_image(IconNames.SMALL_SQUARE).show_image(0)
    devices.tell_camera_to(MesCameraEvent.START_VIDEO_CAPTURE)
    music.set_volume(255)
    music.play_melody("C5 C5 C5 C5 C5 C5 C5 C5 ", 136)
input.on_button_pressed(Button.B, on_button_pressed_b)

devices.tell_camera_to(MesCameraEvent.LAUNCH_VIDEO_MODE)
devices.tell_camera_to(MesCameraEvent.START_VIDEO_CAPTURE)