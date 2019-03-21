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
<<<<<<< HEAD
    rid = $(this).attr("data-recipeid");
    $.get('/breakfast/like/', {recipe_id: rid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
=======
    rid = $(this).attr("data-rid");
    $.get('/breakfast/like', {recipe_id: rid}, function(data){
    $('#like_count').html(data);
    $('#likes').hide();
>>>>>>> 3dfa2187a16e1c4078cf76e63f299df980d9ded8
    });
// });
}
