$(document).ready(function () {

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.30,
        autostart: true
    });

    // Text animation (ONLY works if textillate libs are loaded)
    if ($.fn.textillate) {
        $('.siri-message').textillate({
            loop: true,
            sync: true,
            in: {
                effect: 'fadeInUp',
                sync: true
            },
            out: {
                effect: 'fadeOutUp',
                sync: true
            }
        });
    }

    // Mic button click event
    $("#MicBtn").on("click", function () {
        //for sound
        //call function main.js
        eel.playAssistantSound()


        //for click oval->siriwave
        $("#oval").hide();
        $("#SiriWave").show();
    });

});
