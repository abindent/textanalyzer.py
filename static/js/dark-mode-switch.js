  function darkModetoggle() {
      var element = document.body;
      element.classList.toggle("dark-mode");
  }

  function password_show_hide() {
  var x = document.getElementById("loginpass");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

   function password_show_hide_register() {
 var pass1 = document.getElementById("pass1");
 var pass2 = document.getElementById("pass2"); 
 if (pass1.type === "password" || pass2.type === "password" || pass1.type === "password" && pass2.type === "password") {
      pass1.type = "text";
      pass2.type = "text";
   } 
 else {
     pass1.type = "password";
     pass2.type = "password";    
   }
}


