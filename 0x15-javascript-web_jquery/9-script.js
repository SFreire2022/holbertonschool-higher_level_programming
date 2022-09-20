$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
    if (textStatus === 'success') {
      $('#hello').text(data.hello);
     }
  });
});
