(function() {
    "use strict";

    var treeviewMenu = $('.app-menu');

    // Toggle Sidebar
    $('[data-toggle="sidebar"]').click(function(event) {
        event.preventDefault();
        $('.app').toggleClass('sidenav-toggled');
    });

    // Activate sidebar treeview toggle
    $("[data-toggle='treeview']").click(function(event) {
        event.preventDefault();
        if (!$(this).parent().hasClass('is-expanded')) {
            treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
        }
        $(this).parent().toggleClass('is-expanded');
    });

    // Set initial active toggle
    $("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

    //Activate bootstrip tooltips
    $("[data-toggle='tooltip']").tooltip();

})();

let dateDropdown = document.getElementById('date-dropdown');

let currentYear = new Date().getFullYear();
let earliestYear = 2015;
while (currentYear >= earliestYear) {
    let dateOption = document.createElement('option');
    dateOption.text = currentYear;
    dateOption.value = currentYear;
    dateDropdown.add(dateOption);
    currentYear -= 1;
}

(function() {

    var date = new Date();

    var today = new Date(date.getFullYear(),
        date.getFullYear.Month(), date.getDate());

    var optDatetoday = {
        format: 'mm-dd-yyyy',
        todayHighlight: true,
        orientation: 'bottom right',
        autoclose: true,


    }

    document.getElementById("datetoday").innerHTML = date;

})();
