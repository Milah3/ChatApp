$(document).ready(function() {
    $('#send_btn').bind('click', function() {

        const message = document.getElementById('msg');
//        console.log(msg.value)
        $(document).load('/run', {'msg': message.value}, function(){ message.value = ''; return 'run complete'});
//        $.getJSON('/run', function(data) {
//            // do something
//            console.log('Oh my tuuubbbbbe');
//        });
//        return console.log('working...');
        });
});





function validate(name) {
    if (name.length >= 2) {
        return true
    }
    return false
}
