# 🏋️‍♂️ Gym API

Esta es una API RESTful para la gestión de planes de membresía en un gimnasio. El proyecto está desarrollado con **Django** y **Django REST Framework**, y está desplegado en **Render**.

## 🚀 Documentación en línea

Puedes acceder a la documentación completa de la API aquí:  
🔗 [https://gym-api-jslw.onrender.com/docs/](https://gym-api-jslw.onrender.com/docs/)

---
## ⚙️ Tecnologías utilizadas
- Python 3.12
- Django
- Django REST Framework
- SQLite3 (en desarrollo)
- Render (para despliegue)

## 👥 Integrantes del grupo
- Juan David Reina
- Sebastian Banderas
- Miguel Angel Lema
  
## 📦 Endpoints disponibles

Todos los endpoints están bajo la ruta base: `api/plans`
Documentacion: `/docs`

### 🔍 Obtener todos los planes
- **Método:** `GET`
- **URL:** `/plans/`
- **Descripción:** Retorna una lista de todos los planes disponibles.

### 🔍 Obtener un plan por ID
- **Método:** `GET`
- **URL:** `/plans/{id}/`
- **Descripción:** Retorna los detalles de un plan específico.

### ➕ Crear un nuevo plan
- **Método:** `POST`
- **URL:** `/plans/`
- **Descripción:** Crea un nuevo plan en la base de datos.

### ✏️ Actualizar un plan existente
- **Método:** `PUT`
- **URL:** `/plans/{id}/`
- **Descripción:** Actualiza completamente un plan existente.

### ❌ Eliminar un plan
- **Método:** `DELETE`
- **URL:** `/plans/{id}/`
- **Descripción:** Elimina un plan existente.

---

## 📄 Modelo de Plan (JSON)

```json
{
  "id": "string",
  "nombre": "string",
  "descripcion": "string",
  "precio": 0,
  "duracion_dias": 0,
  "acceso_piscina": true,
  "acceso_clases_grupales": true,
  "acceso_personal_trainer": false
}



