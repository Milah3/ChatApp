$(document).ready(function() {
    $('#send_btn').bind('click', function() {
        const message = document.getElementById('msg');
        $(document).load('/run', {'msg': message.value}, function(){ message.value = ''; return 'run complete'});
     });
});


function validate(name) {
    if (name.length >= 2) {
        return true
    }
    return false
}










    // Other way of pass msg to server
//$(document).ready(function() {
//    $('#send_btn').bind('click', function() {
//        const message = document.getElementById('msg');
//        console.log(msg.value)
//        $.getJSON('/run', function(data) {
//            // do something
//            console.log('Oh my tuuubbbbbe');
//        });
//        return console.log('working...');
//        });
//});