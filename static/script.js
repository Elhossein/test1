let mainNav1 = document.getElementById("first-js-menu");
let navBarToggle1 = document.getElementById("first-js-navbar-toggle");
let btn1 = document.getElementById('first-btn');
navBarToggle1.addEventListener("click", function() {
    mainNav1.classList.toggle("hide");
    mainNav1.classList.toggle("active");
    btn1.classList.toggle('right')
    btn1.classList.toggle("down");
});


let mainNav2 = document.getElementById("second-js-menu");
let navBarToggle2 = document.getElementById("second-js-navbar-toggle");
let btn2 = document.getElementById('second-btn');
navBarToggle2.addEventListener("click", function() {
    mainNav2.classList.toggle("hide");
    mainNav2.classList.toggle("active");
    btn2.classList.toggle('right')
    btn2.classList.toggle("down");
});

let mainNav3 = document.getElementById("third-js-menu");
let navBarToggle3 = document.getElementById("third-js-navbar-toggle");
let btn3 = document.getElementById('third-btn');
navBarToggle3.addEventListener("click", function() {
    mainNav3.classList.toggle("hide");
    mainNav3.classList.toggle("active");
    btn3.classList.toggle('right')
    btn3.classList.toggle("down");
});

let mainNav4 = document.getElementById("forth-js-menu");
let navBarToggle4 = document.getElementById("forth-js-navbar-toggle");
let btn4 = document.getElementById('forth-btn');
navBarToggle4.addEventListener("click", function() {
    mainNav4.classList.toggle("hide");
    mainNav4.classList.toggle("active");
    btn4.classList.toggle('right')
    btn4.classList.toggle("down");
});