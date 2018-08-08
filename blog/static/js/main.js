$(document).ready(function(){

  $('.send-button-1').on('click',() => { $('.list-1').slideToggle("slow");});
  $('.send-button-2').on('click',() => { $('.list-2').slideToggle("slow");});
  $('.send-button-3').on('click',() => { $('.list-3').slideToggle("slow");});
  $('.send-button-4').on('click',() => { $('.list-4').slideToggle("slow");});

  var sidebar = $("#sidebar").offset().top;

  $(window).scroll(function(){

    var scrollPosition = $(window).scrollTop();

    if ($(window).width() >= 1000){
      if(scrollPosition >= sidebar){
        $("#sidebar").stop().animate({
          "marginTop": (scrollPosition-sidebar) + "px"}, "slow" );
      }else{
        $("#sidebar").stop().animate({"marginTop":
        (0) + "px"}, "slow" );
      }
    }

  });




})
