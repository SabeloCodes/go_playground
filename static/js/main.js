/*==========================INITIALIZE CAROUSEL =================================*/


$(document).ready(function(){
    $('.carousel .carousel-slider .slider').carousel({
        interval: 4000,
    });
})

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
                '<h3>Info Window Content</h3>' +
                '<div class="info-content">' +
                '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>' +
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


/*========================== NAV BAR ==================================*/
