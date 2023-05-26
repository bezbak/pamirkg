window.addEventListener('scroll',e =>{
  document.body.style.cssText = `--scrolltop:${this.scrollY}px`
})

window.addEventListener( 'scroll', function() {
    $(window).bind('mousewheel DOMMouseScroll MozMousePixelScroll', function(event) {
      delta = parseInt(event.originalEvent.wheelDelta || -event.originalEvent.detail);
      if (delta >= 0) {
          document.querySelector('.header').classList.add('header__scroll');
        }else if(delta = 0){
          document.querySelector('.header').classList.add('header__scroll');
        }
        else {
           document.querySelector('.header').classList.remove('header__scroll')
      }
    });
  });

