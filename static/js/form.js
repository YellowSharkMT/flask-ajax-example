(function ($, window, document) {
  /* globals window, jQuery, document, console */

  // enable this return statement to disable Ajax submission
  // return;

  $(document).ready(function () {
    var myForm = $('#myForm');


    myForm.on('submit', function (e) {
      e.preventDefault();
      var data = myForm.serialize();

      $.post('/my-ajax-endpoint', data, function (result) {
        if (result.success) {
          alert(result.message);
        } else {
          alert('Error: ' + result.message);
        }
        console.log(result);
      });
    })
  });
}(jQuery, window, document))
