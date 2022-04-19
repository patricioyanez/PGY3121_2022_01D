function sumar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;

    if(n1 == "" || n2 == "")
    {
        alert("No especifico un número");
        return;
    }

    let total = parseInt(n1) + parseInt(n2);
    let mensaje = "El total es: " + total; 
    alert(mensaje);
    document.getElementById("lblMensaje").innerHTML = mensaje;
}