from django.db import models

# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID Paciente')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(unique=True, verbose_name='email')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProveedoresSeguros (models.Model):
    proveedor_id = models.AutoField(primary_key=True, verbose_name='ID Proveedor')
    proveedor_nombre = models.CharField(max_length=50, verbose_name='Nombre Proveedor')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SegurosPacientes (models.Model):
    seguro_paciente_id = models.AutoField(primary_key=True, verbose_name='ID Seguro')
    seguro_nombre = models.CharField(max_length=50, verbose_name='Plan de Seguro')
    id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(ProveedoresSeguros, on_delete=models.CASCADE)
    numero_asociado = models.IntegerField(unique=True, verbose_name='Número de Afiliado')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Especialidades (models.Model):
    especialidad_id = models.AutoField(primary_key=True, verbose_name='ID Especialidad')
    especialidad_nombre = models.CharField(max_length=50, verbose_name='Especialidad')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profesionales (models.Model):
    profesional_id = models.AutoField(primary_key=True, verbose_name='ID Profesional')
    profesional_nombre = models.CharField(max_length=50, verbose_name='Nombre Profesional')
    profesional_apellido = models.CharField(max_length=50, verbose_name='Apellido Profesional')
    especialidad_id = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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


class Estudios (models.Model):
    estudio_id = models.AutoField(primary_key=True, verbose_name='ID Estudio')
    estido_nombre = models.CharField(max_length=50, verbose_name='Nombre Estudio')
    estudio_descripcion = models.CharField(max_length=100, verbose_name='Descripción Estudio')
    estudio_precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Estudio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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


class Facturas (models.Model):
    factura_id = models.AutoField(primary_key=True, verbose_name='ID Factura')
    factura_numero = models.IntegerField(unique=True, verbose_name='Número Factura')
    factura_fecha = models.DateField(verbose_name='Fecha Factura')
    pago_id = models.ForeignKey(Pagos, on_delete=models.CASCADE, verbose_name='ID Pago')    
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Insumos (models.Model):
    insumo_id = models.AutoField(primary_key=True, verbose_name='ID Insumo')
    insumo_nombre = models.CharField(max_length=50, verbose_name='Nombre Insumo')
    insumo_descripcion = models.CharField(max_length=100, verbose_name='Descripción Insumo')
    stock_actual = models.CharField(max_length=5,verbose_name='Stock Actual')
    stock_minimo = models.CharField(max_length=5, verbose_name='Stock Mínimo')
    unidad_medida = models.CharField(max_length=50, verbose_name='Unidad de Medida')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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


