/*==========================INITIALIZE CAROUSEL =================================*/


$(document).ready(function(){
    $('.carousel .carousel-slider .slider').carousel({
        interval: 4000,
    });
});

/*========================== MAP ==================================*/
// Initialize and add the map
function initMap() {
  // The location of Brockwell Park
  var brockwell = {lat: 51.450476, lng: -0.106252}; 
  // The map, centered at Brockwell Park
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: brockwell});
  // The marker, positioned at Brockwell Park
  var marker = new google.maps.Marker({position: brockwell, map: map});
  
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


