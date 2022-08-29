function disabledAll(elem){

    let showText;
    
    if(elem.checked){
         showText = "disabled"
    }
    else{
        showText = "enabled again"
    }

    alert(`All the options except the selected will be ${showText}. Do you want to procceed?`)
    $("#optionsTab").find("input:checkbox").each(function(){
        if(elem.checked && this !== elem){
            $(this).prop("disabled", true);
            $(this).prop('checked', false);
        }
        else{
            
            if($(this) !== $("#switch_9") && $(this) !== $("#switch_10")){
               $(this).prop("disabled", false);
            }
        }
    })
}