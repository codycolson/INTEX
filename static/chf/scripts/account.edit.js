
$(function() {

    $('#jquery-loadmodal-js').ajaxForm(function(data) {
    console.log("#jquery-loadmodal-js-body")
        $('#jquery-loadmodal-js-body').html(data);
    });
});//ready

