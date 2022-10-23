let data = {} // objeto que va a contener el body del request

//Función destinada a ser ejecutada cada vez que se requiere hacer un análisis 
function load_page(){

    let tag; // Etiqueta que va a contener el resultado del análisis y es de caracter informativo
    if(document.getElementById('tag')){
        tag = document.getElementById('tag')
    }else{
        tag = document.createElement('div');
        tag.setAttribute('id','tag')

    }
    tag.innerHTML = "<div class='container-anim'></div> Analizando... <span class='close small-icon-analizer' id='btn-2'>X</span>"
    tag.classList.add("tag-label")
    tag.classList.add("search")
    document.body.appendChild(tag)
    document.getElementById('btn-2').addEventListener('click', ()=>{
        tag.classList.add('invisible')
    })
    let base ={
        texto :document.getElementsByTagName('p'),
        main_titles :document.getElementsByTagName('h1'),
        second_titles: document.getElementsByTagName('span')

    }

    // Se realiza el request para enviar la información del sitio web al modelo en el backend
    let resultado = replaceText(base).then((res)=>{

        response = res['result'] //resultado del análisis
        let counter_textos = response["texto"].reduce(add,0)
        let counter_titles=response["main_titles"].reduce(add,0)
        let counter_sec_titles =response["second_titles"].reduce(add,0)
        let final_counter = counter_textos + counter_titles + counter_sec_titles

        if(final_counter >0){
            tag.classList.remove("search")
            tag.classList.add("fail") 
            tag.innerHTML = "<span class='reload  small-icon-analizer'  id='btn-1'>⟳</span> Probabilidad de Sesgo <span class='close small-icon-analizer' id='btn-2'>X</span>"
            //Si al probabilidad de que haya sesgo es superior al 20% se aplica un estilo especial a al etiqueta
        // y se le indica al usuario através de una burbuja flotante la probabilidad de haber sesgo.
        for (let type in response){
            let counter = 0
            for(let text of response[type]){
                if (text >0.35 ){
                    flag = document.createElement('div')
                    flag.classList.add('flag-bias')
                    flag.innerText= Math.round(text * 100) +"%"
                    base[type][counter].style.background = 'rgba(255, 58, 32, 0.4)'
                    base[type][counter].style.position = 'relative'
                    base[type][counter].appendChild(flag)
                    counter = counter+=1
                }
                
            }
        } 

        }else{
            tag.classList.remove("search")
            tag.classList.add("success")
            tag.innerHTML = "<span class='reload small-icon-analizer'  id='btn-1'>⟳</span>Libre de Sesgo <span class='close small-icon-analizer'id='btn-2'>X</span>"
        }

        
        // En caso de que ningún texto contenga un aprobabilidad mayor al 20% la etiqueta indicará que el texto está libre se sesgo

        
        document.body.appendChild(tag)
        document.getElementById('btn-1').addEventListener('click', load_page)
        document.getElementById('btn-2').addEventListener('click', ()=>{
            tag.classList.add('invisible')
        })



        




});


}

// función reductora aditiva para arreglos

function add(accumulator, a) {
    if(a>0.35){
        return accumulator + 1;
    }else{
        return accumulator + 0;
    }
    
  }


// Función que realiza la petición al servidor y estructura la respuesta

async function replaceText(base){

    let textos = [...base["texto"]];
    let main_titles = [...base["main_titles"]];
    let second_titles = [...base["second_titles"]];

    data.texto = textos.map((r)=>r.innerText);
    data.main_titles = main_titles.map((r)=>r.innerText);
    data.second_titles = second_titles.map((r)=>r.innerText);
    if((data.texto.length + data.main_titles.length + data.second_titles.length)==0){
        return {"result":{
            "texto":[],
            "main_titles":[],
            "second_titles":[],

        }}
    }
    data.url = window.location.href;
    let resultado = await fetch("https://www.frity.com.co/appac2/api/v1/data/model",{

        method: 'POST',
        headers: {
            'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(data)
    })
    
    let fin = await resultado.json()
    return fin
          

    
}

load_page()
