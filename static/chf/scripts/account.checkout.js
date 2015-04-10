$(function() {


    $("#checkout").on('click', function() {

        $.loadmodal({
        url: '/account.confirmation',
        title: 'Congrats!',
        height: '780px',
        });

    });//click
});//ready