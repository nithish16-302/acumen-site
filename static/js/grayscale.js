/*!
 * Start Bootstrap - Grayscale Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery to collapse the navbar on scroll
function collapseNavbar() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
}

$(window).scroll(collapseNavbar);
$(document).ready(collapseNavbar);

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $(".navbar-collapse").collapse('hide');
});

function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

function saveParticipantDetails(e){
    e.preventDefault();
    $form = $("#participantDetails");
    formData = getFormData($form)
    $.post(
        $form.attr('action'),
        formData
    )
}

function editOnEnter(e){
    e.srcElement.readOnly = false;
}

function disableOnLeave(e){
    e.srcElement.readOnly = true;
}

function init(){
    form_inputs = $('.details-input');
    for(var i =0; i < form_inputs.length; i++){
        form_inputs[i].readOnly = true;
        form_inputs[i].onmouseenter = editOnEnter;
        form_inputs[i].onmouseleave = disableOnLeave;
    }
}

$('document').ready(function (){
    init();
    searchParams = window.location.search.split('&')
    if (searchParams[0] == "?redirect=true"){
        if(searchParams[1] == "registered=true"){
            $('#message')[0].innerHTML = ('Registration successful');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "login=true"){
            $('#message')[0].innerHTML = ('Login successful');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "loginfailed=true"){
            $('#message')[0].innerHTML = ('Login unsuccessful. Invalid Credentials.');
        }
        else if(searchParams[1] == "teamupdate=true"){
            $('#message')[0].innerHTML = ('Team details have been updated.');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "teamupdate=false"){
            $('#message')[0].innerHTML = ('There was an error updating team details. Please check the email addresses of teammates.');
        }
        else if(searchParams[1] == "teamcreate=true"){
            $('#message')[0].innerHTML = ('New team has been created successfully.');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "teamcreate=false"){
            $('#message')[0].innerHTML = ('Team name is already taken or there is an issue creating new team.');
        }
        else if(searchParams[1] == "join=false"){
            $('#message')[0].innerHTML = ('There was an error joining into the team.');
        }
        else if(searchParams[1] == "join=true"){
            $('#message')[0].innerHTML = ('Joined the team successfully');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "update=true"){
            $('#message')[0].innerHTML = ('Your details have been updated.');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "payment=true"){
            $('#message')[0].innerHTML = ('"Payment is successful! Payment status will be updated soon."');
            $('#message')[0].style.color = "#0088ee";
        }
        else if(searchParams[1] == "payment=false"){
            $('#message')[0].innerHTML = ('Payment unsuccessful! If you have any queries please contact us.');
        }
        else if(searchParams[1] == "leave=false"){
            $('#message')[0].innerHTML = ('Couldn\'t leave team.');
        }
        else if(searchParams[1] == "leave=true"){
            $('#message')[0].innerHTML = ('You left the team successfully.');
            $('#message')[0].style.color = "#0088ee";
        }
        $('#registrations')[0].click();
    }
});

$('.details-input').keydown(function(e){
    if (e.keyCode == 65 && (e.ctrlKey || e.metaKey)) {
        console.log(e)
        e.target.select()
    }
})