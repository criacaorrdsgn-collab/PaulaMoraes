document.addEventListener("DOMContentLoaded", () => {
    // 1. Scroll Animations (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // observer.unobserve(entry.target); // Deixe comentando se quiser que a animação repita
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-in-up');
    animatedElements.forEach(el => observer.observe(el));

    // 2. Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Parallax Hero Effect (Sutil)
    const heroBg = document.querySelector('.hero-premium');
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        if(heroBg && scrolled < window.innerHeight) {
            heroBg.style.backgroundPositionY = -(scrolled * 0.3) + 'px';
        }
    });
});
