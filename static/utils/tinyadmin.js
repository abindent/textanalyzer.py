var script= document.createElement('script');

script.type='text/javascript';
script.src=`/static/packages/tinymce/tinymce.min.js`;

document.head.appendChild(script);


script.onload = function(){

    tinymce.init({
        selector: '#id_content',

        height:656,
      
        plugins: [
          'lists', 'advlist', 'anchor', 'link', 'autolink', 'quickbars', 'table', 'image', 'media', 'help', 'print', 'preview', 'autosave', 'charmap', 'emoticons', 'insertdatetime',
          'code', 'codesample', 'help', 'save', 'searchreplace', 'fullscreen', 'directionality', 'insertdatetime'
        ],
      
        toolbar: [
          'undo redo | blocks  | bold italic  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | ltr rtl | link quickimage quicktable | insertdatetime anchor',
          'save print preview media | forecolor backcolor emoticons  | restoredraft charmap | code codesample help | fullscreen'],
    
      
      })

}