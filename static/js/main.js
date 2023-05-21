function myFunction() {
    let text="Choose a button!";
    if (confirm(text) == true) {
        text="You pressed OK! JavaScript confirmed as working.";
    } else {
        text="You cancelled! JavaScript confirmed as working.";
    }
    document.getElementById("demo").innerHTML = text;
}