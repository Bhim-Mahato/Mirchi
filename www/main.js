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

        // play assistant sound (Python)
        eel.playAssistantSound();

        // UI animation
        $("#oval").hide();
        $("#SiriWave").show();

        // call Python function using eel
        eel.allCommands();   // ✅ correct
});


//add shortcut ket (hot key)

    function doc_keyup(e) {
    // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

    if (e.key === 'm' ) {          //on click buttton "m"
        eel.playAssistantSound()
        $("#oval").attr("hidden", true);
        $(".siriWave").attr("hidden", false);
        eel.allCommands()
    }
}

document.addEventListener('keyup', doc_keyup, false);

//funtion for send button


function PlayAssistant(message) {
    if (message != "") {
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands(message);
        $("#chatbox").val("");
        $("#MicBtn").attr('hidden', false);
        $("#SendBtn").attr('hidden', true);
    }
}

function ShowHideButton(message) {
    if (message.length == 0) {
        $("#MicBtn").attr('hidden', false);
        $("#SendBtn").attr('hidden', true);
    }
    else {
        $("#MicBtn").attr('hidden', true);
        $("#SendBtn").attr('hidden', false);
    }
}

$("#chatbox").keyup(function () {
    let message = $("#chatbox").val();
    ShowHideButton(message)
});

$("#SendBtn").click(function () {
    let message = $("#chatbox").val()
    PlayAssistant(message)
});

$("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
        let message = $("#chatbox").val()
        PlayAssistant(message)
    }
});

});
