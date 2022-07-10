
//    $(document).on('change', '.div-toggle', function() {
//        var target = $(this).data('target');
//        var show = $(".dpa-link", this).data('show');
//        $(target).children().addClass('hide');
//        $(show).removeClass('hide');
//    });
//    $(document).ready(function(){
//        $('.div-toggle').trigger('change');
//    });

    $('.list-group li a').on('click', function(){
        $('.card-body .hide').addClass('hide');
        $(this).removeClass('hide');
    });

