// Ajax call to do CRUD operations from the data taken from server side

// $(document).ready(function(){$.get("/dashboard", {direction:"left"}).done(function (data) 
// {for (var i = 0; i < data.length; i ++) {
//     $("#dashboardtable").append("<tr><td>" + data[i].customer_id + "</td><td>" + data[i].customer_name + "</td><td>" + data[i].phone_no + "</td><td>" + data[i].email_id + "</td><td>" + data[i].address + "</td></tr>");
// }
//     alert("left button clicked");})});

const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle");
      sidebar = body.querySelector("nav");
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if(getMode && getMode ==="dark"){
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if(getStatus && getStatus ==="close"){
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () =>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        localStorage.setItem("mode", "dark");
    }else{
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if(sidebar.classList.contains("close")){
        localStorage.setItem("status", "close");
    }else{
        localStorage.setItem("status", "open");
    }
})