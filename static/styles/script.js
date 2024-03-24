document.addEventListener("DOMContentLoaded", function () {

    const scroll = document.getElementById('scroll');

    scroll.addEventListener('click', function () {
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    });
});