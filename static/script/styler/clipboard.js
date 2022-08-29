$(function(){
    var intv = setInterval(function(){ $(".copybutton").html('<i class="fas fa-copy">&nbsp;</i>Copy'); }, 2000);
      $("body").on('click',".copybutton",function() { 
    $(".copybutton").html('<i class="fas fa-copy">&nbsp;</i>Copy');
    $(this).html('Copied'); 
    clearInterval(intv);
    });
    });
    
        var clipboard = new ClipboardJS('.copybutton');
        /* clipboard.on('success', function(e) {
            console.info('Action:', e.action);
            console.info('Text:', e.text);
        });
        
        clipboard.on('error', function(e) {
            console.error('Action:', e.action);
            console.error('Trigger:', e.trigger);
        });
        */
    
    