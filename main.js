$(document).ready(function(){
    // alert('funcionommmmmmmm')
    $('ul.lista li a:first').addClass('active');
    $('.contenido-global .contenido').hide();
    $('.contenido-global .contenido:first').show();

    $('ul.lista li a').click(function(){
        $('ul.lista li a').removeClass('active');
        $(this).addClass('active');
        $('.contenido-global .contenido').hide();

        var activetab = $(this).attr('href')
        $(activetab).show();
        return false
    });
});