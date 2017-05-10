 function getCookie(name) { //function that returns a cookie
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function makeCookie(){
    document.cookie=[{"ingredients": "m"}]//; expires= Fri, 07 Apr 2017 12:00:00 UTC; path=/"
    var x = document.cookie;
    console.log(x)
}