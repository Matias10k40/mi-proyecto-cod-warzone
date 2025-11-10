<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Call of Duty: La Experiencia Definitiva de FPS (Trabajo Final)</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --color-dark-bg: #1a1a1a;
            --color-light-bg: #2b2b2b;
            --color-accent: #e50914; /* Rojo distintivo de CoD */
            --color-text-light: #f0f0f0;
            --color-text-dark: #cccccc;
            --font-primary: 'Roboto', sans-serif;
            --font-display: 'Orbitron', sans-serif;
        }

        body {
            font-family: var(--font-primary);
            margin: 0;
            padding-bottom: 80px; /* Espacio para el footer fijo */
            background-color: var(--color-dark-bg);
            color: var(--color-text-light);
            line-height: 1.6;
            overflow-x: hidden;
        }

        header {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://placehold.co/1920x400/000000/E50914?text=Fondo+de+CoD+aqui') no-repeat center center/cover; 
            padding: 80px 0;
            text-align: center;
            position: relative;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            overflow: hidden;
        }
        header::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.6); z-index: 1; }
        header h1 {
            margin: 0; font-family: var(--font-display); font-size: 3.8em; color: var(--color-accent); 
            text-shadow: 0 0 15px rgba(229, 9, 20, 0.7); position: relative; z-index: 2; animation: fadeInDown 1s ease-out;
        }
        header p {
            font-size: 1.5em; color: var(--color-text-dark); position: relative; z-index: 2; overflow: hidden;
            border-right: .15em solid var(--color-accent); white-space: nowrap; margin: 0 auto; letter-spacing: .1em;
            max-width: 800px; animation: typing 3s steps(40, end), blink-caret .75s step-end infinite;
            animation-delay: 1s; animation-fill-mode: forwards;
        }

        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-50px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes typing { from { width: 0 } to { width: 100% } }
        @keyframes blink-caret { from, to { border-color: transparent } 50% { border-color: var(--color-accent); } }

        .container { width: 90%; max-width: 1200px; margin: 40px auto; padding: 20px 0; }

        section {
            padding: 30px; margin-bottom: 40px; background: var(--color-light-bg); border-radius: 12px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5); transition: transform 0.3s ease-in-out;
            border-left: 5px solid var(--color-accent); opacity: 0; transform: translateY(20px);
            animation: sectionFadeIn 0.8s ease-out forwards;
        }
        section:hover { transform: translateY(-5px); }

        /* Retrasos para animacion escalonada */
        section:nth-of-type(1) { animation-delay: 2.5s; }
        section:nth-of-type(2) { animation-delay: 3s; }
        section:nth-of-type(3) { animation-delay: 3.5s; }
        section:nth-of-type(4) { animation-delay: 4s; }
        section:nth-of-type(5) { animation-delay: 4.5s; }
        section:nth-of-type(6) { animation-delay: 5s; }
        section:nth-of-type(7) { animation-delay: 5.5s; }

        @keyframes sectionFadeIn { to { opacity: 1; transform: translateY(0); } }

        h2 { font-family: var(--font-display); color: var(--color-accent); border-bottom: 3px solid var(--color-accent);
            padding-bottom: 10px; margin-top: 0; margin-bottom: 20px; text-shadow: 0 0 8px rgba(229, 9, 20, 0.4);
        }

        /* Estilos de Contenido e Imagenes */
        ul { list-style: none; padding-left: 0; }
        ul li { position: relative; padding-left: 30px; margin-bottom: 12px; color: var(--color-text-dark); }
        ul li::before { content: '»'; color: var(--color-accent); font-size: 1.2em; position: absolute; left: 0; top: 0; }
        
        .img-container { text-align: center; margin: 20px 0; }
        .img-container img {
            max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            transition: transform 0.4s ease; border: 3px solid #4a4a4a;
        }
        .img-container img:hover { transform: scale(1.02); border-color: var(--color-accent); }
        
        .info-list { margin-top: 20px; }
        .info-list li {
            background-color: #3a3a3a; padding: 15px; border-radius: 8px; margin-bottom: 15px;
            border-left: 3px solid var(--color-accent); transition: background-color 0.3s;
        }
        .info-list li:hover { background-color: #4a4a4a; }
        .info-list strong { color: var(--color-accent); font-family: var(--font-display); }
        
        /* Estilo para la aclaración */
        .aclaracion {
            padding: 10px 15px;
            background-color: #e5091420; /* Fondo rojo semitransparente */
            border: 1px solid var(--color-accent);
            border-radius: 6px;
            margin-top: 15px;
            font-weight: bold;
            color: var(--color-accent);
        }


        footer {
            background-color: #0d0d0d; color: var(--color-text-dark); text-align: center; padding: 20px 0;
            position: fixed; bottom: 0; width: 100%; border-top: 3px solid var(--color-accent);
            box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.4); z-index: 10;
        }
    </style>
