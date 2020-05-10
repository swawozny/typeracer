$('.cpm').click(function(){
    var score = $(this).attr("score");
        var me = $(this)
        $.get('/end-game', {score: score}, function(data){
                        $('#pages').html(data);
                        me.hide();
                        });
                                });