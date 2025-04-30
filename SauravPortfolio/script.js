const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Set initial theme to dark
body.setAttribute('data-theme', 'dark');
themeToggle.innerText = 'LIGHT';

themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    if (currentTheme === 'dark') {
        body.removeAttribute('data-theme');
        themeToggle.innerText = 'DARK';
    } else {
        body.setAttribute('data-theme', 'dark');
        themeToggle.innerText = 'LIGHT';
    }
});