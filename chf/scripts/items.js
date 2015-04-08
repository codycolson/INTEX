$(function() {


    $("#searchbox").on('click', function() {

        var id = $("#search").val();
        window.location.href = '/items/search/' + id;
        return false;
    });//click
});//ready