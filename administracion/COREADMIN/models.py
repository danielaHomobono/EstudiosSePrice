from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime



# Create your models here.
class Admin (models.Model):
    admin_id = models.AutoField(primary_key=True, verbose_name='ID Admin')
    username = models.CharField(max_length=50, unique=True, verbose_name='Username')
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(unique=True, verbose_name='email')
    admin_password = models.CharField(max_length=100, verbose_name='Contraseña')
    admin_dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    admin_telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    status = models.BooleanField(default=False)  # admin status (approved/on-hold)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin.username} Perfil Admin'

    class Meta:
        unique_together = ('date_joined', 'time')
        ordering = ['date_joined', 'time']

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
    paciente_id = models.AutoField(primary_key=True, verbose_name='ID Paciente')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(unique=True, max_length=8, verbose_name='DNI')
    phone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(unique=False, verbose_name='email')
    image = models.ImageField(default="default.png", upload_to="profile_pictures", null=True, blank=True)  # profile picture
    proveedor_nombre = models.ForeignKey(ProveedoresSeguros, on_delete=models.CASCADE)
    plan_seguro = models.CharField(max_length=50, verbose_name='Plan')
    numero_asociado = models.CharField(unique=True, max_length=20, verbose_name='Número de Afiliado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.paciente.username} Perfil Paciente'
    
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
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    especialidad_id = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)  # doctor status(approved/on-hold)

    def __str__(self):
        return f'{self.profesional_nombre} Perfil Profesional'

    class Meta:
        verbose_name_plural = "Profesionales"
        ordering = ['profesional_apellido']



class Estudios (models.Model):
    estudio_id = models.AutoField(primary_key=True, verbose_name='ID Estudio')
    estudio_nombre = models.CharField(max_length=50, verbose_name='Nombre Estudio')
    estudio_descripcion = models.CharField(max_length=100, verbose_name='Descripción Estudio')
    estudio_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Estudio')
    profesional = models.ForeignKey(Profesionales, on_delete=models.CASCADE, related_name="Estudios", default=1)  # doctor fk
    app_total = models.IntegerField(default=0)  # total patients/appointments completed by doctor
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.estudio_id} - {self.estudio_nombre} Información Estudios'

    class Meta:
        verbose_name_plural = "Estudios"
        ordering = ['estudio_nombre']



class Turnos(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='turnos')
    especialidad = models.ForeignKey('Especialidades', on_delete=models.CASCADE, related_name='turnos')
    estudio = models.ForeignKey('Estudios', on_delete=models.CASCADE, related_name='turnos')
    profesional = models.ForeignKey('Profesionales', on_delete=models.CASCADE, related_name='turnos')
    app_link = models.TextField(null=True, blank=True)  # video call room link
    app_date = models.DateField(null=True, blank=True)  # call date
    app_time = models.TimeField(null=True, blank=True)  # call time/slot
    status = models.CharField(max_length=20, choices=[
        ('SCHEDULED', 'Programada'),
        ('CONFIRMED', 'Confirmada'),
        ('CHECKED_IN', 'Checked in'),
        ('CHECKED_OUT', 'Checked out'),
        ('CANCELLED', 'Cancelada'),
    ], default='SCHEDULED')
    completed = models.BooleanField(default=False)  # appointment completed/to-be-done
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} Información del turno'
    
    class Meta:
        unique_together = ('profesional', 'app_date', 'app_time')
        ordering = ['app_date', 'app_time']
        verbose_name_plural = "Turnos"


class IngresoPaciente(models.Model):
    ingreso_id = models.AutoField(primary_key=True, verbose_name='ID Visita')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesionales, on_delete=models.CASCADE)
    estudio_nombre = models.ForeignKey(Estudios, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha Visita')
    ingreso_hora = models.TimeField(verbose_name='Hora Visita')
    ingreso_tipo = models.CharField(max_length=20, choices=[
        ('SIN_TURNO', 'Ingreso por Guardia'),
        ('CON_TURNO', 'Ingreso con Turno'),
    ], default='CON_TURNO')
    ingreso_gravedad = models.CharField(max_length=10, choices=[
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
        verbose_name_plural = "Ingreso"
        ordering = ['fecha_ingreso']

    def __str__(self):
        return f'{self.visita_id} - {self.paciente} - {self.estado}'



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
    visita_id = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE)
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

