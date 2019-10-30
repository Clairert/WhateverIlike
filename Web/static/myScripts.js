$(function(){ 
    console.log("Hi Everybody!");
    console.log("Hi Dr. Nick!");
});


$.get(ajax_url, function(){
    console.log("We did it");
}).fail(function(){
    console.log("We did it not");
}).always(function(){
    console.log("It doesn't matter if we did it");
});


