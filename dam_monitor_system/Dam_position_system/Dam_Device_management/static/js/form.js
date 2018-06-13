$(function () {
    //Date picker
    $('.myDatepicker').datepicker({
      autoclose: true
    });
    getTotalExpense();
  });
  //获取总费用
  function getTotalExpense() {
    $(".partExpense").on("blur", function () {
      var total = 0;
      $(".partExpense").each(function (index, el) {
        total += parseFloat($(el).val() ? $(el).val() : 0);
      });
      $("#totalExpense").val(total);
    });
  }