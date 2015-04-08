// wait for the DOM to be loaded
$(function() {


    $("#show_account_edit").on('click', function() {
        var qty = $("#show_account_edit").val();
        console.log(qty)
        $.loadmodal({
        url: '/users.edit/' + qty,
        title: 'Edit User Info',
        width: '700px',
        });


    });//click
});//ready

$(function() {


    $("#show_account_create").on('click', function() {
        $.loadmodal({
        url: '/users.create/',
        title: 'Create User',
        width: '700px',
        });


    });//click
});//ready

