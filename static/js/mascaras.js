function fMasc(objeto,mascara) {
  obj=objeto
  masc=mascara
  setTimeout("fMascEx()",1)
}

function fMascEx() {
  obj.value=masc(obj.value)
}

// MÁSCARA RG
function mRG(rg){
  rg=rg.replace(/\D/g,"")
  rg=rg.replace(/(\d{2})(\d)/,"$1.$2")
  rg=rg.replace(/(\d{3})(\d)/,"$1.$2")
  rg=rg.replace(/(\d{3})(\d{1,2})$/,"$1-$2")
  return rg
}

// MÁSCARA CPF
function mCPF(cpf){
  cpf=cpf.replace(/\D/g,"")
  cpf=cpf.replace(/(\d{3})(\d)/,"$1.$2")
  cpf=cpf.replace(/(\d{3})(\d)/,"$1.$2")
  cpf=cpf.replace(/(\d{3})(\d{1,2})$/,"$1-$2")
  return cpf
}

// MÁSCARA CNPJ
function mCNPJ(cnpj){
  cnpj=cnpj.replace(/\D/g,"")
  cnpj=cnpj.replace(/(\d{2})(\d)/,"$1.$2")
  cnpj=cnpj.replace(/(\d{3})(\d)/,"$1.$2")
  cnpj=cnpj.replace(/(\d{3})(\d)/,"$1/$2")
  cnpj=cnpj.replace(/(\d{4})(\d)/,"$1-$2")
  return cnpj
}

// MÁSCARA CEP
function mCEP(cep){
  cep=cep.replace(/\D/g,"")
  cep=cep.replace(/(\d{5})(\d)/,"$1-$2")
  cep=cep.replace(/(\d{5})(\d{1,3})$/,"$1-$2")
  return cep
}

// MÁSCARA DATA DE NASCIMENTO
function mDATA(data){
  data=data.replace(/\D/g,"")
  data=data.replace(/(\d{2})(\d)/,"$1/$2")
  data=data.replace(/(\d{2})(\d)/,"$1/$2")
  data=data.replace(/(\d{4})(\d{1,2})$/,"$1-$2")
  return data
}

// MÁSCARA TELEFONE
function mTEL(tel){
  tel=tel.replace(/\D/g,"")
  tel=tel.replace(/(\d{0})(\d)/,"$1($2")
  tel=tel.replace(/(\d{2})(\d)/,"$1) $2")
  tel=tel.replace(/(\d{5})(\d)/,"$1-$2")
  tel=tel.replace(/(\d{4})(\d)/,"$1$2")
  // tel=tel.replace(/D/g,"");             //Remove tudo o que não é dígito
  // tel=tel.replace(/^(d{2})(d)/g,"($1) $2"); //Coloca parênteses em volta dos dois primeiros dígitos
  // tel=tel.replace(/(d)(d{4})$/,"$1-$2");    //Coloca hífen entre o quarto e o quinto dígitos
    
  return tel
}

$("#divcar").ready(function(){
  var valor = $("input[id^='quantidade']");
  var valores = [];
  var total = 0
  valor.each(function(index){
    valores.push($( this )['context']['value'])
    var id_muda = $( this )['context']['id'].split('_')
    $('#total'+id_muda[1]).html(parseInt($('#total'+id_muda[1]).html())*parseInt($( this )['context']['value']))
    // $('quantidade_'+id_muda).html(parseInt($( this )['context']['value'])+parseInt($('quantidade_'+id_muda).html()))
  })

  var preco = $("td[id^='total']");
  var precos = [];
  preco.each(function(index){
    precos.push($( this )['context']['innerText'])
  })
  for (i = 0; i < precos.length; i++) {
    //var valor_item = parseInt(precos[i])*parseInt(valores[i])
    total = total+(parseInt(precos[i]))
  };
  $('#valorTotal').html('R$ '+total);
});


