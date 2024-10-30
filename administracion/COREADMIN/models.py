from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
import uuid



# Create your models here.
class ProveedoresSeguros (models.Model):
    proveedor_id = models.AutoField(primary_key=True, verbose_name='ID Proveedor')
    proveedor_nombre = models.CharField(max_length=50, verbose_name='Nombre Proveedor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.proveedor_nombre
    
    class Meta:
        verbose_name_plural = "Proveedores de Seguros"
        ordering = ['proveedor_nombre']



class Paciente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Paciente')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(unique=False, verbose_name='email')
    proveedor_nombre = models.ForeignKey(ProveedoresSeguros, on_delete=models.CASCADE)
    plan_seguro = models.CharField(max_length=50, verbose_name='Plan')
    numero_asociado = models.CharField(unique=True, max_length=20, verbose_name='Número de Afiliado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.last_name} {self.name}'
    
    class Meta:
        verbose_name_plural = "Pacientes"
        ordering = ['last_name']



class Especialidades (models.Model):
    especialidad_id = models.AutoField(primary_key=True, verbose_name='ID Especialidad')
    especialidad_nombre = models.CharField(max_length=50, verbose_name='Especialidad')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.especialidad_nombre

    class Meta:
        verbose_name_plural = "Especialidades"
        ordering = ['especialidad_nombre']



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
        ordering = ['profesional_apellido']



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
        ordering = ['estudio_nombre']



class Turnos(models.Model):
    APPOINTMENT_STATUS = [
        ('SCHEDULED', 'Programada'),
        ('CONFIRMED', 'Confirmada'),
        ('CHECKED_IN', 'Checked in'),
        ('CHECKED_OUT', 'Checked out'),
        ('CANCELLED', 'Cancelada'),
    ]

    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='turnos')
    especialidad = models.ForeignKey('Especialidades', on_delete=models.CASCADE, related_name='turnos')
    estudio = models.ForeignKey('Estudios', on_delete=models.CASCADE, related_name='turnos')
    professional = models.ForeignKey('Profesionales', on_delete=models.CASCADE, related_name='turnos')
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(default=timezone.timedelta(minutes=15))
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default='SCHEDULED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('professional', 'date', 'time')
        ordering = ['date', 'time']
        verbose_name_plural = "Turnos"

    def __str__(self):
        return f"Turno: {self.patient} para {self.estudio} con {self.professional} el {self.date} a las {self.time}"

    def clean(self):
        super().clean()
        if not self.is_slot_available(self.professional, self.date, self.time, self.duration):
            raise ValidationError("This time slot is not available.")


    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @classmethod
    def is_slot_available(cls, professional, date, time, duration):
        end_time = (datetime.combine(date, time) + duration).time()
        return not cls.objects.filter(
            professional=professional,
            date=date,
            time__lt=end_time,
            time__gt=(datetime.combine(date, time) - duration).time()
        ).exists()

    

class IngresoVisita(models.Model):
    VISITA_TIPO = [
        ('SIN_TURNO', 'Ingreso por Guardia'),
        ('CON_TURNO', 'Ingreso con Turno'),
    ]

    visita_id = models.AutoField(primary_key=True, verbose_name='ID Visita')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    visita_fecha = models.DateField(verbose_name='Fecha Visita')
    visita_hora = models.TimeField(verbose_name='Hora Visita')
    visita_tipo = models.CharField(max_length=20, choices=VISITA_TIPO, default='CON_TURNO')
    visita_gravedad = models.CharField(max_length=10, choices=[
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ], null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[
        ('Esperando', 'Esperando'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ])
    fecha_hora_completado = models.DateTimeField(verbose_name='Fecha y Hora Completado', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Visitas"
        ordering = ['visita_fecha']

    def __str__(self):
        return f'{self.visita_id} - {self.paciente} - {self.estado}'



class Pagos (models.Model):
    pago_id = models.AutoField(primary_key=True, verbose_name='ID Pago')
#    turno_id = models.ForeignKey(Turnos, on_delete=models.CASCADE)
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
        ordering = ['pago_fecha']



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
        ordering = ['factura_numero']



class Insumos (models.Model):
    insumo_id = models.AutoField(primary_key=True, verbose_name='ID Insumo')
    insumo_nombre = models.CharField(max_length=50, verbose_name='Nombre Insumo')
    insumo_descripcion = models.CharField(max_length=100, verbose_name='Descripción Insumo')
    stock_actual = models.IntegerField(verbose_name='Stock Actual')
    stock_minimo = models.IntegerField(verbose_name='Stock Mínimo')
    unidad_medida = models.CharField(max_length=50, verbose_name='Unidad de Medida')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.insumo_id} - {self.insumo_nombre} - {self.stock_actual}'

    class Meta:
        verbose_name_plural = "Insumos"
        ordering = ['insumo_nombre']



class SolicitudesInsumos(models.Model):
    ESTADO_SOLICITUD_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
        ('Completada', 'Completada'),
    ]
    estado_solicitud = models.CharField(max_length=20, choices=ESTADO_SOLICITUD_CHOICES, default='Pendiente')
    solicitud_id = models.AutoField(primary_key=True, verbose_name='ID Solicitud')
    solicitud_fecha = models.DateField(verbose_name='Fecha Solicitud')
    insumo_id = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    cantidad_solicitada = models.CharField(max_length=5, verbose_name='Cantidad Solicitada')
    solicitado_por = models.CharField(max_length=50, verbose_name='Solicitado por')
    fecha_completada = models.DateField(verbose_name='Fecha Completada', null=True, blank=True)
    fecha_actualizacion = models.DateField(verbose_name='Fecha Actualización', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.solicitud_id} - {self.insumo_id} - {self.estado_solicitud}'
    
    class Meta:
        verbose_name_plural = "Solicitudes de Insumos"
        ordering = ['solicitud_fecha', 'estado_solicitud']



class ResultadoLaboratorio (models.Model):
    resultado_id = models.AutoField(primary_key=True, verbose_name='ID Resultado')
    visita_id = models.ForeignKey(IngresoVisita, on_delete=models.CASCADE)
    estudio_id = models.ForeignKey(Estudios, on_delete=models.CASCADE)
    resultado_detalle = models.CharField(max_length=200, verbose_name='Detalle Resultado')
    created_at = models.DateTimeField(auto_now_add=True)
    resultado_fecha = models.DateField(verbose_name='Fecha Resultado')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f'{self.resultado_id} - {self.resultado_fecha}'
    
    class Meta:
        verbose_name_plural = "Resultados de Laboratorio"
        ordering = ['resultado_fecha']

