$(function() { 
    /*if($.trim($("#fancytext").val())!='') { 
       generateFancy($("#fancytext").val());
     } else {
      generateFancy("Preview Text");
     }*/
     
   $(".fancytext").keyup(function() { 
      $(".fancytext").val($(this).val());
      if($.trim($(this).val())!='') { 
      generateFancy($(this).val());
      } else {
      generateFancy("Preview Text");
      }
    });
   var ct = 89;
   function generateFancy(txt) {
     var fancyText = '';
        var result = forward(txt);
            var finalRes =  result.split('\n\n');
            var sn=1;
           $.each(finalRes,function(inx, vl) { 
               $("#copy_"+inx).val(vl);
               
            
             sn++;
           });
           
           
           for(k=89; k<=ct; k++) {
               //console.log(k);
               $("#copy_"+k).val(crazyWithFlourishOrSymbols(txt));
           }
             
   }
    
    $(".loadmore").click(function(){
      $(this).text('Loading...');
       var text = $.trim($(".fancytext").val());
      if(text=='') {
        text = 'Preview Text';
      } 
      var that = $(this);
      var intvl = setInterval(function(){  that.text('Load More');clearInterval(intvl); }, 1000);
      for(var i=1;i<=10;i++){
       fancyText  =  '<div class="input flex mb-2"><input type="text" class="bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-not-allowed dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 text-'+ct+'" value="'+crazyWithFlourishOrSymbols(text)+'" id="copy_'+ct+'" disabled readonly> <button type="button" class="copybutton text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" data-clipboard-action="copy" data-clipboard-target="#copy_'+ct+'"><i class="fas fa-copy">&nbsp;</i>Copy</button></div>';
         ct++;
       $("#result").append(fancyText);
       }
    });
   
   });