// wait for the DOM to be loaded
$(function() {


    $("#show_account_edit").on('click', function() {

        $.loadmodal({
        url: '/account.edit',
        title: 'Edit Your Account Info',
        width: '700px',
        });


    });//click
});//ready

$(function() {


    $("#change_password").on('click', function() {

        $.loadmodal({
        url: '/account.changepassword',
        title: 'Change Your Password',
        width: '700px',
        });


    });//click
});//ready

