$(function()
{

    $('.btnGuardar').click(function()
    {
        if(!$('.txtNombre').val())
        {
            alert("error");
        // $('.chkActivo').prop('checked', 'false');
            return false;
        }
    });
    $('.btnLimpiar').click(function()
    {
        $('.txtId').val('');
        $('.txtNombre').val('');
        $('.chkActivo').prop('checked', false);
        return false;
    });
});