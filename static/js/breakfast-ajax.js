function saveLikes() {
    var rid;
    rid = $(this).attr("data-recipeid");
    $.get('/breakfast/like/', {recipe_id: rid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
}
