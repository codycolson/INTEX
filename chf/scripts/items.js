$(function() {


    $("#searchbox").on('click', function() {

        var id = $("#search").val();
        window.location.href = '/items/' + id;
        return false;
    });//click
});//ready