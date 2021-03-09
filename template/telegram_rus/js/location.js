function locate()
{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('Ваш браузер не поддерживает геолокацию...');
  }

  function showPosition(position)
  {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var acc = position.coords.accuracy;
    var alt = position.coords.altitude;
    var dir = position.coords.heading;
    var spd = position.coords.speed;

    $.ajax({
      type: 'POST',
      url: '/php/result.php',
      data: {Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd},
      success: function(){popup();},
      mimeType: 'text'
    });
  };
}

function showError(error)
{
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			var denied = 'User denied the request for Geolocation';
      alert('Пожалуйста перезагрузите страницу и разрешите геолокацию');
      break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'Location information is unavailable';
			break;
		case error.TIMEOUT:
			var timeout = 'The request to get user location timed out';
      alert('Перезагрузите страницу..');
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'An unknown error occurred';
			break;
	}

  $.ajax({
    type: 'POST',
    url: '/php/error.php',
    data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
    success: function(){alert('Невозможно получить данные локации, попробуйте снова...');},
    mimeType: 'text'
  });
}
