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
function restar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;

    if(n1 == "" || n2 == "")
    {
        alert("No especifico un número");
        return;
    }

    let total = parseInt(n1) - parseInt(n2);
    let mensaje = "El total es: " + total; 
    alert(mensaje);
    document.getElementById("lblMensaje").innerHTML = mensaje;
}
function multiplicar()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;

    if(n1 == "" || n2 == "")
    {
        alert("No especifico un número");
        return;
    }

    let total = parseInt(n1) * parseInt(n2);
    let mensaje = "El total es: " + total; 
    alert(mensaje);
    document.getElementById("lblMensaje").innerHTML = mensaje;
}
function dividir()
{
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;

    if(n1 == "" || n2 == "")
    {
        alert("No especifico un número");
        return;
    }
    n2 = parseInt(n2);
    if(n2 == 0)
    {
        alert("No se puede dividir por cero");
        return; 
    }
    let total = parseInt(n1) / parseInt(n2);
    let mensaje = "El total es: " + total; 
    alert(mensaje);
    document.getElementById("lblMensaje").innerHTML = mensaje;
}