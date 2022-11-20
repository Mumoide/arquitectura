(function() {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
      btn.addEventListener("click",(evento)=>{
        const confirmacion=confirm("¿Seguro de eliminar el usuario?");
        if (!confirmacion) {
          evento.preventDefault();
        }
      });
    });
})();

var message_ele = document.getElementById('mensaje');

setTimeout(function () {
  message_ele.style.display = "none";
}, 5000);