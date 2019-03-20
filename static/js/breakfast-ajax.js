$('#likes').click(function(){
    var rid;
    rid = $(this).attr("data-rid");
    $.get('/breakfast/like/', {recipe_id: rid}, function(data){
    $('#like_count').html(data);
    $('#likes').hide();
    });
    });