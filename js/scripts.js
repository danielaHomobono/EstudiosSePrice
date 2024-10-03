// Validaciones o funciones JavaScript necesarias
document.addEventListener('DOMContentLoaded', function() {
    // Aquí puedes manejar interacciones del usuario
    console.log("Página cargada correctamente");
});

document.getElementById('registro-paciente-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Captura los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const dni = document.getElementById('dni').value;
    const contacto = document.getElementById('contacto').value;
    const obraSocial = document.getElementById('obra-social').value;
    const numeroAsociado = document.getElementById('numero-asociado').value;

    // Simular el envío de los datos al backend
    console.log({
        nombre,
        dni,
        contacto,
        obraSocial,
        numeroAsociado
    });

    alert('Paciente registrado exitosamente');
});

