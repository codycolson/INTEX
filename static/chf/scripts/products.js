$(function() {


    $("#searchbox").on('click', function() {

        var id = $("#search").val();
        window.location.href = '/products/search/' + id;
        return false;
    });//click
});//ready