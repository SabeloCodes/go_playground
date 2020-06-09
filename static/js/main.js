/*========================== INITIALIZE CAROUSEL =================================*/


$(document).ready(function(){
    $('.carousel .carousel-slider .slider').carousel({
        interval: 4000,
    });
});

/*========================== CARD HOVER =================================*/

$('.card').hover(
    function(){
        $(this).find('.bottom').stop().slideDown();
    },
    function(){
        $(this).find('.bottom').slideUp();
    }
);

/*========================== MAP ==================================*/

// Initialize and add the map
function initMap() {
  // The location of the park
  var park = {lat: lat, lng: lng }; 
  // The map, centered at the park
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: {lat: lat, lng: lng }});
  // The marker, positioned at the respective park
  var marker = new google.maps.Marker({position: {lat: lat, lng: lng}, map: map});
  
  // The info window, when marker is clicked
  var contentString = '<div class="info-window">' +
                '<h3>Playground Info Window </h3>' +
                '<div class="info-content">' +
                '<p> Write up some information about the park being reviewed</p>' +
                '</div>' +
                '</div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 400
        });

        marker.addListener('click', function () {
            infowindow.open(map, marker);
        });
  
}


/*========================== FORM ==================================*/

// $('#star_rating') .slider({
// 	formatter: function(value) {
// 		return 'Current value: ' + value;
// 	}
// });


