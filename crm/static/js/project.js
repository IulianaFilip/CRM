
  document.addEventListener('DOMContentLoaded', function () {
    var navLinks = document.querySelectorAll('.nav.nav-pills .nav-link');

    navLinks.forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault();

        // Remove active class from all nav items
        navLinks.forEach(function (navLink) {
          navLink.classList.remove('active');
        });

        // Add active class to the clicked nav item
        this.classList.add('active');

        // Hide all tables
        var tables = document.querySelectorAll('.table-responsive');
        tables.forEach(function (table) {
          table.classList.add('d-none');
        });

        // Show the selected table
        var selectedTable = document.querySelector(this.getAttribute('href'));
        if (selectedTable) {
          selectedTable.classList.remove('d-none');
        }
      });
    });
  });
