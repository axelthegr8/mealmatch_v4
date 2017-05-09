/*

$(document).ready(function(){
    $("#hide").click(function(){
        $("#feed").hide();
    });
    $(".col-feed").click(function(){
         
        $("#feed").show();
    });
});
*/

$(document).ready(function(){
    console.log($('#searchbar_plus').attr());
    $('#searchbar_plus').attr('disabled',true);
    $('#ingredient-form').keyup(function(){
        console.log(this);
        if($(this).val().length !=0) {
            $('#searchbar_plus').attr('disabled', false);
        }
        else {
            $('#searchbar_plus').attr('disabled', true);
        }
    });




   $('a').click(function(){
       $("#pager_1").hide()
       $("#pager_2").hide()
       $("#pager_3").hide()
       $("#pager_4").hide()
      var id = "#pager_" + $(this).attr('id');
       $(id).show();
           
   });
});




/*<a href="#" id="pager_1" class="pagerlink" >link</a>

$('a.pagerlink').click(function() { 
    
    var id = $(this).attr('id');
    alert(id);
});*/
$(function () {
    $("#clickme").toggle(function () {
        $(this).parent().animate({left:'0px'}, {queue: false, duration: 500});
    }, function () {
        $(this).parent().animate({left:'-280px'}, {queue: false, duration: 500});
    });
});