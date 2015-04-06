// wait for the DOM to be loaded
$(function() {


    $("#show_login_dialog").on('click', function() {

        $.loadmodal({
        url: '/mylogin.loginform',
        title: 'Login'
        });


    });//click
});//ready

