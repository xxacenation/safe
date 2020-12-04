input.onButtonPressed(Button.A, function () {
    if (true) {
        devices.tellCameraTo(MesCameraEvent.StopVideoMode)
        images.iconImage(IconNames.Square).showImage(0)
        music.playMelody("C D E F G A B C5 ", 136)
        basic.showString("Launch Codes: 175469823")
    }
})
input.onButtonPressed(Button.B, function () {
    images.iconImage(IconNames.SmallSquare).showImage(0)
    devices.tellCameraTo(MesCameraEvent.StartVideoCapture)
    music.setVolume(255)
    music.playMelody("C5 C5 C5 C5 C5 C5 C5 C5 ", 136)
})
devices.tellCameraTo(MesCameraEvent.LaunchVideoMode)
devices.tellCameraTo(MesCameraEvent.StartVideoCapture)
