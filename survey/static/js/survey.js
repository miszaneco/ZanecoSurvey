function onchange_rate_type(rate_type){
//var rate_type = document.getElementById('#rate_type');
//alert(rate_type);

switch(rate_type.value){
    case 'Worst':{
    document.getElementById('rate').value = 1
    return
    }

    case 'Poor':{
    document.getElementById('rate').value = 2
    return
    }

    case 'Fair':{
    document.getElementById('rate').value = 3
    return
    }

    case 'Good':{
    document.getElementById('rate').value = 4
    return
    }

    case 'Excellent':{
    document.getElementById('rate').value = 5
    return
    }
}
}