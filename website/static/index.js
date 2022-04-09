$(function() {
    $('#test').bind('click', function() {
        $.getJSON('/run', function(data) {
            // do something
            console.log('Oh my tuuubbbbbe');
        });
        return console.log('working...');
    });
});


function validate(name) {
    if (name.length >= 2) {
        return true
    }
    return false
}
