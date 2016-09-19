/**
 * Created by itc_user on 8/27/2016.
 */




$(document).ready(function () {
    // document.getElementById('image_preview').addEventListener('change', handleFileSelect, false);
    document.getElementById("files").onchange = function () {
        var reader = new FileReader();

        reader.onloadend = function (e) {
            // get loaded data and render thumbnail.
            document.getElementById("image_preview").src = e.target.result;
        };

        // read the image file as a data URL.
        reader.readAsDataURL(this.files[0]);

    };

    $("#preview").click(function () {
        $(".display_form").toggle();
    });

    $("#cancel").click(function () {
        $(".display_form input").each(function () {
            $(this).val("");
        });
        $(".display_form").hide();
    });


    // FUNCTION PARTICIPANTS NUMBER


    $('#participants_number').on('change', function () {
        var currentValue = $(this).val();
        var listLength = $('.email_holder').children().length;
        if (currentValue > listLength) {
            var numberOfFieldsToAdd = currentValue - listLength;
            for (var i = 0; i < numberOfFieldsToAdd; i++) {
                var index = listLength + i;
                $('.email_holder').append('<div class="email_holder col-lg-12" style="padding: 0px"><div id="email_participant_input input_location"><input type="text" name="participants_name' + index + '" placeholder="Name" class="input_name col-lg-4"> <input type="text" name="participants_email' + index + '" placeholder="E-mail" class="input_mail col-lg-6"> </div></div>');
            }

        } else {
            var numberOfFieldsToRemove = listLength - currentValue;
            for (var i = 0; i < numberOfFieldsToRemove; i++) {
                $('.email_holder').children().last().remove();
            }
        }


    });

// FUNCTION UPLOAD IMAGE

    // previewFile();  //calls the function named previewFile()

//ocpu.seturl("//public.opencpu.org/ocpu/library/utils/R")

//actual handler
// $("#submitbutton").on("click", function(){
//
//     //arguments
//     var myheader = $("#header").val() == "true";
//     var myfile = $("#csvfile")[0].files[0];
//
//     if(!myfile){
//         alert("No file selected.");
//         return;
//     }
//
//     //disable the button during upload
//     $("#submitbutton").attr("disabled", "disabled");
//
//     //perform the request
//     var req = ocpu.call("read.csv", {
//         "file" : myfile,
//         "header" : myheader
//     }, function(session){
//         session.getConsole(function(outtxt){
//             $("#output").text(outtxt);
//         });
//     });
//
//     //if R returns an error, alert the error message
//     req.fail(function(){
//         alert("Server error: " + req.responseText);
//     });
//
//     //after request complete, re-enable the button
//     req.always(function(){
//         $("#submitbutton").removeAttr("disabled")
//     });
// });

});