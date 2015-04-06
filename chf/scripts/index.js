//$(function () {
//
//    $('#username').on('change', function() {
//        var username = $(this).val();
//
//        $.ajax({
//            url: '/index.check_username',
//            data: {
//                username: 'username'
//            },
//            type: "POST",
//            success: function(response) {
//                if (response == '1'){
//                    $('#username_message').text('Yes')
//                }else{
//
//                }//if
//            },//success
//        });//ajax
//
//    });//change
//
//});//ready