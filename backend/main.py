from fastapi import FastAPI, Depends, HTTPException, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import jwt
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

# Configurar rutas estáticas PRIMERO para servir el frontend
app.mount("/", StaticFiles(directory="frontend/templates", html=True), name="templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redirección desde raíz a login
@app.get("/")
async def root():
    return RedirectResponse(url="/login")

# Modelo Pydantic para login
class LoginRequest(BaseModel):
    username: str
    password: str

# Configuración de autenticación
SECRET_KEY = "clave_secreta_nominas"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Base de datos temporal
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    }
}

# Importar rutas de la API
from backend.services import payroll, reports
from fastapi import APIRouter

# Router para empleados
empleados_router = APIRouter(prefix="/api")

@empleados_router.post("/login")
async def login(username: str, password: str):
    user = fake_users_db.get(login_data.username)
    if not user or user["password"] != login_data.password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(
        {"sub": username, "exp": datetime.utcnow() + access_token_expires},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return {"token": access_token}

@empleados_router.get("/empleados", tags=["Empleados"])
async def get_empleados():
    # Simulación de datos
    return [
        {"id": 1, "nombre": "Juan Pérez", "posicion": "Desarrollador", "salario": 50000, "fecha_ingreso": "2023-01-15"},
        {"id": 2, "nombre": "María García", "posicion": "Diseñadora", "salario": 45000, "fecha_ingreso": "2023-03-20"}
    ]

@empleados_router.post("/empleados", tags=["Empleados"])
async def create_empleado():
    return {"message": "Empleado creado"}

@empleados_router.put("/empleados/{empleado_id}", tags=["Empleados"])
async def update_empleado(empleado_id: int):
    return {"message": f"Empleado {empleado_id} actualizado"}

@empleados_router.delete("/empleados/{empleado_id}", tags=["Empleados"])
async def delete_empleado(empleado_id: int):
    return {"message": f"Empleado {empleado_id} eliminado"}