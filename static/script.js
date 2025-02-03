function enviarMensaje() {
    fetch('/tarea')
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").innerText = data.message;
        })
        .catch(error => console.error('Error:', error));
}
