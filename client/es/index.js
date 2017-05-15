import axios from 'axios';

(function(){
  axios.get('/api/routes')
      .then(function(response){

        function initMap() {
          let element = document.getElementsByClassName("loader")[0];
          element.parentNode.removeChild(element);

          let map = new google.maps.Map(document.getElementById('map'), {
            center: {
              lat: response.data.routes[0].lat,
              lng: response.data.routes[0].lng
            },
            zoom: 13
          });

          let flightPath = new google.maps.Polyline({
            path: response.data.routes,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
          });

          flightPath.setMap(map);
        }
        google.load("maps", "3", {"other_params": "sensor=false&key=AIzaSyCKcBrI7ULLNL-igiYaeZQ5oCNycm65YHc","callback" : initMap });
    });
})();
