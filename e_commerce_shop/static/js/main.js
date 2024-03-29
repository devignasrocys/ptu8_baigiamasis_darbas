// MOBILE MENU
const btn = document.getElementById("menu-btn");
const toggleMenu = () => {
    document.getElementById("navbar").classList.toggle("display");
    document.querySelector(".burger-btn__span").classList.toggle("active")
}
btn.addEventListener("click", toggleMenu)


// CAROUSELE
let slideIndex =  0
const carousele_slides = document.getElementsByClassName("carousele__slide");
if (carousele_slides.length > 0) {
    const carousele = () => {
        let i = 0;
        for (i = 0; i < carousele_slides.length; i++) {
            carousele_slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > carousele_slides.length - 1) {slideIndex = 0}
        carousele_slides[slideIndex].style.display = "block"
        setTimeout(carousele, 5000)
    }
    carousele()
}

// PRODUCT IMAGES PREVIEW
const images_arr = document.querySelectorAll(".product-details__small-img")
if (images_arr.length > 0) {
    images_arr.forEach((image) => {
        image.addEventListener("click", (e) => {
            document.getElementById("product-preview-img").src = e.target.src
        })
    })
}

// MESSAGES 
const messages = document.querySelectorAll('.messages')
setTimeout(() => {
    messages.forEach(message => {
        message.style.display = 'none'
    })
},5000)
 
