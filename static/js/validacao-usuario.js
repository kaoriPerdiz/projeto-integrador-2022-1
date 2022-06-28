const emailValido = (email) => {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
}

function validacaoCadastro() {
    let nome = $('#nome').val()
    let email = $('#email').val()
    let senha = $('#senha').val()

    if (nome == '') {
        alert('Preencha o campo nome')
        return false
    }
    if (email == '') {
        alert('Preencha o campo e-mail')
        return false
    }
    if (senha == '') {
        alert('Preencha o campo senha')
        return false
    }
    if (!emailValido(email)) {
        alert('E-mail inválido')
        return false
    }
}

const validacaoInformacoes = () => {
    let idade = $('#idade').val()
    let genero = $('input[name=genero]:checked', '#formulario').val()
    let telefone = $('#telefone').val()
    let primeiroEmprego = $('input[name=primeiroEmprego]:checked', '#formulario').val()

    if (idade == '') {
        alert('Preencha o campo idade')
        return false
    } else if (idade <= 0 || idade >= 100) {
        alert('Idade inválida')
        return false
    }

    if (genero === undefined) {
        alert('Selecione um gênero')
        return false
    }

    if (telefone == '(11) 11111-1111' || telefone == '(22) 22222-2222' || telefone == '(33) 33333-3333' ||
    telefone == '(44) 44444-4444' || telefone == '(55) 55555-5555' || telefone == '(66) 66666-6666' ||
    telefone == '(77) 77777-7777' || telefone == '(88) 88888-8888' || telefone == '(99) 99999-9999' ||
    telefone == '(00) 00000-0000' || telefone == '(12) 34567-8901' || telefone == '') {
        alert('Informe um número válido')
        return false
    }
    if (primeiroEmprego === undefined) {
        alert('Selecione um motivo')
        return false
    }
}

function mask(o, f) {
    setTimeout(function () {
        var v = mphone(o.value);
        if (v != o.value) {
            o.value = v;
        }
    }, 1);
}

function mphone(v) {
    var r = v.replace(/\D/g, "");
    r = r.replace(/^0/, "");
    if (r.length > 10) {
        r = r.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (r.length > 5) {
        r = r.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (r.length > 2) {
        r = r.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        r = r.replace(/^(\d*)/, "($1");
    }
    return r;
}