$("#id_cep").keyup(function(){
  var cep = $("#id_cep").val();
    if(cep.length == 9){
      $.post("/api_cep", {'cep': cep},
        function(resposta){
          $("#id_logradouro").val(resposta['logradouro']);
          $("#id_bairro").val(resposta['bairro']);
          $("#id_cidade").val(resposta['cidade']);
          $("#id_estado").val(converteEstado(resposta['uf']));

      console.log("CEP: " + resposta['uf']);
      console.log("CEP: " + resposta['cep']);
      })
    } 
  });
  
  function converteEstado(val) {
    var data;
    switch (val.toUpperCase()) {
      case "AC" : data = "Acre";                  break;
      case "AL" : data = "Alagoas";               break;
      case "AM" : data = "Amazonas";              break;
      case "AP" : data = "Amapa";                 break;
      case "BA" : data = "Bahia";                 break;
      case "CE" : data = "Ceara";                 break;
      case "DF" : data = "Distrito Federal";      break;
      case "ES" : data = "Espirito Santo";        break;
      case "GO" : data = "Goias";                 break;
      case "MA" : data = "Maranhao";              break;
      case "MG" : data = "Minas Gerais";          break;
      case "MS" : data = "Mato Grosso do Sul";    break;
      case "MT" : data = "Mato Grosso";           break;
      case "PA" : data = "Para";                  break;
      case "PB" : data = "Paraiba";               break;
      case "PE" : data = "Pernambuco";            break;
      case "PI" : data = "Piaui";                 break;
      case "PR" : data = "Parana";                break;
      case "RJ" : data = "Rio de Janeiro";        break;
      case "RN" : data = "Rio Grande do Norte";   break;
      case "RO" : data = "Rondonia";              break;
      case "RR" : data = "Roraima";               break;
      case "RS" : data = "Rio Grande do Sul";     break;
      case "SC" : data = "Santa Catarina";        break;
      case "SE" : data = "Sergipe";               break;
      case "SP" : data = "São Paulo";             break;
      case "TO" : data = "Tocantins";             break;
    }
    return data;
  };

function mudaPrecoVisual(id, preco){
    var quantidade = $("#quantidade_"+id).val();
    var tot = parseInt(quantidade)*parseInt(preco)
    console.log('ufa')
    console.log(tot);
    $.post("/qtd_carrinho", {'id': id, 'qtd':quantidade, 'total':tot});
    $("#total"+id).html(parseInt(quantidade)*parseInt(preco));
    var valores = $("td[id^='total']");
    var total = 0 
    valores.each(function(index){
      if(!isNaN(index)){
        total = total+parseInt($( this ).text());
      }
    })
    //ATUALIZANDO VALOR DO PRODUTO NO BANCO
    

    // $('.stripe-button').attr('data-amount',total);
    $('#valorTotal').html('R$ '+total);
    console.log(total.toString()+'00')
    
};


function checkout_pay(){
  var total = $('#valorTotal').text().replace('R$ ','')
  bloqueia_desbloqueia(true)
  console.log(total)
  $('#teste').each(function(i){           // Here you are modifying attribute
    $(this).attr('src', "https://checkout.stripe.com/checkout.js");
    $(this).attr('class',"stripe-button");
    $(this).attr('data-key',"pk_test_KoLJlYei9kUFrORmdpXFUvGZ00ojYcnPeW");
    $(this).attr('data-amount',total.toString()+'00');
    $(this).attr('data-name',"Organic Shop");
    $(this).attr('data-description',"Os melhores alimentos com você!");
    $(this).attr('data-locale',"auto");
    $(this).attr('data-image',"https://stripe.com/img/documentation/checkout/marketplace.png");
})
$('#valor_python').each(function(i){           // Here you are modifying attribute
  $(this).attr('value', total.toString()+'00');
});
};


function bloqueia_desbloqueia(opcao){
  $('#btn_pay').attr('hidden',opcao)
  var valores = $("input[id^='quantidade']");
  valores.each(function(index){
    $( this ).attr('disabled',opcao)
  });
}


// MÁSCARA CELULAR
function mCEL(cel){
  cel=cel.replace(/\D/g,"")
  cel=cel.replace(/(\d{0})(\d)/,"$1($2")
  cel=cel.replace(/(\d{2})(\d)/,"$1) $2")
  cel=cel.replace(/(\d{5})(\d)/,"$1-$2")
  cel=cel.replace(/(\d{4})(\d)/,"$1$2")
  return cel
}