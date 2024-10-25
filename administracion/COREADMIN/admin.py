from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from coreadmin.models import *
from django.contrib.auth.models import User


class ClinicaSePrice(admin.AdminSite):
    site_header = 'Sistema de Gestión Clinica SePrice'
    site_title = 'Clinica SePrice'
    index_title = 'Panel de Control'
    empty_value_display = 'No hay datos disponibles'


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'dni')
    search_fields = ('id', 'name', 'last_name', 'dni')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('especialidad_id', 'especialidad_nombre')
    search_fields = ('especialidad_id', 'especialidad_nombre')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ProfesionalesAdmin(admin.ModelAdmin):
    list_display = ('profesional_id', 'profesional_nombre', 'profesional_apellido', 'especialidad_id')
    search_fields = ('profesional_id', 'profesional_nombre', 'profesional_apellido', 'especialidad_id')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TurnosAdmin(admin.ModelAdmin):
    list_display = ('turno_id', 'turno_fecha', 'turno_hora', 'profesional_id', 'paciente_id', 'estado_ENUM')
    search_fields = ('turno_id', 'turno_fecha', 'turno_hora', 'profesional_id', 'paciente_id', 'estado_ENUM')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class EstudiosAdmin(admin.ModelAdmin):
    list_display = ('estudio_id', 'estudio_nombre')
    search_fields = ('estudio_id', 'estudio_nombre')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PagosAdmin(admin.ModelAdmin):
    list_display = ('pago_id', 'pago_creacion', 'pago_fecha', 'pago_monto', 'pago_medio_ENUM', 'pago_estado_NUM', 'paciente_id')
    search_fields = ('pago_id', 'pago_creacion', 'pago_fecha', 'pago_monto', 'pago_medio_ENUM', 'pago_estado_NUM', 'paciente_id')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class FacturasAdmin(admin.ModelAdmin):
    list_display = ('factura_id', 'factura_numero', 'factura_fecha', 'pago_id', 'paciente_id')
    search_fields = ('factura_id', 'factura_numero', 'factura_fecha', 'pago_id', 'paciente_id')
    readonly_fields = ('created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class InsumosAdmin(admin.ModelAdmin):
    list_display = ('insumo_id', 'insumo_nombre','stock_actual', 'stock_minimo', 'unidad_medida')
    search_fields = ('insumo_id', 'insumo_nombre','stock_actual', 'stock_minimo', 'unidad_medida')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class SolicitudesInsumosAdmin(admin.ModelAdmin):
    list_display = ('solicitud_id', 'solicitud_fecha', 'insumo_id', 'cantidad_solicitada', 'estado_solicitud_ENUM', 'solicitado_por', 'fecha_completada', 'fecha_actualizacion')
    search_fields = ('solicitud_id', 'solicitud_fecha', 'insumo_id', 'cantidad_solicitada', 'estado_solicitud_ENUM', 'solicitado_por', 'fecha_completada', 'fecha_actualizacion')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class VisitasGuardiaAdmin(admin.ModelAdmin):
    list_display = ('visita_id', 'paciente_id', 'visita_fecha', 'visita_hora', 'visita_gravedad_ENUM', 'estado_ENUM', 'fecha_hora_completado')
    search_fields = ('visita_id', 'paciente_id', 'visita_fecha', 'visita_hora', 'visita_gravedad_ENUM', 'estado_ENUM', 'fecha_hora_completado')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class VisitasLaboratorioAdmin(admin.ModelAdmin):
    list_display = ('visita_id', 'paciente_id', 'visita_fecha', 'visita_hora', 'estado_ENUM', 'fecha_hora_completado')
    search_fields = ('visita_id', 'paciente_id', 'visita_fecha', 'visita_hora', 'estado_ENUM', 'fecha_hora_completado')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ResultadoLaboratorioAdmin(admin.ModelAdmin):
    list_display = ('resultado_id', 'visita_id', 'estudio_id', 'resultado_fecha')
    search_fields = ('resultado_id', 'visita_id', 'estudio_id','resultado_fecha')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



# Register your models here.
site_admin = ClinicaSePrice(name='clinica_seprice')
site_admin.register(Paciente, PacienteAdmin)
site_admin.register(ProveedoresSeguros)
site_admin.register(Especialidades, EspecialidadesAdmin)
site_admin.register(Profesionales, ProfesionalesAdmin)
site_admin.register(Turnos, TurnosAdmin)
site_admin.register(Estudios, EstudiosAdmin)
site_admin.register(Pagos, PagosAdmin)
site_admin.register(Facturas, FacturasAdmin)
site_admin.register(Insumos, InsumosAdmin)
site_admin.register(SolicitudesInsumos, SolicitudesInsumosAdmin)
site_admin.register(VisitasGuardia, VisitasGuardiaAdmin)
site_admin.register(VisitasLaboratorio, VisitasLaboratorioAdmin)
site_admin.register(ResultadoLaboratorio, ResultadoLaboratorioAdmin)

