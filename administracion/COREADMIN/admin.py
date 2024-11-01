from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from coreadmin.models import *
from django.contrib.auth.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('paciente_id', 'name', 'last_name', 'dni')
    search_fields = ('paciente_id', 'name', 'last_name', 'dni')
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
    list_display = ('solicitud_id', 'estado_solicitud', 'solicitud_fecha', 'insumo_id', 'cantidad_solicitada', 'solicitado_por', 'fecha_completada', 'fecha_actualizacion')
    search_fields = ('solicitud_id', 'estado_solicitud', 'solicitud_fecha', 'insumo_id', 'cantidad_solicitada', 'solicitado_por', 'fecha_completada', 'fecha_actualizacion')
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


class TurnosAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'paciente', 'profesional', 'app_date', 'app_time', 'status')
    list_filter = ('status', 'app_date', 'profesional')
    search_fields = ('paciente_name', 'profesional_nombre', 'notes')
    readonly_fields = ('created_at', 'updated_at')


class IngresoPacienteAdmin(admin.ModelAdmin):
    list_display = ('ingreso_id', 'paciente', 'profesional', 'fecha_ingreso', 'fecha_hora_completado', 'ingreso_tipo', 'ingreso_gravedad', 'estado')
    search_fields = ('paciente_name', 'fecha_ingreso', 'fecha_hora_completado', 'ingreso_tipo', 'ingreso_gravedad', 'estado')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Admin, UserAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(ProveedoresSeguros)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Profesionales, ProfesionalesAdmin)
admin.site.register(Estudios, EstudiosAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(Facturas, FacturasAdmin)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(SolicitudesInsumos, SolicitudesInsumosAdmin)
admin.site.register(ResultadoLaboratorio, ResultadoLaboratorioAdmin)
admin.site.register(Turnos, TurnosAdmin)
admin.site.register(IngresoPaciente, IngresoPacienteAdmin)
