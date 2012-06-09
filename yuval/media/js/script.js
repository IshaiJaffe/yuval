function ws_basic(b, a, f) {
    var e = jQuery;
    var d = f.children();
    var c = e('<div style="position:relative;"></div>');
    f.append(c);
    c.append(d);
    f.css({position:"relative", overflow:"hidden"});
    c.css({position:"relative", width:(b.outWidth * a.length) * 1.1 + "px", left:0, top:0});
    a.css({position:"static"});
    this.go = function (g) {
        c.stop(true).animate({left:-e(a.get(g)).position().left}, b.duration, "easeInOutExpo");
        return g
    }
}
;// -----------------------------------------------------------------------------------
jQuery("#slideDiv").wowSlider({effect:"basic", prev:"", next:"", duration:60 * 100, delay:60 * 100, outWidth:896, outHeight:413, width:896, height:413, autoPlay:true, stopOnHover:false, loop:true, bullets:true, caption:false, controls:false});