$(function() {

    $('#jquery-loadmodal-js').ajaxForm(function(data) {
    console.log("#jquery-loadmodal-js-body")
        $('#jquery-loadmodal-js-body').html(data);
    });
});//ready

$(function() {


    $(".deleter").on('click', function() {

        var id = $(this).attr("rel");
        $.ajax({
        url: '/account.deletecartitems/' + id
        })
        .done(function(data) {
            $('#jquery-loadmodal-js-body').html(data);
        })
    });//click
});//ready



