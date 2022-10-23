let data = {
}
document.body.append(document.createElement('script').setAttribute("src","script.js"))


function load_page(){
    let tag;
    if(document.getElementById('tag')){
        tag = document.getElementById('tag')
    }else{
        tag = document.createElement('div');
        tag.setAttribute('id','tag')

    }
    

    tag.innerHTML = "<div class='lds-hourglass'></div> Analizando... <span class='close small-icon-analizer' id='btn-2'>X</span>"
    tag.classList.add("tag-label")
    tag.classList.add("search")
    document.body.appendChild(tag)
    document.getElementById('btn-2').addEventListener('click', ()=>{
        tag.classList.add('invisible')
    })
    let base ={
        texto :document.getElementsByTagName('p'),
        main_titles :document.getElementsByTagName('h1'),
        second_titles: document.getElementsByTagName('h2')

    }



    let resultado = replaceText(base).then((res)=>{

        response = res['result']

        for (let type in response){
            let counter = 0
            for(let text of response[type]){
                if (text >0.5 ){
                    flag = document.createElement('div')
                    flag.classList.add('flag-bias')
                    flag.innerText= text.toFixed(2) * 100 +"%"
                    base[type][counter].style.background = 'rgba(255, 58, 32, 0.4)'
                    base[type][counter].style.position = 'relative'
                    base[type][counter].appendChild(flag)
                    counter = counter+=1
                }
                
            }
        } 
        let counter_textos = response["texto"].reduce(add,0)
        let counter_titles=response["main_titles"].reduce(add,0)
        let counter_sec_titles =response["second_titles"].reduce(add,0)


        let final_counter = counter_textos + counter_titles + counter_sec_titles

        if(final_counter >0){
            tag.classList.remove("search")
            tag.classList.add("fail") 
            tag.innerHTML = "<span class='reload  small-icon-analizer'  id='btn-1'>⟳</span> Probabilidad de Sesgo <span class='close small-icon-analizer' id='btn-2'>X</span>"
        }else{
            tag.classList.remove("search")
            tag.classList.add("success")
            tag.innerHTML = "<span class='reload small-icon-analizer'  id='btn-1'>⟳</span>Libre de Sesgo <span class='close small-icon-analizer'id='btn-2'>X</span>"
        }
        
        document.body.appendChild(tag)
        document.getElementById('btn-1').addEventListener('click', load_page)
        document.getElementById('btn-2').addEventListener('click', ()=>{
            tag.classList.add('invisible')
        })
});


}

function add(accumulator, a) {
    if(a>0.5){
        return accumulator + 1;
    }else{
        return accumulator + 0;
    }
    
  }




async function replaceText(base){

    let textos = [...base["texto"]]
    let main_titles = [...base["main_titles"]]
    let second_titles = [...base["second_titles"]]

    data.texto = textos.map((r)=>r.innerText)
    data.main_titles = main_titles.map((r)=>r.innerText)
    data.second_titles = second_titles.map((r)=>r.innerText)
    let resultado = await fetch("http://127.0.0.1:8000/model",{
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
