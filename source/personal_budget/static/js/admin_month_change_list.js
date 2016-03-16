(function($) {
  $(document).ready(function() {
    setBalanceColor()
  });

  function setBalanceColor(data){
    var balance = $("#balance").text()

    if (balance < 0) {
      $(".balance-container").addClass("things-are-not-good");
    }
    else {
      $(".balance-container").addClass("i-am-rich");
    }
  }

})(django.jQuery);