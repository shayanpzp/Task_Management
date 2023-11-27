document.addEventListener('DOMContentLoaded', function () {
    const isDarkMode = localStorage.getItem('dark-mode') === 'enabled';

    toggleDarkMode(isDarkMode);

    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function () {
            const newMode = document.body.classList.contains('dark-mode') ? 'disabled' : 'enabled';
            localStorage.setItem('dark-mode', newMode);
            toggleDarkMode(newMode === 'enabled');
        });
    }

    function toggleDarkMode(enabled) {
        document.body.classList.toggle('dark-mode', enabled);
    }
});