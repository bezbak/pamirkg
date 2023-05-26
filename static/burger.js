// let open = document.querySelector('.header__nav');
// let btn = document.querySelector('.burger__btn');
// btn.addEventListener('click', function fnc(){
//     if(open == 1){
//         open.setAttribute('id', 'open');
//     }
//     else{
//         open.removeAttribute('id', 'open');
//     } 
// })
document.addEventListener('DOMContentLoaded', ()=>{
    document.getElementById('burger').addEventListener('click',()=>{
        document.querySelector('.header__nav').classList.toggle('open');
        document.querySelector('.one').classList.toggle('leftone')
        document.querySelector('.three').classList.toggle('rightree')
        document.querySelector('.two').classList.toggle('midtwo')
    });
    let prices = document.getElementById('price');
    prices.addEventListener('click', ()=>{
        document.querySelector('.fixed__menu').classList.toggle('prices')
        document.getElementById('price').classList.toggle('befores')
    })
    
  
    
   
})
document.getElementById('fix').addEventListener('click', ()=>{
    document.querySelector('.fix__menu').classList.toggle('opacyti')
})
document.getElementById('close__fix').addEventListener('click', ()=>{
    document.querySelector('.fix__menu').classList.toggle('opacyti') 
})
document.getElementById('adds').addEventListener('click', ()=>{
    document.querySelector('.nice').classList.add('nice__active')
    let int = setInterval(()=>{
    let i = 0;
    if(i = 5){
        document.querySelector('.nice').classList.remove('nice__active')
        clearInterval(int)
    }
    }, 5000)
})