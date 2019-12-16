window.onload = function() {
    var code = document.getElementsByClassName("language-python")[0];
    code.style.display = "none";
  };

function show_hide_solution() {
    var code = document.getElementsByClassName("language-python")[0];
    var button = document.getElementById("show");
    if (code.style.display === "none") {
      code.style.display = "block";
      button.innerHTML = "Hide Solution";
    } else {
      code.style.display = "none";
      button.innerHTML = "Show Solution";
    }
  }