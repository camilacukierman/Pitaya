/**
 * Created by itc_user on 8/27/2016.
 */






$(document).ready(function(){
    $("#preview").click(function(){
        $(".display_form").toggle();
    });

    $("#cancel").click(function(){
        $(".display_form input").each(function(){
            $(this).val("");
        });
        $(".display_form").hide();
    })

    $('#participants_number').on ('change',function () {
          $('.email_holder').empty();
         var val = $('#participants_number').val();
            var val = $(this).val();
        for(i=0; i<val; i++) {
        $('.email_holder').append('<div class="email_participant_input>"> <input type="text" name="participant_name" placeholder="Name"> <input type="text" name="participant_email" placeholder="E-mail"> </div>');
    }

    });
});

// FUNCTION UPLOAD IMAGE


   function previewFile(){
       var preview = document.querySelector('img'); //selects the query named img
       var file    = document.querySelector('input[type=file]').files[0]; //sames as here
       var reader  = new FileReader();

       reader.onloadend = function () {
           preview.src = reader.result;
       };

       if (file) {
           reader.readAsDataURL(file); //reads the data as a URL
       } else {
           preview.src = "";
       }
  }

  previewFile();  //calls the function named previewFile()

ocpu.seturl("//public.opencpu.org/ocpu/library/utils/R")

//actual handler
$("#submitbutton").on("click", function(){

    //arguments
    var myheader = $("#header").val() == "true";
    var myfile = $("#csvfile")[0].files[0];

    if(!myfile){
        alert("No file selected.");
        return;
    }

    //disable the button during upload
    $("#submitbutton").attr("disabled", "disabled");

    //perform the request
    var req = ocpu.call("read.csv", {
        "file" : myfile,
        "header" : myheader
    }, function(session){
        session.getConsole(function(outtxt){
            $("#output").text(outtxt);
        });
    });

    //if R returns an error, alert the error message
    req.fail(function(){
        alert("Server error: " + req.responseText);
    });

    //after request complete, re-enable the button
    req.always(function(){
        $("#submitbutton").removeAttr("disabled")
    });
});