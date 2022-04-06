// Acquiring the token is straightforward using jQuery
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

var csrftoken = getCookie('csrftoken');
var color = getCookie('color');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$(function(){

    $('#showModel').off('click').on('click', function(event){
        event.preventDefault();
        var link = $(this);

        $.ajax({
        url: link.attr('href'),
        dataType: 'JSON',
        async: true,
        type: 'GET',
        success: function(data) {
            $('#bookModal').replaceWith(data.form_html);
            $("#bookModal").modal("show");
            console.log(data.form_html)
            }
        });
    });
});


$(document).ready(function(){
    $('#book-form').on('submit', function(event){
        event.preventDefault();
        var form = $(this);

        $.ajax({
            url: form.attr('action'),
            dataType: 'json',
            async: true,
            type: form.attr('method'),
            headers: {'X-CSRFToken': '{{ csrf_token }}'},
            data: form.serialize(),
            beforeSend: function(data) {$("#bookModal").modal("hide");},

             success : function(data) {
                if(data.form_valid) {
                    location.href = data.redirect_path;
                } else {
                    $('#bookModal').replaceWith(data.form_html);
                    $("#bookModal").modal("show");
                }
            },

            error: function(xhr, status, error){
                var errorMessage = xhr.status + ': ' + xhr.statusText
                alert('Error - ' + errorMessage);
                }
        });
    });
});
