document.addEventListener('DOMContentLoaded', function () {
    // Check the user's preference for dark mode
    const isDarkMode = localStorage.getItem('dark-mode') === 'enabled';

    // Set the initial mode based on user preference
    toggleDarkMode(isDarkMode);

    // Add event listener to the dark mode toggle button
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function () {
            // Toggle dark mode on button click
            const newMode = document.body.classList.contains('dark-mode') ? 'disabled' : 'enabled';
            localStorage.setItem('dark-mode', newMode);
            toggleDarkMode(newMode === 'enabled');
        });
    }

    // Function to toggle dark mode styles
    function toggleDarkMode(enabled) {
        document.body.classList.toggle('dark-mode', enabled);
    }
});