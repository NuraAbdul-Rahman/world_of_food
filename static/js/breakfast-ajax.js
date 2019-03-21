// $('#likes').click(function(){
//     var rid;
//     rid = $(this).attr("data-rid");
//     $.get('/breakfast/like/', {recipe_id: rid}, function(data){
//     $('#like_count').html(data);
//     $('#likes').hide();
//     });
//     });

function saveLikes() {
    // JQuery code to be added in here.
    //$('#likes').click(function(){
    // print("hey");
    var rid;
    rid = $(this).attr("data-recipeid");
    $.get('/breakfast/like/', {recipe_id: rid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
// });
}
