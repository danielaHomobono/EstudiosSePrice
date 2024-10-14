
function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active-section');
    });
    
    const activeSection = document.getElementById(sectionId);
    if (activeSection) {
        activeSection.classList.add('active-section');
    }
}


function handleFormSubmit(formId, successMessage) {
    document.getElementById(formId).addEventListener('submit', function(e) {
        e.preventDefault();
        alert(successMessage);
        this.reset();
    });
}


document.addEventListener('DOMContentLoaded', function() {
    handleFormSubmit('registro-paciente-form', 'Paciente registrado exitosamente');
    handleFormSubmit('agendar-turno-form', 'Turno agendado exitosamente');
    handleFormSubmit('laboratorio-sin-turno-form', 'Paciente registrado para laboratorio');
    handleFormSubmit('guardia-sin-turno-form', 'Paciente registrado para guardia');
    handleFormSubmit('insumos-form', 'Insumo registrado exitosamente');
    handleFormSubmit('pagos-facturacion-form', 'Pago procesado exitosamente');
    handleFormSubmit('recepcion-paciente-form', 'Estado del paciente actualizado');
});


function verificarTurno() {
    const nombrePaciente = document.getElementById('nombre-paciente').value;
    const fechaTurno = document.getElementById('fecha-turno').value;
    
   
    if (nombrePaciente && fechaTurno) {
        alert(`Turno verificado para ${nombrePaciente} en la fecha ${fechaTurno}`);
    } else {
        alert('Por favor, ingrese el nombre del paciente y la fecha del turno');
    }
}


function verificarStock() {
    const nombreInsumo = document.getElementById('nombre-insumo').value;
    
    
    if (nombreInsumo) {
        alert(`Verificando stock de ${nombreInsumo}. Esta función se conectaría a una base de datos en una aplicación real.`);
    } else {
        alert('Por favor, ingrese el nombre del insumo');
    }
}
