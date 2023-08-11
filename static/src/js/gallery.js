$(document).ready(function() {
    //make a array with galleries that have class gallery
    let galleries = $('.gallery');
    let placeholder = $('#gallery-placeholder');
    let views = [];
    
    //add galleries to array
    galleries.each(function() {
        views.push($(this));
    });
    
    let selector = $('#selector');
    let selected;
    
    //show gallery based on selected selector
    selector.on('change', function() {
        placeholder.addClass('hidden');

        views.forEach(view => view.addClass('hidden'));

        selected = selector.val();
        
        $('#' + selected).toggleClass('block');
        $('#' + selected).toggleClass('hidden');
        
        console.log("Galeria: ", selected);
    });
});