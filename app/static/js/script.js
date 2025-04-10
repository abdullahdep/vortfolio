var script = document.createElement('script');

// Set the src attribute to the Bootstrap CDN
script.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js";

// Set the script to load asynchronously
script.async = true;





// header

// Append the script element to the body or head of the document
document.head.appendChild(script);
    document.addEventListener('DOMContentLoaded', function () {
        const userIcons = document.querySelectorAll('.user-icon');

        userIcons.forEach(icon => {
            const toggle = icon.querySelector('.nav-link');
            const dropdown = icon.querySelector('.custom-dropdown');

            toggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                // Close all other dropdowns
                userIcons.forEach(other => {
                    if (other !== icon) {
                        other.classList.remove('active');
                    }
                });

                // Toggle current dropdown
                icon.classList.toggle('active');

                // Check scroll indicators after dropdown is shown
                if (icon.classList.contains('active')) {
                    checkScrollIndicators(dropdown);
                }
            });

            // Add scroll event listener to dropdown
            if (dropdown) {
                dropdown.addEventListener('scroll', () => {
                    checkScrollIndicators(dropdown);
                });
            }
        });

        // Function to check and update scroll indicators
        function checkScrollIndicators(dropdown) {
            const isScrollable = dropdown.scrollHeight > dropdown.clientHeight;
            const isAtTop = dropdown.scrollTop <= 0;
            const isAtBottom = dropdown.scrollHeight - dropdown.scrollTop === dropdown.clientHeight;

            dropdown.classList.toggle('show-top-indicator', isScrollable && !isAtTop);
            dropdown.classList.toggle('show-bottom-indicator', isScrollable && !isAtBottom);
        }

        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.user-icon')) {
                userIcons.forEach(icon => {
                    icon.classList.remove('active');
                });
            }
        });

        // Prevent dropdown clicks from closing
        document.querySelectorAll('.custom-dropdown').forEach(dropdown => {
            dropdown.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });

        // Add touch events for mobile
        if ('ontouchstart' in window) {
            document.addEventListener('touchstart', (e) => {
                if (!e.target.closest('.user-icon')) {
                    userIcons.forEach(icon => icon.classList.remove('active'));
                }
            });
        }

        // Add smooth scroll behavior for dropdown items
        document.querySelectorAll('.dropdown-item').forEach(item => {
            item.addEventListener('click', function (e) {
                const dropdown = this.closest('.custom-dropdown');
                const section = this.closest('.dropdown-section');
                if (section) {
                    e.preventDefault();
                    section.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
            });
        });

        // Add section header dropdown functionality
        const sectionHeaders = document.querySelectorAll('.section-header-dropdown');

        sectionHeaders.forEach(header => {
            header.addEventListener('click', () => {
                const section = header.dataset.section;
                const content = document.getElementById(`${section}-content`);

                // Toggle active class
                header.classList.toggle('active');
                content.classList.toggle('active');

                // Close other sections
                sectionHeaders.forEach(otherHeader => {
                    if (otherHeader !== header) {
                        const otherSection = otherHeader.dataset.section;
                        const otherContent = document.getElementById(`${otherSection}-content`);
                        otherHeader.classList.remove('active');
                        otherContent.classList.remove('active');
                    }
                });
            });
        });
    });

    function toggleFullscreenMenu(event) {
        event.preventDefault();
        const menu = document.getElementById('fullscreenMenu');
        menu.classList.toggle('active');
        document.body.style.overflow = menu.classList.contains('active') ? 'hidden' : '';
    }

    // Add smooth scroll for navbar links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Add hover effect for dropdowns
    document.querySelectorAll('.dropdown').forEach(dropdown => {
        dropdown.addEventListener('mouseenter', () => {
            const menu = dropdown.querySelector('.dropdown-menu');
            if (menu) menu.classList.add('show');
        });
        dropdown.addEventListener('mouseleave', () => {
            const menu = dropdown.querySelector('.dropdown-menu');
            if (menu) menu.classList.remove('show');
        });
    });
