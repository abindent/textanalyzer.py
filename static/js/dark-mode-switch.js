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
    } else {
      pass1.type = "password";
      pass2.type = "password";
    }
  }


  function disableall() {

    let switch1 = document.getElementById("customSwitch1")
    let switch2 = document.getElementById("customSwitch2")
    let switch3 = document.getElementById("customSwitch8")
    let switch4 = document.getElementById("customSwitch3")
    let switch5 = document.getElementById("customSwitch4")
    let switch6 = document.getElementById("customSwitch6")
    let switch7 = document.getElementById("customSwitch7")
    let switch8 = document.getElementById("customSwitch10")
    let switchcount = document.getElementById("customSwitch5")

      switch1.disabled = true;
      switch2.disabled = true;
      switch3.disabled = true;
      switch4.disabled = true;
      switch5.disabled = true;
      switch6.disabled = true;
      switch7.disabled = true;
      switch8.disabled = true;
      switch1.checked = false;
      switch2.checked = false;
      switch3.checked = false;
      switch4.checked = false;
      switch5.checked = false;
      switch6.checked = false;
      switch7.checked = false;
      switch8.checked = false;
    if(switchcount.checked == false){
      switch1.disabled = false;
      switch2.disabled = false;
      switch3.disabled = false;
      switch4.disabled = false;
      switch5.disabled = false;
      switch6.disabled = false;
      switch7.disabled = false;
      switch8.disabled = false;
    }
  }

if (location.protocol !== 'https:') {
    location.replace(`https:${location.href.substring(location.protocol.length)}`);
}
