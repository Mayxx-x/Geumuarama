var t_views = [$(".m-escotismo"), $(".m-about")];
var views = [$(".v-escotismo"), $(".v-about")];

$(".m-escotismo").on("click", function(e) {
    
    views.forEach(view => view.hide());

    $(".v-escotismo").show();
});
$(".m-about").on("click", function(e) {
    views.forEach(view => view.hide());

    $(".v-about").show();
});