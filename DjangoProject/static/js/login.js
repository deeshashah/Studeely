$(document).ready(function(){
	var one,two;
  $(document).mousemove(function(e){
  	one = e.offsetX === undefined ? e.originalEvent.layerX : e.offsetX;
	two = e.offsetY === undefined ? e.originalEvent.layerY : e.offsetY;
     TweenLite.to($('body'), 
        .5, 
        { css: 
            {
            	backgroundPosition: ""+ parseInt(one/8) + "px "+parseInt(two/'12')+"px, "+parseInt(one/'15')+"px "+parseInt(two/'15')+"px, "+parseInt(one/'30')+"px "+parseInt(two/'30')+"px"
            }
        });
  });
});