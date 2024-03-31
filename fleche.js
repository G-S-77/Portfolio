const btn1 = document.querySelector('.btn1');

btn1.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    })
})