tinymce.init({
  selector: '#mytextarea',

  plugins: [
    'lists', 'advlist', 'anchor', 'link', 'autolink', 'quickbars', 'table', 'image', 'media', 'help', 'preview', 'autosave', 'charmap', 'emoticons', 'insertdatetime',
    'code', 'codesample', 'help', 'save', 'searchreplace', 'fullscreen', 'directionality', 'insertdatetime'
  ],

  toolbar: [
    'undo redo | blocks  | bold italic  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | ltr rtl | link quickimage quicktable | insertdatetime anchor',
    'save print preview media | forecolor backcolor emoticons  | restoredraft charmap | code codesample help | fullscreen'],

      

})