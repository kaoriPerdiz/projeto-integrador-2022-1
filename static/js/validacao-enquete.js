function validation() {
    let motivo = $('input[name=motivo]:checked', '#formulario').val()
    if(motivo === undefined){
        alert('Selecione um motivo')
        return false
    }
    return true
}