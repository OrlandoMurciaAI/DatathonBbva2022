const tag = document.createElement('p');
tag.innerHTML = "Buscando.."
tag.classList.add("tag-label")
tag.classList.add("search")
document.body.appendChild(tag)
let base ={
    texto :document.getElementsByTagName('p'),
    main_titles :document.getElementsByTagName('h1'),
    second_titles: document.getElementsByTagName('h2')

}


let data = {
}
let resultado = replaceText(base).then((res)=>{

    response = res['result']

    for (let type in response){
        let counter = 0
        for(let text of response[type]){
            if (text >0 ){
                base[type][counter].style.background = 'rgba(255, 58, 32, 0.4)'
            }
            counter = counter+=1
        }
    } 
    let counter_textos = response["texto"].reduce(add,0)
    let counter_titles=response["main_titles"].reduce(add,0)
    let counter_sec_titles =response["second_titles"].reduce(add,0)


    let final_counter = counter_textos + counter_titles + counter_sec_titles
    console.log(final_counter)
    if(final_counter >0){
        tag.classList.remove("search")
        tag.classList.add("fail") 
        tag.innerHTML = "Probabilidad de Sesgo"
    }else{
        tag.classList.remove("search")
        tag.classList.add("success")
        tag.innerHTML = "Libre de Sesgo"
    }
    
    document.body.appendChild(tag)
});

function add(accumulator, a) {
    return accumulator + a;
  }




async function replaceText(base){

    let textos = [...base["texto"]]
    let main_titles = [...base["main_titles"]]
    let second_titles = [...base["second_titles"]]

    data.texto = textos.map((r)=>r.innerText)
    data.main_titles = main_titles.map((r)=>r.innerText)
    data.second_titles = second_titles.map((r)=>r.innerText)
    console.log(data)

    let resultado = await fetch("http://127.0.0.1:8000/model",{
        method: 'POST',
        headers: {
            'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    
    let fin = await resultado.json()
    return fin
          

    
}




   