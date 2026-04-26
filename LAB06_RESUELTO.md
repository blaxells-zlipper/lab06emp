# Laboratorio 06 Resuelto - Django Templates

## Estado

Laboratorio implementado de extremo a extremo en el proyecto:

- `C:\Users\Mauricio\Desktop\tecsupp\lab06empr\lab06`

Incluye:

- Modelos `Categoria` y `Producto`.
- Registro en Admin.
- Vistas `index`, `producto`, `productos_por_categoria`.
- Menu lateral de categorias en inicio y detalle.
- Vista de productos por categoria.
- Campo de foto para categoria y producto.
- Datos cargados (categorias y productos de la guia).
- Imagenes generadas para cada categoria y producto.

## Credenciales de administrador

- Usuario: `admin`
- Contrasena: `Tecsup2023`

## URLs de prueba

- Inicio tienda: `http://127.0.0.1:8000/tienda/`
- Detalle producto (ejemplo): `http://127.0.0.1:8000/tienda/producto/1/`
- Productos por categoria (ejemplo): `http://127.0.0.1:8000/tienda/categoria/1/`
- Admin: `http://127.0.0.1:8000/admin/`

## Comandos para ejecutar

```bash
cd C:\Users\Mauricio\Desktop\tecsupp\lab06empr\lab06
..\venv\Scripts\python manage.py runserver
```

## Observaciones

- Se implemento la herencia de plantillas con `layout.html` para evitar duplicacion de codigo.
- Se corrigio la ruta de la app `tienda` para mantener la estructura correcta junto a `manage.py`.
- Se agrego `Pillow` para soportar carga de imagenes en modelos.
- Se habilito `MEDIA_URL` y `MEDIA_ROOT` para servir fotos en desarrollo.
- Se realizaron pruebas de rutas y todas responden con estado HTTP 200.

## Conclusiones

- El motor de plantillas de Django permite separar claramente estructura base y contenido por vista.
- El uso de ORM facilito filtrar productos por categoria y renderizar datos dinamicos.
- La integracion de static/media completo el flujo visual requerido por el laboratorio.
- La app resultante cumple el requerimiento funcional principal y la tarea adicional.
- El proyecto queda listo para ampliaciones futuras (carrito, buscador, autenticacion cliente).
