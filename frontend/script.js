const tag = document.createElement('p');
tag.innerHTML = "Buscando.."
tag.classList.add("tag-label")
tag.classList.add("search")
document.body.appendChild(tag)


let data = {
}
let resultado = replaceText(document.body).then(res=>{
    counts = res['result']
    if(counts>0){
        tag.classList.remove("search")
        tag.classList.add("success")
        tag.innerHTML = "Libre de Sesgo"
    }else{
        tag.classList.remove("search")
        tag.classList.add("fail") 
        tag.innerHTML = "Probabilidad de Sesgo"
    }

    
    document.body.appendChild(tag)
});





async function replaceText(element){

    let texto = element.getElementsByTagName('p')
    let texto2 = element.getElementsByTagName('span')
    let main_title = element.getElementsByTagName('h1')
    let second_title = element.getElementsByTagName('h2')

    let textos = [...texto]
    let textos2 = [...texto2]
    textos = textos.concat(textos2);
    let main_titles = [...main_title]
    let second_titles = [...second_title]

    data.textos = textos.map((r)=>r.innerHTML)
    data.titulos = main_titles.map((r)=>r.innerHTML)
    data.titulos_sec = second_titles.map((r)=>r.innerHTML)

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




   