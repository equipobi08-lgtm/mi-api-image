# Crear el archivo README.md con la descripción del proyecto
@"
# API de Captura de Pantalla

Esta API permite capturar una captura de pantalla de una página web utilizando Selenium y Flask.

---

## 🧪 Uso

Realiza una solicitud GET a \`/captura\` con el parámetro \`url\`:

\`\`\`
GET /captura?url=https://ejemplo.com
\`\`\`

Respuesta:

\`\`\`json
{
  "image": "data:image/png;base64,..."
}
\`\`\`

🚀 Despliegue
Esta API está desplegada en Render.com.

\`\`\`bash
git clone https://github.com/tu-usuario/mi-api-image.git
cd mi-api-image
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
\`\`\`
"@ | Out-File -FilePath README.md -Encoding UTF8