// document.addEventListener('DOMContentLoaded', ()=>{

    window.addEventListener('click',e =>{
        if(e.target.hasAttribute('randoms')){
            document.querySelector('.active__random').classList.remove('active__random');
            e.target.classList.add('active__random')
        }
    })
// })



Fancybox.bind("#gallery a", {
    groupAll : true, // Group all items
    on : {
      ready : (fancybox) => {
        console.log(`fancybox #${fancybox.id} is ready!`);
      }
    }
  });
//   Fancybox.bind("#gallery a", {
//     groupAll : true,
   
//   });



let btn = document.getElementById("video-tagged");

btn.onclick = window.open("./video.html")