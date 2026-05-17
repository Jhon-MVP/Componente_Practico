# Changelog

## [v1.0.0] - 2026-05-17

### Agregado
- Sistema CRUD completo para Marca, Usuario, Dispositivo, Asignacion y Mantenimiento
- Autenticacion de usuarios con modelo personalizado
- Archivo .gitignore para excluir archivos sensibles
- Archivo requirements.txt con dependencias del proyecto
- Tests unitarios para modelos Marca y Usuario
- Pipeline de integracion continua con GitHub Actions

### Seguridad
- Validacion de formularios para prevenir datos invalidos
- Proteccion CSRF habilitada en todas las vistas
- Login requerido en todas las vistas del inventario
