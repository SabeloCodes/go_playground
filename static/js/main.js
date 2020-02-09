/*==========================INITIALIZE SELECT/CAROUSEL =================================*/


$(document).ready(function(){
    $('.carousel .carousel-slider .slider').carousel({
        fullwidth: true,
        interval: 2000,
        autoplay:true,
        indicators: true,
        showarrows:true
    });
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
    $(".button-collapse").sideNav();
});





