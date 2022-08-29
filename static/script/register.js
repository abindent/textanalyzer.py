$("#show_pass").click(function () {
    $(this).is(':checked') ? togglePass("text", "Hide") : togglePass("password", "Show");
})


function togglePass(type, text){
    $("#password").attr("type", type)
    $("#cpassword").attr("type", type)
    $("#show_pass_span").text(text)
}