</head>
<body>

    <header>
        <h1>CALL OF DUTY: WARZONE & HARDWARE</h1>
        <p>Tu próxima misión te espera: Análisis de Gaming y Componentes PC.</p>
    </header>

    <div class="container">

        <section id="parte1-intro">
            <h2>PARTE 1: Introducción a la Página Web y Servidor Local</h2>
            <p>Esta sección presenta el diseño de la página web de la franquicia **Call of Duty**, que combina un estilo moderno (CSS) con animaciones (CSS Keyframes) para una experiencia inmersiva.</p>
            <p>El código fuente ha sido desarrollado para ser ejecutado en un servidor local, como se evidencia a continuación, accesible mediante `127.0.0.1` o `localhost` (Nginx, 2024; W3Schools, 2024).</p>
        </section>

        <section id="parte1-evidencia">
            <h2>Puesta en Marcha del Servidor Web Local (Evidencia)</h2>
            <p>El servidor se levanta usando el servicio **Nginx** (Nginx, 2024), el cual sirve la página web a través del puerto por defecto, accesible mediante la dirección **`http://localhost`**.</p>
            
            <h3>1. Terminal con Servidor Nginx Activo:</h3>
            <p>Aquí se muestra la ejecución de Nginx en la terminal.</p>
            <div class="img-container">
                <img src="terminal_server_running.png" alt="Captura de pantalla de la terminal con el servidor Nginx activo.">
            </div>
            
            <h3>2. Navegador Accediendo a localhost:</h3>
            <p>Se muestra la página web cargada en el navegador, confirmando el acceso local.</p>
            <div class="img-container">
                <img src="browser_localhost_evidence.png" alt="Captura de pantalla del navegador mostrando la web en localhost.">
            </div>
        </section>

        <hr>

        <section id="parte2-mainboard">
            <h2>PARTE 2: Análisis de la Mainboard con CPU-Z</h2>
            <p>Se utilizó el programa **CPU-Z** (CPUID, 2024) para obtener la información detallada del sistema, específicamente el modelo de la Mainboard, lo cual es esencial para conocer las capacidades de expansión del equipo.</p>
            
            <h3>1. Modelo de la Mainboard (Evidencia CPU-Z):</h3>
            <p>La captura de pantalla de CPU-Z muestra el modelo exacto de la placa madre del equipo.</p>
            <div class="img-container">
                <img src="cpu_z_mainboard_capture.png" alt="Captura de CPU-Z mostrando la pestaña Mainboard.">
            </div>
            
            <h3>2. Datasheet y Características:</h3>
            <p>El manual de la Mainboard es crucial para cualquier actualización o diagnóstico avanzado (MSI, 2020).</p>

            <p>
                <strong>Enlace al Datasheet (Manual de Mantenimiento):</strong> 
                <a href="https://download-2.msi.com/archive/mnu_exe/nb/MS-16R6_v1.0_Spanish.zip" target="_blank" style="color: #4CAF50;">
                    Manual de Mantenimiento MSI GF63 Thin (GF63)
                </a>
            </p>
            
            <p class="aclaracion">
                **¡ACLARACIÓN!** Para el modelo de portátil MSI GF63, se utiliza el manual de mantenimiento del dispositivo como Datasheet funcional, ya que contiene toda la información de la Mainboard integrada.
            </p>

            <div class="img-container">
                <img src="la ram.png" alt="Captura de las especificaciones de la memoria RAM.">
            </div>
            
            <h3 style="margin-top: 30px;">3. Tres Características Destacadas de la Mainboard:</h3>
            <ul class="info-list">
                <li>
                    <strong>Característica 1: [Nombre de la Característica]</strong>
                    <p>Explicación: [Describir la característica y por qué te llamó la atención].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_CARACTERISTICA_1]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
                <li>
                    <strong>Característica 2: [Nombre de la Característica]</strong>
                    <p>Explicación: [Describir la característica y por qué te llamó la atención].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_CARACTERISTICA_2]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
                <li>
                    <strong>Característica 3: [Nombre de la Característica]</strong>
                    <p>Explicación: [Describir la característica y por qué te llamó la atención].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_CARACTERISTICA_3]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
            </ul>
        </section>

        <hr>

        <section id="parte3-bios">
            <h2>PARTE 3: Parámetros de la BIOS/UEFI</h2>
            
            <h3>1. Foto de la BIOS o UEFI (Evidencia):</h3>
            <p>La BIOS/UEFI es el firmware fundamental que inicializa y prueba los componentes del hardware (Techopedia, 2023).</p>
            <div class="img-container">
                <img src="bios_uefi_photo.jpg" alt="Foto de la interfaz BIOS o UEFI.">
            </div>
            
            <h3 style="margin-top: 30px;">2. Explicación de Tres Parámetros:</h3>
            <ul class="info-list">
                <li>
                    <strong>Parámetro 1: [Nombre del Parámetro]</strong>
                    <p>Explicación: [Describir su función y relevancia para el sistema. Ejemplo: "Boot Order" para seleccionar la unidad de arranque].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_PARAMETRO_1]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
                <li>
                    <strong>Parámetro 2: [Nombre del Parámetro]</strong>
                    <p>Explicación: [Describir su función y relevancia. Ejemplo: "XMP/DOCP Profile" para la velocidad de la RAM].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_PARAMETRO_2]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
                <li>
                    <strong>Parámetro 3: [Nombre del Parámetro]</strong>
                    <p>Explicación: [Describir su función y relevancia. Ejemplo: "Virtualization Technology" para máquinas virtuales].</p>
                    <p>Fuente: <a href="[ENLACE_WEB_PARAMETRO_3]" target="_blank" style="color: #4CAF50;">[Cita APA y Enlace Web]</a></p>
                </li>
            </ul>
        </section>
        
        <hr>

        <section id="bibliografia">
            <h2>Bibliografía y Referencias (Formato APA 7)</h2>
            <p>Incluir aquí todas las referencias completas que citó a lo largo del documento. **Asegúrese de que cada referencia tenga un enlace web válido para su validación**.</p>
            <ul class="info-list">
                <li>CPUID. (2024). *CPU-Z*. Recuperado el 7 de octubre de 2025, de https://www.cpuid.com/</li>
                <li>MSI. (2020). *Manual de Servicio y Mantenimiento de la Serie MS-16R6*. Recuperado el 7 de octubre de 2025, de https://download-2.msi.com/archive/mnu_exe/nb/MS-16R6_v1.0_Spanish.zip</li>
                <li>Nginx. (2024). *[Título del artículo o documentación de Nginx]*. Recuperado el 7 de octubre de 2025, de [Enlace Web a la documentación o tutorial de Nginx].</li>
                <li>W3Schools. (2024). *HTML Tutorial*. Recuperado el 7 de octubre de 2025, de https://www.w3schools.com/html/default.asp</li>
                <li>Techopedia. (2023). *[Título del artículo sobre BIOS/UEFI]*. Recuperado el 7 de octubre de 2025, de [Enlace Web]</li>
                </ul>
        </section>

    </div>

    <footer>
        <p>Documento Elaborado para [Nombre de la Asignatura]. Servidor: localhost</p>
    </footer>

</body>
</html>