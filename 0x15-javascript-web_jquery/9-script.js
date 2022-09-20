$(document).ready(function () {
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
