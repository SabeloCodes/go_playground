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
  var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng}, map: map
    });
  
  // The info window, when marker is clicked
  var infoWindowContent = '<div class="info-window">' +
                '<h7>Playground Info Window </h7>' +
                '<div class="info-content">' +
                '<p> Write up some information about the park being reviewed</p>' +
                '</div>' +
                '</div>';

        var infoWindow = new google.maps.InfoWindow({
            content: infoWindowContent,
            maxWidth: 400
        });

        marker.addListener('click', function () {
            infoWindow.open(map, marker);
        });
  
}

/*========================== GEOCODE ==================================*/

// Get location form
    var locationForm = document.getElementById('location-form');

// Listen for submit
    // locationForm.addEventListener('submit', geocode);
    document.getElementById("submit-playground").addEventListener('click', geocode)

// Prevent form from being submitted
// 		document.getElementById("location-form").addEventListener("click", function(event){
//   	event.preventDefault();
// }); 


// Call geocode
function geocode(){

    console.log("testing");

    var location = document.getElementById('location-name').value;
    axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
        params:{
            address: location,
            key: 'AIzaSyAvJ8SKMHEjkJmZW5blhSqzEGllrkIG5cE'
        }
    })


    .then(function(response){
        //Log full response
        console.log(response);

        // Geometry
        var lat = response.data.results[0].geometry.location.lat;
        var lng = response.data.results[0].geometry.location.lng;

        // Geocode values
        document.getElementById('lat').value = lat;
        document.getElementById('lng').value = lng;

        // Submit form
        document.getElementById("location-form").submit()
    })
    .catch(function(error){
        console.log(error);
    });
}






