from datetime import date
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Empleado(Base):
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    puesto = Column(String(50))
    registros = relationship("RegistroLaboral", back_populates="empleado")

class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    tipo_pago = Column(String(20), nullable=False)
    tarifas = relationship("Tarifa", back_populates="evento")

class Tarifa(Base):
    __tablename__ = 'tarifas'
    id = Column(Integer, primary_key=True)
    evento_id = Column(Integer, ForeignKey('eventos.id'), index=True)
    monto = Column(Float, nullable=False)
    vigencia_desde = Column(Date, nullable=False)
    evento = relationship("Evento", back_populates="tarifas")

class RegistroLaboral(Base):
    __tablename__ = 'registros_laborales'
    id = Column(Integer, primary_key=True, index=True)
    empleado_id = Column(Integer, ForeignKey('empleados.id'), index=True)
    evento_id = Column(Integer, ForeignKey('eventos.id'), index=True)
    fecha = Column(Date, nullable=False)
    cantidad = Column(Float, nullable=False)
    estado = Column(String(20), default='pendiente')
    evidencias_url = Column(String(200))
    comentarios_supervisor = Column(String(300))
    
    empleado = relationship("Empleado", back_populates="registros")
    evento = relationship("Evento")