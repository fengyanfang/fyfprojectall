function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
           var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function needCsrfCookie(returnUrl) {
    $( document ).ready(function(){
        if( getCookie('csrftoken') == null ) {
            //window.location.replace('/api/getcsrftoken?returnurl=' + returnUrl);

            var decodeuriStr = "%E4%BA%BF%E6%95%99%E4%BA%BF%E5%AD%A6%E7%89%88%E6%9D%83%E6%89%80%E6%9C%89";
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (xhttp.readyState == 4 && xhttp.status == 200) {
                    console.log("get csrf response")
                }
            };
            xhttp.open("GET", "/api/getcsrftoken", true);
            xhttp.send();
    }})
}


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));

            }
        }
    });

});


//$.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//
//
//         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//             // Only send the token to relative URLs i.e. locally.
//             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         }
//     }
//});