function abrir(imageSrc, text) {
    const modal = document.getElementById("transparente");
    const cardContent = document.querySelector(".card-conteudo");

    document.getElementById("Imagem").src = imageSrc;
    document.getElementById("Texto").textContent = text;

    modal.style.display = 'flex';
    cardContent.style.opacity = 0;
    cardContent.style.transform = 'scale(0.8)';

    setTimeout(() => {
        cardContent.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
        cardContent.style.opacity = 1;
        cardContent.style.transform = 'scale(1)';
    }, 50);
}

function fechar(event) {
    if (event.target.id === "transparente") {
        const modal = document.getElementById("transparente");
        const cardContent = document.querySelector(".card-conteudo");

        cardContent.style.transition = 'transform 0.3s ease, opacity 0.3s ease';
        cardContent.style.opacity = 0;
        cardContent.style.transform = 'scale(0.8)';

        setTimeout(() => {
            modal.style.display = 'none';
        }, 300); 
    }
}

var musicaAtual = "";  

function playMusic(musicFile) {
    var audioPlayer = document.getElementById("musicPlayer");
    var audioSource = document.getElementById("audioSource");

    
    if (musicaAtual === musicFile) {
        if (audioPlayer.paused) {
            audioPlayer.play();  
        } else {
            audioPlayer.pause();  
        }
    } else {
        audioSource.src = musicFile;
        audioPlayer.load();  
        audioPlayer.play();  
        musicaAtual = musicFile;  
    }
}






