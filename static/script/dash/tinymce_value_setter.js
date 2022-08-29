// Function to get the value of tinymce editor
function setText() {

    try {
        // Fetching he value from tinymce editor
        let html_content;
        html_content = tinymce.activeEditor.getContent();

        // Setting the content
        $("#content").html(html_content);
        return true;

    }
    catch (e) {
        console.log(e)
        return false;
    }

}

// Function to submit the form 
$("#create_blog").submit(function(e){
    
    // Decalring a container boolean
    let boolean;

    // Stroing some value to that container  
    boolean = setText()

    // Submitting the form if "setText" function returns true else abroads the process
    if (boolean === true) {
       return true;       
    }
    else {
       return false;
    }

})
