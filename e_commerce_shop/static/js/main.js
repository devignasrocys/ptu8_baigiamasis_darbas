const btn = document.getElementById("menu-btn");

btn.addEventListener("click", (e) => {
    e.preventDefault();
    document.getElementById("navbar").classList.toggle("display");
})

let slideIndex =  0
const carousele = () => {
    let i = 0;
    const hero_elements = document.getElementsByClassName("carousele__slide");
    for (i = 0; i < hero_elements.length; i++) {
        hero_elements[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > hero_elements.length) {slideIndex = 1}
    hero_elements[slideIndex-1].style.display = "block"
    setTimeout(carousele, 2000)
}
carousele()
