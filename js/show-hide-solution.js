window.onload = function() {
    var x = document.getElementsByClassName("language-python")[0];
    x.style.display = "none";
  };

function show_hide_solution() {
    var x = document.getElementsByClassName("language-python")[0];
    if (x.style.display === "none") {
      x.style.display = "block";
      x.value = "Hide Solution";
    } else {
      x.style.display = "none";
      x.value = "Show Solution";
    }
  }