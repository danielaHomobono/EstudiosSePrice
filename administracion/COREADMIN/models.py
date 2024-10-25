from django.db import models

# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Paciente')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(unique=False, verbose_name='email')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.id} - {self.name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = "Pacientes"


class ProveedoresSeguros (models.Model):
    proveedor_id = models.AutoField(primary_key=True, verbose_name='ID Proveedor')
    proveedor_nombre = models.CharField(max_length=50, verbose_name='Nombre Proveedor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.proveedor_nombre
    
    class Meta:
        verbose_name_plural = "Proveedores de Seguros"


class SegurosPacientes (models.Model):
    seguro_paciente_id = models.AutoField(primary_key=True, verbose_name='ID Seguro')
    seguro_nombre = models.CharField(max_length=50, verbose_name='Plan de Seguro')
    id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(ProveedoresSeguros, on_delete=models.CASCADE)
    numero_asociado = models.CharField(unique=True, max_length=15, verbose_name='Número de Afiliado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.seguro_paciente_id} - {self.seguro_nombre} - {self.numero_asociado}'
    
    class Meta:
        verbose_name_plural = "Seguros de Pacientes"


class Especialidades (models.Model):
    especialidad_id = models.AutoField(primary_key=True, verbose_name='ID Especialidad')
    especialidad_nombre = models.CharField(max_length=50, verbose_name='Especialidad')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.especialidad_nombre

    class Meta:
        verbose_name_plural = "Especialidades"


class Profesionales (models.Model):
    profesional_id = models.AutoField(primary_key=True, verbose_name='ID Profesional')
    profesional_nombre = models.CharField(max_length=50, verbose_name='Nombre Profesional')
    profesional_apellido = models.CharField(max_length=50, verbose_name='Apellido Profesional')
    especialidad_id = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.profesional_id} - {self.profesional_nombre} {self.profesional_apellido}'

    class Meta:
        verbose_name_plural = "Profesionales"


class Turnos (models.Model):
    turno_id = models.AutoField(primary_key=True, verbose_name='ID Turno')
    turno_fecha = models.DateField(verbose_name='Fecha Turno')
    turno_hora = models.TimeField(verbose_name='Hora Turno')
    profesional_id = models.ForeignKey(Profesionales, on_delete=models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    estado_ENUM = (
        ('Programado', 'Programado'),
        ('Completado', 'Completado'),
        ('Cancelado', 'Cancelado'),
        ('Ausente', 'Ausente'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.turno_id} - {self.turno_fecha} {self.turno_hora} - {self.estado_ENUM}'

    class Meta:
        verbose_name_plural = "Turnos"


class Estudios (models.Model):
    estudio_id = models.AutoField(primary_key=True, verbose_name='ID Estudio')
    estudio_nombre = models.CharField(max_length=50, verbose_name='Nombre Estudio')
    estudio_descripcion = models.CharField(max_length=100, verbose_name='Descripción Estudio')
    estudio_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Estudio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.estudio_id} - {self.estudio_nombre}'

    class Meta:
        verbose_name_plural = "Estudios"


class Pagos (models.Model):
    pago_id = models.AutoField(primary_key=True, verbose_name='ID Pago')
    turno_id = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    pago_creacion = models.DateField(verbose_name='Fecha Creación')
    pago_fecha = models.DateField(verbose_name='Fecha Pago')
    pago_monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto Pago')
    pago_medio_ENUM = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta de débito', 'Tarjeta de débito'),
        ('Tarjeta de crédito', 'Tarjeta de crédito'),
        ('Seguro', 'Seguro'),
    )
    pago_estado_NUM = (
        ('Pendiente', 'Pendiente'),
        ('Acreditado', 'Acreditado'),
        ('Rechazado', 'Rechazado'),
    )
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pago_id} - {self.pago_monto} - {self.pago_estado_NUM}'

    class Meta:
        verbose_name_plural = "Pagos"


