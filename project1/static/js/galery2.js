var images;
var currentImg;

$(function(){
images = $('.photos img').toArray();
});

$('.photos article').click(function ()  {
    console.log ('xyu');
currentImg = $(this).find('img').attr('src');
$('.image img').attr('src', currentImg);
$('.image').css('display', 'flex');
});

$('.image, .image .container').click(function (e) {
if (e.target !== this) {
return;
}

$('.image').css('display', 'none');
});

$('.image button').click(function () {
var id;

for ( var i = 0; i < images.length; i++ ) {
if (images[i].getAttribute('src') == currentImg) {
id = i;
}
}

if ($(this).data("direction") == "left") {
id = id - 1;
}
else {
id = id + 1;
}

if (id < 0) {
id = images.length - 1;
}
else if (id >= images.length) {
id = 0;
}

$('.image img').attr('src', images[id].getAttribute('src'));
currentImg = images[id].getAttribute('src');
});