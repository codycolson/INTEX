$(function() {


    $("#searchbox").on('click', function() {

        var id = $("#search").val();
        window.location.href = '/products.returnrental/search/' + id;
        return false;
    });//click
});//ready