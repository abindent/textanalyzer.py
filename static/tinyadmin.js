var script= document.createElement('script');
script.type='text/javascript';
script.src="https://cdn.tiny.cloud/1/gjvp0jzu4kr5c37zixrvdmw931aoemzbatvuadw17iich6eh/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload=function(){
tinymce.init({
    selector: "#id_content",
    height:656,
    plugins: [
      'advlist autolink link image lists charmap print preview hr anchor pagebreak',
      'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
      'table emoticons template paste help codesample spellchecker'
    ],
      toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | print preview media fullpage | ' +
      'forecolor backcolor emoticons | spellchecker | codesample help ',
      menu: {
      favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
    },
      menubar: 'favs file edit view insert format tools table help',
      content_css: 'css/content.css',
      browser_spellcheck: true,
      contextmenu: false,
      content_css: 'css/content.css',
      spellchecker_callback: function (method, text, success, failure) {
        var words = text.match(this.getWordCharPattern());
        if (method === "spellcheck") {
          var suggestions = {};
          for (var i = 0; i < words.length; i++) {
            suggestions[words[i]] = ["First", "Second"];
          }
          success({ words: suggestions, dictionary: [ ] });
        } else if (method === "addToDictionary") {
          // Add word to dictionary here
          success();
        }
      }
      });
}
