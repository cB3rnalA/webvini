const form = document.getElementById('form')
const search = document.getElementById('search')
const result = document.getElementById('result')


/// api URL ///
const apiURL = 'https://api.lyrics.ovh';


/// adding event listener in form

form.addEventListener('submit', e=> {
    e.preventDefault();
    searchValue = search.value.trim()

    if(!searchValue){
        swal("Ingresa algo en el campo de texto :D")
    }
    else{ 
        searchSong(searchValue)
    }
})


//search song 
async function searchSong(searchValue){
    const searchResult = await fetch(`${apiURL}/suggest/${searchValue}`)
    const data = await searchResult.json();

    // console.log(finaldata)
    showData(data)
}



//display final result in DO
function showData(data){
  
    result.innerHTML = `
    <ul class="song-list">
      ${data.data
        .map(song=> `<li>
                    <div style="font-size: x-large;">
                        <img src="${song.artist.picture}" alt="Artist image">
                        <strong>${song.artist.name}</strong> - ${song.title} 
                    </div>
                    <div class = "purchase-info">
                    <button onclick="alerta()" type = "button" class = "btn"; style="background-color: black;">
                    Pedir producto</button>
      </div>
                </li>`
        )
        .join('')}
    </ul>
  `;
}

function alerta(){
    swal("!Gracias por decirnoslo¡\n Lo mas pronto posible te enviaremos un  correo para decirte que el producto ya se encuentra disponible en la pagina")
}





//event listener in get lyrics button
result.addEventListener('click', e=>{
    const clickedElement = e.target;

    //checking clicked elemet is button or not
    if (clickedElement.tagName === 'SPAN'){
        const artist = clickedElement.getAttribute('data-artist');
        const songTitle = clickedElement.getAttribute('data-songtitle');
        
        getLyrics(artist, songTitle)
    }
})

// Get lyrics for song
async function getLyrics(artist, songTitle) {
    const res = await fetch(`${apiURL}/v1/${artist}/${songTitle}`);
    const data = await res.json();
  
    const lyrics = data.lyrics.replace(/(\r\n|\r|\n)/g, '<br>');
  
    result.innerHTML = `<div class="full-lyrics"><h2><strong>${artist}</strong> - ${songTitle}</h2>
    <p>${lyrics}</p></div>`;
  
  }