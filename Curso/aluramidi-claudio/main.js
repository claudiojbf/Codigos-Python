function tocaSom(idElementSound){
   const elemento = document.querySelector(idElementSound).play();
   if(elemento && elemento.localName === 'audio'){
       elemento.play();
   }
   else{
    console.log('Elemento não encontrado');
   }
}


const listaDeTeclas = document.querySelectorAll('.tecla');



for (let contador = 0; contador < listaDeTeclas.length; contador++){
    const tecla = listaDeTeclas[contador];
    const instrumento = tecla.classList[1];
    
    const idAudio  = `#som_${instrumento}`;
    
    tecla.onclick = function (){
        tocaSom(idAudio);
    }

    tecla.onkeydown = function (event){
        if(event.code == 'Enter' || event.code == 'Space'){
            tecla.classList.add('ativa');
        }
    } 

    tecla.onkeyup = function (event){
        tecla.classList.remove('ativa');
    }

}