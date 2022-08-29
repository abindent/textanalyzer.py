$(function(){
  var intv = setInterval(function(){ $(".imgValueCopier").html('<i class="fas fa-copy">&nbsp;</i>Copy'); }, 2000);
  $("body").on('click',".imgValueCopier", function() { 
  $(".imgValueCopier").html('<i class="fas fa-copy">&nbsp;</i>Copy');
  $(this).html('Copied'); 
  clearInterval(intv);
 
});
});

   var clipboard = new ClipboardJS('.imgValueCopier');
  
