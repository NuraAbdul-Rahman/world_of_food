

function saveLikes() {
    var rid;
    rid = $(this).attr("data-recipeid");
    $.get('/breakfast/like/', {id: rid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
}
