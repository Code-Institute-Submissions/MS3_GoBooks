  $(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('.datepicker').datepicker();
    $('select').formSelect();
    $('.modal').modal();
    $('textarea#book_review, textarea#book_description').characterCounter();
  });