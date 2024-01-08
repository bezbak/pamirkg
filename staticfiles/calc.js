let nigts = document.querySelector('#nigts');
let km = document.querySelector('#km');

function calc(){
    let n = (+nigts.value*15) + (+km.value*0.70)
     if(+nigts.value>3  && +km.value>250 ){
        document.getElementById('resultcalc').innerHTML = `Сумма равна ${n}$ `
     }
    else if(+nigts.value==3 ){
        document.getElementById('resultcalc').innerHTML = `Сумма равна ${n}$ `
     }
    else if(+km.value==250 ){
        document.getElementById('resultcalc').innerHTML = `Сумма равна ${n}$ `
     }
     else if(+nigts.value<3){
        document.getElementById('nigts').value = null
        document.getElementById('nigts').placeholder= `Не меньше 3 ночей`
        document.getElementById('nigts').classList.add('reds')
     }
     else if(+km.value<250){
        document.getElementById('km').value = null
        document.getElementById('km').placeholder= `Не меньше 250км`
        document.getElementById('km').classList.add('reds')
     }
   
     else if(+km.value<250){
        document.getElementById('resultcalc').innerHTML = `не меншьше 250км`
     }
    
     else{
        document.getElementById('resultcalc').innerHTML = 'ERROR' 
   }
}