document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('nav');
    const toggleBtn = nav?.querySelector('button[aria-controls="nav-links"]');
    const navLinks = nav?.querySelectorAll('#nav-links a');

    if (toggleBtn && nav) {
        // Toggle menu
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            nav.classList.toggle('nav-open');
            const isOpen = nav.classList.contains('nav-open');
            toggleBtn.setAttribute('aria-expanded', isOpen.toString());
        });

        // Close on link click
        if (navLinks) {
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (nav.classList.contains('nav-open')) {
                        nav.classList.remove('nav-open');
                        toggleBtn.setAttribute('aria-expanded', 'false');
                    }
                });
            });
        }

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (nav.classList.contains('nav-open') && !nav.contains(e.target)) {
                nav.classList.remove('nav-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && nav.classList.contains('nav-open')) {
                nav.classList.remove('nav-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.focus();
            }
        });

        // Ensure nav resets properly if resized past mobile breakpoint
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768 && nav.classList.contains('nav-open')) {
                nav.classList.remove('nav-open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
        });

        // Navbar shrink on scroll
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }
});
