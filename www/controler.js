$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    }
    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {

        $("#SiriWave").hide();
        $("#oval").show();
    }

    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() != "") {
            chatBox.innerHTML += '<div class="row justify-content-end mb-4">' +
                '<div class="width-size">' +
                '<div class="sender_message">' + message + '</div>' +
                '</div>' +
                '</div>';

            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() != "") {
            chatBox.innerHTML += '<div class="row justify-content-start mb-4">' +
                '<div class="width-size">' +
                '<div class="receiver_message">' + message + '</div>' +
                '</div>' +
                '</div>';

            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Hide Loader and display Face Auth animation
    eel.expose(hideLoader);
    function hideLoader() {
        $("#Loader").hide();
        $("#FaceAuth").show();
    }

    // Hide Loader and display Face Auth animation
    eel.expose(hideLoader)
    function hideLoader() {

        $("#Loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);

    }
    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {

        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);

    }
    // Hide success and display 
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {

        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);

    }


    eel.expose(hideStart)
    function hideStart() {

        // Hide Start screen
        $("#Start").attr("hidden", true);

        // First make Oval visible
        $("#Oval").attr("hidden", false);

        // Remove previous animation if exists
        $("#Oval").removeClass("animate__animated animate__zoomIn");

        // Small delay to force reflow (important)
        setTimeout(function () {
            $("#Oval")[0].offsetWidth;  // force reflow
            $("#Oval").addClass("animate__animated animate__zoomIn");
        }, 100);
    }


});