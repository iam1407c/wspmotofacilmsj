# Documentación directa con python sin docker
- Revisar los puntos (a),(b),(c),(d) de la documentación formal con docker
- Ejecutar los siguientes comando
    ```
        cd app
        pip install -r requirements.txt
        python main.py
    ```

# Documentación formal con docker

#### a. Seguridad del Archivo `.env`

- **No compartas** el archivo `.env` públicamente, ya que contiene información sensible.
- Asegúrate de que `.env` esté listado en `.gitignore` para evitar que se suba a repositorios públicos.

#### a.1. Explicación de las Variables del Archivo `.env`

- **WHATSAPP_API_URL**: La URL base para la API de WhatsApp, normalmente provista por Meta. En este caso, estamos usando la versión `v18.0` de la API de WhatsApp Graph.
  
- **WHATSAPP_PHONE_NUMBER_ID**: El ID único de tu número de teléfono de WhatsApp Business. Este ID es necesario para enviar mensajes a través de la API y debe ser el mismo que está registrado en tu cuenta de WhatsApp Business.

- **WHATSAPP_ACCESS_TOKEN**: El token de acceso que se utiliza para autenticar las solicitudes API. Este token es generado en el panel de Meta Developers y tiene permisos asociados para interactuar con la API de WhatsApp. **Asegúrate de mantener este token seguro y no compartirlo públicamente.**

- **TEMPLATE_NAME**: El nombre exacto de la plantilla de mensaje que has creado y aprobado en tu cuenta de WhatsApp Business. Este nombre debe coincidir con la plantilla que está registrada en el panel de Meta. Por ejemplo, `welcome_message`.

- **LANGUAGE_CODE**: El código de idioma de la plantilla que estás utilizando. Asegúrate de que la plantilla tenga una traducción aprobada para el idioma que especifiques. Por ejemplo, usa `es` para español.

- **PHONE_COLUMN**: El nombre de la columna en el archivo CSV que contiene los números de teléfono de los destinatarios. Asegúrate de que esta columna esté correctamente definida y que los números estén en formato internacional.


#### b. Manejo de Errores y Logs

- Los logs se almacenan en la carpeta `app/logs/` como `send_messages.log`. Revisa este archivo para monitorear el progreso y detectar posibles errores.
- El `Makefile` también permite ver los logs en tiempo real con `make logs`.

#### c. Variables Dinámicas en Plantillas

- Asegúrate de que las variables en tu plantilla de WhatsApp correspondan con las que estás enviando en el script.
- Si tu plantilla requiere más variables, actualiza tanto el archivo `contacts.csv` como el script `main.py` para manejarlas adecuadamente.

#### d. Límites de la API

- **Evita exceder** los límites de la API de WhatsApp. Ajusta el `sleep(1)` en el script según los límites de tu cuenta.
- Considera implementar mecanismos más avanzados de rate limiting si es necesario.

### 8. Ejemplo Completo de Uso

1. **Clonar el Proyecto y Navegar al Directorio:**

    ```bash
        No usado
    ```

2. **Configurar el Archivo `.env`:**

    Edita el archivo `.env` con tus credenciales y configuraciones.

3. **Preparar los Contactos:**

    Asegúrate de que `app/data/contacts.csv` contenga los contactos y variables necesarias.

4. **Construir la Imagen Docker:**

    ```bash
    make build
    ```

5. **Ejecutar el Contenedor Docker:**

    ```bash
    make run
    ```

6. **Verificar los Logs:**

    ```bash
    make logs
    ```

### 9. Recursos Adicionales

- [Documentación de la WhatsApp Business API](https://developers.facebook.com/docs/whatsapp)
- [Guía de Plantillas de Mensajes](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates)
- [Docker Documentation](https://docs.docker.com/)
- [Makefile Tutorial](https://www.gnu.org/software/make/manual/make.html)
