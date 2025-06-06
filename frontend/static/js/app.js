document.addEventListener('DOMContentLoaded', () => {
  // Verificar autenticación
  const authToken = localStorage.getItem('authToken');
  const isLoginPage = window.location.pathname.includes('login.html');
  
  if (!authToken && !isLoginPage) {
    window.location.href = '/login.html';
    return;
  }
  
  if (authToken && isLoginPage) {
    window.location.href = '/empleados.html';
    return;
  }
  
  if (!isLoginPage) {
    cargarEmpleados();
  }
});

async function cargarEmpleados() {
  try {
    const response = await fetch('/api/empleados');
    const empleados = await response.json();
    const tbody = document.getElementById('empleadosList');
    tbody.innerHTML = empleados.map(emp => `
      <tr>
        <td>${emp.nombre}</td>
        <td>${emp.posicion}</td>
        <td>${emp.salario}</td>
        <td>
          <button class="btn btn-sm btn-warning" onclick="editarEmpleado(${emp.id})">Editar</button>
          <button class="btn btn-sm btn-danger" onclick="eliminarEmpleado(${emp.id})">Eliminar</button>
        </td>
      </tr>
    `).join('');
  } catch (error) {
    console.error('Error cargando empleados:', error);
  }
}

async function guardarEmpleado(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const empleado = Object.fromEntries(formData.entries());
  
  try {
    const response = await fetch('/api/empleados', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(empleado)
    });
    
    if (response.ok) {
      window.location.href = '/empleados.html';
    }
  } catch (error) {
    console.error('Error guardando empleado:', error);
  }
}

function handleLogin(event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const credenciales = Object.fromEntries(formData.entries());
  
  // Autenticación básica - ¡MEJORAR para producción!
  if(credenciales.usuario === 'admin' && credenciales.contrasena === 'admin123') {
    localStorage.setItem('authToken', 'dummy-token');
    window.location.href = '/empleados.html';
  } else {
    alert('Credenciales incorrectas');
  }
}

function logout() {
  localStorage.removeItem('authToken');
  window.location.href = '/login.html';
}