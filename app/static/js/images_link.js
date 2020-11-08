all_image = document.getElementsByClassName("image")

Array.prototype.forEach.call(all_image, function(image) {
    // Do stuff here
    console.log(image);
});