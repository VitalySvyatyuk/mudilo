$('input[name="search"]').on('input', function(){
  $.ajax({
    url: 'https://mudilo.me/api/v1/search' + '?search=' + this.value,
    // url: 'http://127.0.0.1:8000/api/v1/search' + '?search=' + this.value,
    type: 'GET',
    dataType: 'json',
    success: function(res) {
      $('#search-results').empty()
      for (plate of res) {
        var img = '<img class="img-country" src="/static/images/' + plate[1] + '-flag-icon-32.png">'
        $('#search-results').append(
          '<span class="search-span mx-3">' + img + plate[0].toUpperCase() + '</span><br>'
        )
      }
    }
  });
});

$(document).on('click', '.search-span', function (e) {
  $('input[name="search"]').val(e.target.textContent)
});

$('input[name="search"]').focusout(function() {
  setTimeout(function () {
    $('#search-results').empty()
  }, 200)

});


