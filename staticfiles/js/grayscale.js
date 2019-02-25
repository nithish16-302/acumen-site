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
    if (window.location.search == "?redirect=true"){
        $('#registrations').click();
    }
});

$('.details-input').keydown(function(e){
    if (e.keyCode == 65 && (e.ctrlKey || e.metaKey)) {
        console.log(e)
        e.target.select()
    }
})