// Ederick: This is a seperate JavaScript file for the Privacy Policy Page
//          Used in combination with Jquery for 'click to reveal text' feature
 
$(document).ready(function(){
    $(".icon-bg").click(function () {
        $(".btn").toggleClass("active");
        $(".icon-bg").toggleClass("active");
        $(".container").toggleClass("active");
        $(".box-upload").toggleClass("active");
        $(".box-caption").toggleClass("active");
        $(".box-tags").toggleClass("active");
        $(".private").toggleClass("active");
        $(".set-time-limit").toggleClass("active");
        $(".button").toggleClass("active");
    });

    $(".button").click(function () {
        $(".button-overlay").toggleClass("active");
    });

    $(".iconmelon").click(function () {
        $(".box-upload-ing").toggleClass("active");
        $(".iconmelon-loaded").toggleClass("active");
    });

    $(".private").click(function () {
        $(".private-overlay").addClass("active");
        $(".private-overlay-wave").addClass("active");
    });
});