class Facturas (models.Model):
    factura_id = models.AutoField(primary_key=True, verbose_name='ID Factura')
    factura_numero = models.IntegerField(unique=True, verbose_name='Número Factura')
    factura_fecha = models.DateField(verbose_name='Fecha Factura')
    pago_id = models.ForeignKey(Pagos, on_delete=models.CASCADE, verbose_name='ID Pago')    
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.factura_numero}'

    class Meta:
        verbose_name_plural = "Facturas"


class Insumos (models.Model):
    insumo_id = models.AutoField(primary_key=True, verbose_name='ID Insumo')
    insumo_nombre = models.CharField(max_length=50, verbose_name='Nombre Insumo')
    insumo_descripcion = models.CharField(max_length=100, verbose_name='Descripción Insumo')
    stock_actual = models.CharField(max_length=5,verbose_name='Stock Actual')
    stock_minimo = models.CharField(max_length=5, verbose_name='Stock Mínimo')
    unidad_medida = models.CharField(max_length=50, verbose_name='Unidad de Medida')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.insumo_id} - {self.insumo_nombre} - {self.stock_actual}'

    class Meta:
        verbose_name_plural = "Insumos"


class SolicitudesInsumos (models.Model):
    solicitud_id = models.AutoField(primary_key=True, verbose_name='ID Solicitud')
    solicitud_fecha = models.DateField(verbose_name='Fecha Solicitud')
    insumo_id = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    cantidad_solicitada = models.CharField(max_length=5, verbose_name='Cantidad Solicitada')
    estado_solicitud_ENUM = (
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Completada', 'Completada'),
    )
    solicitado_por = models.CharField(max_length=50, verbose_name='Solicitado por')
    fecha_completada = models.DateField(verbose_name='Fecha Completada')
    fecha_actualizacion = models.DateField(verbose_name='Fecha Actualización')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.solicitud_id} - {self.insumo_id} - {self.estado_solicitud_ENUM}'

    class Meta:
        verbose_name_plural = "Solicitudes de Insumos"


class VisitasGuardia (models.Model):
    visita_id = models.AutoField(primary_key=True, verbose_name='ID Visita')
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    visita_fecha = models.DateField(verbose_name='Fecha Visita')
    visita_hora = models.TimeField(verbose_name='Hora Visita')
    visita_gravedad_ENUM = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    )
    estado_ENUM = (
        ('Esperando', 'Esperando'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    )
    fecha_hora_completado = models.DateTimeField(verbose_name='Fecha y Hora Completado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.visita_id} - {self.paciente_id} - {self.estado_ENUM}'

    class Meta:
        verbose_name_plural = "Visitas de Guardia"


class VisitasLaboratorio (models.Model):
    visita_id = models.AutoField(primary_key=True, verbose_name='ID Visita')
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    visita_fecha = models.DateField(verbose_name='Fecha Visita')
    visita_hora = models.TimeField(verbose_name='Hora Visita')
    estado_ENUM = (
        ('Esperando', 'Esperando'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    )
    fecha_hora_completado = models.DateTimeField(verbose_name='Fecha y Hora Completado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.visita_id} - {self.paciente_id} - {self.estado_ENUM}'

    class Meta:
        verbose_name_plural = "Visitas de Laboratorio"


class ResultadoLaboratorio (models.Model):
    resultado_id = models.AutoField(primary_key=True, verbose_name='ID Resultado')
    visita_id = models.ForeignKey(VisitasLaboratorio, on_delete=models.CASCADE)
    estudio_id = models.ForeignKey(Estudios, on_delete=models.CASCADE)
    resultado_detalle = models.CharField(max_length=200, verbose_name='Detalle Resultado')
    created_at = models.DateTimeField(auto_now_add=True)
    resultado_fecha = models.DateField(verbose_name='Fecha Resultado')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.resultado_id} - {self.resultado_fecha}'
    
    class Meta:
        verbose_name_plural = "Resultados de Laboratorio"