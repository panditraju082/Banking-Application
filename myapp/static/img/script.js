<script>
$(document).ready(function() {
  $('#send-upi').click(function() {
    var upi_details = $('#upi-details').val();
    var upi_amount = parseInt($('#upi-amount').val());
    var total_deposit = parseInt($('#total-deposit').text());
    if (upi_amount <= total_deposit) {
      $.ajax({
        url: '/upi/',
        type: 'POST',
        data: {
          'upi_details': upi_details,
          'upi_amount': upi_amount,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
          $('#deposit-amount').text(response.deposit_amount);
          $('#message').text(response.message);
        }
      });
    } else {
      $('#message').text('Insufficient balance');
    }
  })
});
</script>
