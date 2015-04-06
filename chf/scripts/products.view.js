// wait for the DOM to be loaded
$(function() {


    $("#add_to_cart").on('click', function() {
        var id = $(this).attr('rel');
        var days = $("#select").val();
        console.log(days)
        $.loadmodal({
        url: '/account.rentalcart/' + id + '/' + days,
        title: 'Rental Cart',
        width: '700px',
        });


    });//click
});//ready

$(function() {


    $("#select").on('change', function() {
        if ($(this).val() > 0) {
            $("#add_to_cart").removeAttr("disabled");
        }
        else {
            $("#add_to_cart").prop("disabled",true);
        }

        });//click


    });//ready