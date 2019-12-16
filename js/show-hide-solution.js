window.onload = function() {
    document.getElementById('b-navbar-fg').style.display = 'none';
    var x = document.getElementsByClassName("language-python")[0];
    x.style.display = 'none';
  };

function show_hide_solution() {
    var x = document.getElementsByClassName("language-python")[0];
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }