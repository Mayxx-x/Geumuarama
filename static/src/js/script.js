//set content - pages index
var t_views = [$(".m-escotismo"), $(".m-about"), $(".m-ramos")];
var views = [$(".v-escotismo"), $(".v-about"), $(".v-ramos"), $(".v-fotos"), $(".v-infos"), $(".v-downloads")];

$(".m-escotismo").on("click", function(e) {
    
    views.forEach(view => view.hide());

    $(".v-escotismo").show();
});
$(".m-about").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-about").show();
});
$(".m-ramos").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-ramos").show();
});
$(".m-fotos").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-fotos").show();
});
$(".m-infos").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-infos").show();
});
$(".m-downloads").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-downloads").show();
});