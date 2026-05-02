![C:\\Users\\EPIS\\Documents\\upt.png](media/image26.png){width="1.0926727909011373in"
height="1.468837489063867in"}

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto AnzenCore**

Curso: [Calidad y Pruebas de Software]{.mark}

Docente: Patrick Jose Cuadros Quiroga

Integrantes:

***Arocutipa Arocutipa, Gian Franco (2023076790)***

***Perez Peralta, Fabrizio Salvador Elias (2023077476)***

**Tacna -- Perú**

***2026***

+--------------------------------------------------------------------------------------------+
| CONTROL DE VERSIONES                                                                       |
+-------------+-------------+-------------+-------------+-------------+----------------------+
| Versión     | Hecha por   | Revisada    | Aprobada    | Fecha       | Motivo               |
|             |             | por         | por         |             |                      |
+-------------+-------------+-------------+-------------+-------------+----------------------+
| 1.0         | G.A. / F.P. |             |             | 27/04/2026  | Versión Original     |
+=============+=============+=============+=============+=============+======================+

AnzenCore

Documento de Especificación de Requerimientos de Software

Versión *{1.0}*

+--------------------------------------------------------------------------------------------+
| CONTROL DE VERSIONES                                                                       |
+-------------+-------------+-------------+-------------+-------------+----------------------+
| Versión     | Hecha por   | Revisada    | Aprobada    | Fecha       | Motivo               |
|             |             | por         | por         |             |                      |
+-------------+-------------+-------------+-------------+-------------+----------------------+
| 1.0         | G.A. / F.P. |             |             | 27/04/2026  | Versión Original     |
+=============+=============+=============+=============+=============+======================+

**ÍNDICE GENERAL**

[INTRODUCCIÓN 5](#introducción)

[I. Generalidades de la empresa 5](#generalidades-de-la-empresa)

> [A. Nombre de la empresa 5](#nombre-de-la-empresa)
>
> [B. Visión 5](#visión)
>
> [C. Misión 5](#misión)
>
> [D. Organigrama 5](#organigrama)

[II. Visionamiento de la empresa 6](#visionamiento-de-la-empresa)

> [A. Descripción de la empresa 6](#descripción-de-la-empresa)
>
> [B. Objetivos de negocios 6](#objetivos-de-negocios)
>
> [C. Objetivos de diseño 6](#objetivos-de-diseño)
>
> [D. Alcance del proyecto 7](#alcance-del-proyecto)
>
> [E. Viabilidad del sistema 7](#viabilidad-del-sistema)

[III. Especificación de Requerimientos de Software
8](#especificación-de-requerimientos-de-software)

> [A. Cuadro de Requerimientos funcionales Inicial
> 8](#cuadro-de-requerimientos-funcionales-inicial)
>
> [B. Cuadro de Requerimientos No funcionales
> 9](#cuadro-de-requerimientos-no-funcionales)
>
> [C. Cuadro de Requerimientos funcionales Final
> 10](#cuadro-de-requerimientos-funcionales-final)
>
> [D. Reglas de Negocio 12](#reglas-de-negocio)

[IV. Fase de Desarrollo 13](#fase-de-desarrollo)

> [A. Perfiles de Usuario 13](#perfiles-de-usuario)
>
> [Administrador 13](#_r2g8nyic79j1)
>
> [Vecino 14](#_bjokxoe3m1kd)
>
> [B. Modelo Conceptual 15](#modelo-conceptual)
>
> [a. Diagrama de Paquetes 15](#diagrama-de-paquetes)
>
> [b. Diagrama de Casos de Uso 17](#diagrama-de-casos-de-uso)
>
> [c. Escenarios Casos de Uso 17](#escenarios-casos-de-uso)
>
> [C. Modelo Lógico 29](#modelo-lógico)
>
> [a. Análisis de Objetos 29](#análisis-de-objetos)
>
> [b. Diagrama de Actividades con objetos
> 31](#diagrama-de-actividades-con-objetos)
>
> [c. Diagrama de Secuencia 41](#diagrama-de-secuencia)
>
> [d. Diagrama de Clases 45](#diagrama-de-clases)

[CONCLUSIONES 47](#conclusiones)

[RECOMENDACIONES 47](#recomendaciones)

[BIBLIOGRAFÍA 47](#bibliografía)

# **INTRODUCCIÓN**

El presente documento describe la Especificación de Requerimientos de
Software (ERS) para el sistema AnzenCore, una plataforma web con
componente móvil (APK) orientada a la auditoría de seguridad de
dispositivos Android y a la educación del usuario en ciberseguridad.

AnzenCore propone un modelo innovador: una APK de uso temporal que
analiza el dispositivo del usuario, envía un reporte cifrado a una
plataforma web, y desaparece sin quedar en segundo plano. El usuario
administra su historial de seguridad, sigue un ranking gamificado y
completa micro-lecciones interactivas para corregir vulnerabilidades
detectadas.

El sistema se desarrollará con arquitectura MVC, utilizando PHP en el
backend web y Kotlin para la aplicación Android.

 

# **[Generalidades de la empresa]{.underline}**

## Nombre de la empresa

AnzenCore --- Plataforma de Auditoría de Seguridad Móvil

## Visión

Ser la plataforma de referencia en educación y concienciación sobre
ciberseguridad móvil en Latinoamérica, convirtiendo la auditoría de
dispositivos en una experiencia educativa, accesible y gamificada para
cualquier tipo de usuario.

## Misión

Proveer a los usuarios de Android una herramienta de análisis de
seguridad no invasiva, educativa e interactiva, que les permita
identificar, comprender y corregir vulnerabilidades en sus dispositivos,
sin sacrificar privacidad ni requerir instalación permanente.

## Organigrama

Ejemplo:

![](media/image6.png){width="6.854043088363954in"
height="1.510213254593176in"}

# **[Visionamiento de la empresa]{.underline}**

## Descripción de la empresa

Los usuarios de dispositivos Android desconocen los riesgos de seguridad
presentes en sus propios dispositivos: aplicaciones con permisos
excesivos, sistemas operativos desactualizados, depuración USB activa,
certificados no confiables, entre otros. Las herramientas actuales
exigen instalación permanente, generan informes técnicos difíciles de
interpretar y no motivan al usuario a corregir las vulnerabilidades
encontradas.

## Objetivos de negocios

  **N°**   **Objetivo**                                                        **Indicador de Éxito**
  -------- ------------------------------------------------------------------- ------------------------------------------------------
  1        Ofrecer auditoría de seguridad Android sin instalación permanente   APK temporal funcional con desinstalación automática
  2        Educar al usuario sobre ciberseguridad de forma gamificada          Tasa de completado de micro-lecciones \> 60%
  3        Generar historial de seguridad trazable por usuario                 Dashboard web con gráfico de evolución de puntuación
  4        Fomentar comunidad de seguridad mediante ranking                    Ranking semanal activo con al menos 10 usuarios

> 

## Objetivos de diseño

  **N°**   **Objetivo de Diseño**
  -------- -------------------------------------------------------------------------------
  1        Arquitectura MVC en PHP para el backend web con separación clara de capas
  2        APK en Kotlin con permisos mínimos, análisis local y envío cifrado de reporte
  3        Dashboard web responsivo accesible desde cualquier navegador sin instalación
  4        Sistema de puntuación gamificada con puzzle visual de vulnerabilidades
  5        Privacidad total: no se almacenan contactos, mensajes ni fotos del usuario

> 

## Alcance del proyecto

El sistema AnzenCore comprende los siguientes módulos:

  **Módulo**             **Descripción**                                                  **Tecnología**
  ---------------------- ---------------------------------------------------------------- ------------------
  Plataforma Web (MVC)   Registro, dashboard, ranking, historial de análisis              PHP + MySQL
  APK de Análisis        Escaneo del dispositivo Android, generación de reporte cifrado   Kotlin (Android)
  Módulo Educativo       Micro-lecciones y puzzle de vulnerabilidades                     PHP + JS
  API REST               Comunicación entre APK y plataforma web                          PHP REST API
  Sistema de Ranking     Puntuación de seguridad, ranking semanal/global                  PHP + MySQL

> 

## Viabilidad del sistema

El sistema propuesto es viable técnica, económica y operativamente:

- **Técnicamente,** el equipo cuenta con conocimientos de PHP, MySQL,
  Kotlin y arquitectura MVC. Las tecnologías son de código abierto y no
  generan costos de licencia.

- **Económicamente,** el proyecto se desarrolla en entorno académico.
  Costos limitados a hosting compartido y dominio para despliegue de
  pruebas.

- **Operativamente,** el sistema es accesible desde cualquier navegador
  web. La APK se distribuye desde la plataforma web como descarga
  directa.

> 

## Información obtenida del Levantamiento de Información

  **Técnica**                **Fuente**                    **Hallazgo Principal**
  -------------------------- ----------------------------- --------------------------------------------------------------------------------------
  Revisión de literatura     OWASP Mobile Top 10           Permisos excesivos y almacenamiento inseguro son las amenazas más comunes en Android
  Análisis de competidores   Apps Play Store (antivirus)   Requieren instalación permanente y no ofrecen educación gamificada
  Encuesta informal          Estudiantes universitarios    85% desconoce qué permisos tienen sus apps instaladas
  Análisis de sistema        Android Developer Docs        API de Android permite acceso a metadatos de seguridad sin datos personales

# **[Análisis de Procesos]{.underline}**

## Diagrama del Proceso Actual - Diagrama de actividades

![](media/image34.png){width="2.8958333333333335in"
height="4.515625546806649in"}

![](media/image14.png){width="4.055733814523185in"
height="6.500134514435696in"}

## Diagrama del Proceso Propuesto - Diagrama de actividades Inicial

![](media/image33.png){width="2.3376891951006122in"
height="5.505208880139983in"}

![](media/image29.png){width="2.9367804024496937in"
height="3.807292213473316in"}

![](media/image38.png){width="2.6081036745406823in"
height="5.057292213473316in"}

# **[Especificación de Requerimientos de Software]{.underline}**

## Cuadro de Requerimientos funcionales Inicial

  -----------------------------------------------------------------------------
  **ID**   **Módulo**      **Requerimiento Funcional**          **Prioridad**
  -------- --------------- ------------------------------------ ---------------
  RF-01    Autenticación   El sistema debe permitir registro de Alta
                           usuarios con email y contraseña      

  RF-02    Autenticación   El sistema debe permitir inicio y    Alta
                           cierre de sesión seguro              

  RF-03    APK             El sistema debe generar una APK con  Alta
                           session_id único por usuario         

  RF-04    APK             La APK debe analizar versión de SO,  Alta
                           apps instaladas y permisos           

  RF-05    APK             La APK debe enviar reporte cifrado   Alta
                           vía HTTPS a la API REST              

  RF-06    Dashboard       El sistema debe mostrar puntuación   Alta
                           de seguridad (0-100)                 

  RF-07    Dashboard       El sistema debe listar               Alta
                           vulnerabilidades clasificadas por    
                           criticidad                           

  RF-08    Educativo       El sistema debe mostrar              Media
                           micro-lecciones por cada             
                           vulnerabilidad                       

  RF-09    Educativo       El usuario debe poder marcar         Media
                           vulnerabilidades como corregidas     

  RF-10    Ranking         El sistema debe calcular y mostrar   Media
                           ranking semanal y global             

  RF-11    Historial       El sistema debe almacenar historial  Alta
                           de análisis por usuario              

  RF-12    Dashboard       El sistema debe mostrar gráfico de   Media
                           evolución de puntuación              
  -----------------------------------------------------------------------------

## 

## Cuadro de Requerimientos No funcionales

  **ID**   **Categoría**    **Requerimiento No Funcional**
  -------- ---------------- -------------------------------------------------------------------------
  RNF-01   Seguridad        Todos los reportes de análisis deben transmitirse cifrados con TLS 1.2+
  RNF-02   Privacidad       La APK no debe leer, acceder ni almacenar contactos, mensajes o fotos
  RNF-03   Rendimiento      El análisis del dispositivo debe completarse en menos de 60 segundos
  RNF-04   Disponibilidad   La plataforma web debe estar disponible el 99% del tiempo (24/7)
  RNF-05   Usabilidad       El dashboard debe ser responsivo y usable en pantallas desde 320px
  RNF-06   Compatibilidad   La APK debe ser compatible con Android 8.0 (API 26) o superior
  RNF-07   Mantenibilidad   El backend debe seguir estrictamente el patrón MVC con PHP
  RNF-08   Escalabilidad    La arquitectura debe soportar hasta 10,000 usuarios concurrentes
  RNF-09   Portabilidad     La plataforma web debe funcionar en Chrome, Firefox, Safari y Edge

## Cuadro de Requerimientos funcionales Final

  ------------------------------------------------------------------------------
  **ID**   **Caso de  **Actor**   **Descripción Refinada**          **Prior.**
           Uso**                                                    
  -------- ---------- ----------- --------------------------------- ------------
  RF-01    CU-01      Usuario     Registrarse con email, contraseña Alta
                                  y nombre. Validar email único.    

  RF-02    CU-02      Usuario     Iniciar sesión con credenciales.  Alta
                                  Generar token de sesión.          

  RF-03    CU-03      Sistema     Generar APK con session_id        Alta
                                  SHA-256 único por descarga.       

  RF-04    CU-04      APK         Analizar: versión SO,             Alta
                      (Sistema)   apps+permisos, USB debug,         
                                  orígenes desconocidos, certs      
                                  raíz.                             

  RF-05    CU-05      APK         Cifrar reporte con AES-256 y      Alta
                      (Sistema)   enviarlo a endpoint /api/report.  

  RF-06    CU-06      Sistema     Procesar reporte, calcular score  Alta
                                  (0-100) y persistir en BD.        

  RF-07    CU-07      Usuario     Ver dashboard con score, lista de Alta
                                  vulnerabilidades y estado del     
                                  puzzle.                           

  RF-08    CU-08      Usuario     Ver y completar micro-lección de  Media
                                  cada vulnerabilidad.              

  RF-09    CU-09      Usuario     Marcar vulnerabilidad corregida;  Media
                                  sistema actualiza score.          

  RF-10    CU-10      Sistema     Recalcular ranking semanal/global Media
                                  cada 24 horas.                    

  RF-11    CU-11      Usuario     Ver historial de análisis con     Alta
                                  gráfico de evolución.             

  RF-12    CU-12      Usuario     Descargar nueva APK para          Media
                                  reanálisis tras correcciones.     
  ------------------------------------------------------------------------------

> 

## Reglas de Negocio

  **ID**   **Regla de Negocio**    **Descripción**
  -------- ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  RN-01    APK Efímera             Cada sesión de análisis genera una APK única. No se reutilizan APKs entre sesiones o usuarios.
  RN-02    Privacidad Total        La APK únicamente lee metadatos de seguridad del sistema. Está prohibido acceder a contactos, fotos, mensajes o cualquier dato personal.
  RN-03    Cálculo de Score        Score = 100 - (Σ peso_criticidad_vulnerabilidad). Crítica=20pts, Media=10pts, Leve=5pts.
  RN-04    Ranking                 Ranking = (Score × factor_tiempo) - (vulnerabilidades_repetidas × 5). Se recalcula cada 24h.
  RN-05    Corrección Verificada   Solo se acepta corrección de vulnerabilidad si el usuario completa la micro-lección y realiza la acción en el dispositivo.
  RN-06    Sesión de Análisis      Una sesión de análisis es válida por 24 horas. Después debe generarse una nueva APK.
  RN-07    Historial               Se conservan todos los análisis históricos. No se eliminan aunque el usuario corrija vulnerabilidades.

# **[Fase de Desarrollo]{.underline}**

## Perfiles de Usuario

  **Perfil**                 **Descripción**                                                                                                                            **Acceso**
  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------
  Usuario Final (Novato)     Usuario sin conocimientos técnicos que desea saber si su móvil es seguro. Interactúa principalmente con el puzzle y las micro-lecciones.   Dashboard, puzzle, ranking
  Usuario Final (Avanzado)   Usuario con conocimientos de seguridad que usa AnzenCore como herramienta de auditoría rápida y sigue su historial.                        Dashboard, historial, API, reanálisis
  Administrador              Gestiona usuarios, visualiza estadísticas globales y actualiza la base de firmas de apps sospechosas.                                      Panel admin, gestión usuarios, estadísticas

## Modelo Conceptual

### Diagrama de Paquetes

![](media/image16.png){width="5.53668416447944in"
height="4.212694663167104in"}

![](media/image27.png){width="6.267716535433071in" height="3.25in"}

![](media/image18.png){width="4.197916666666667in"
height="3.3020833333333335in"}

### Diagrama de Casos de Uso

![](media/image35.png){width="3.3422987751531057in"
height="5.19692804024497in"}

![](media/image20.png){width="3.6973009623797024in"
height="5.338542213473316in"}

### Escenarios Casos de Uso

**CU-01: Registrarse**

  **Campo**           **Descripción**
  ------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ID                  CU-01
  Nombre              Registrarse
  Actor Principal     Usuario
  Precondición        El usuario no tiene cuenta registrada
  Flujo Principal     1\. Usuario accede a /register 2. Ingresa nombre, email y contraseña 3. Sistema valida que el email no exista 4. Sistema crea cuenta y envía email de confirmación 5. Usuario accede al dashboard
  Flujo Alternativo   3a. Email ya existe: sistema muestra error y solicita otro email
  Postcondición       Usuario registrado y sesión iniciada
  Prioridad           Alta

**CU-03: Descargar APK Personalizada**

  **Campo**               **Descripción**
  ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **ID**                  **CU-03**
  **Nombre**              **Descargar APK Personalizada**
  **Actor Principal**     **Usuario**
  **Precondición**        **Usuario autenticado en la plataforma web**
  **Flujo Principal**     **1. Usuario presiona \'Analizar mi dispositivo\' 2. Sistema genera session_id SHA-256 único 3. Sistema embebe session_id en APK base 4. Sistema registra solicitud de análisis pendiente 5. Se descarga la APK al dispositivo del usuario**
  **Flujo Alternativo**   **2a. Error de generación: sistema reintenta una vez y notifica**
  **Postcondición**       **APK descargada con session_id vinculado al usuario**
  **Prioridad**           **Alta**

**CU-04 / CU-05: Analizar Dispositivo y Enviar Reporte (APK)**

  **Campo**               **Descripción**
  ----------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **ID**                  **CU-04/05**
  **Nombre**              **Analizar Dispositivo y Enviar Reporte**
  **Actor Principal**     **APK Android (Sistema)**
  **Precondición**        **APK instalada en dispositivo Android 8.0+**
  **Flujo Principal**     **1. APK solicita permisos mínimos al usuario 2. OSAnalyzer lee versión SO y parche de seguridad 3. PermissionAnalyzer lista apps con permisos peligrosos 4. AppAnalyzer detecta apps de orígenes desconocidos 5. CertAnalyzer verifica certificados raíz no confiables 6. ReportBuilder construye JSON de vulnerabilidades 7. NetworkClient cifra con AES-256 y envía a /api/report 8. API confirma recepción con HTTP 200 9. APK notifica al usuario: \'Análisis completado. Puedes desinstalar.\'**
  **Flujo Alternativo**   **8a. Sin conectividad: APK guarda reporte cifrado localmente y reintenta**
  **Postcondición**       **Reporte persistido en BD y puntuación calculada**
  **Prioridad**           **Alta**

**CU-07: Ver Dashboard**

  **Campo**               **Descripción**
  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **ID**                  **CU-07**
  **Nombre**              **Ver Dashboard de Seguridad**
  **Actor Principal**     **Usuario**
  **Precondición**        **Usuario autenticado con al menos un análisis realizado**
  **Flujo Principal**     **1. Usuario accede a /dashboard 2. Sistema recupera último reporte del usuario 3. Muestra indicador de salud (verde/ámbar/rojo) y score 4. Lista vulnerabilidades ordenadas por criticidad 5. Muestra puzzle con piezas pendientes y completadas 6. Muestra gráfico de evolución histórica**
  **Flujo Alternativo**   **2a. Sin análisis previo: sistema muestra botón \'Realizar primer análisis\'**
  **Postcondición**       **Usuario visualiza su estado actual de seguridad**
  **Prioridad**           **Alta**

## Modelo Lógico

### Análisis de Objetos

  **Clase**           **Atributos Principales**                                                        **Métodos Principales**
  ------------------- -------------------------------------------------------------------------------- ---------------------------------------------------
  **User**            **id, nombre, email, password_hash, created_at, score_actual**                   **register(), login(), getHistory(), getScore()**
  **Report**          **id, user_id, session_id, score, fecha_analisis, dispositivo_info**             **create(), getByUser(), calculateScore()**
  **Vulnerability**   **id, report_id, tipo, criticidad, descripcion, estado, lesson_id**              **list(), markFixed(), getByCriticality()**
  **Lesson**          **id, vulnerability_tipo, titulo, contenido, pasos_correccion**                  **getByType(), markCompleted()**
  **Ranking**         **id, user_id, periodo, score_promedio, posicion, vulnerabilidades_repetidas**   **calculate(), getTopN(), getUserPosition()**
  **APKSession**      **session_id, user_id, fecha_generacion, expiracion, estado**                    **generate(), validate(), expire()**

### Diagrama de Actividades con objetos

> **CU-01: Registrarse**

![](media/image7.png){width="4.498441601049869in"
height="6.795745844269466in"}

> **CU-02: Iniciar Sesión**

![](media/image19.png){width="3.9166666666666665in"
height="7.927083333333333in"}

![](media/image24.png){width="5.270833333333333in" height="4.96875in"}

> **CU-03: Descargar APK Personalizada**

![](media/image32.png){width="3.9270833333333335in"
height="8.145833333333334in"}

![](media/image9.png){width="6.114583333333333in"
height="8.364583333333334in"}

> **CU-04/05: Analizar Dispositivo y Enviar Reporte (APK Kotlin)**

![](media/image40.png){width="4.635416666666667in"
height="8.260416666666666in"}

![](media/image10.png){width="3.125in" height="8.333333333333334in"}

![](media/image1.png){width="2.4479166666666665in" height="8.5in"}

> **CU-06: Procesar Reporte y Calcular Score**

![](media/image2.png){width="3.4895833333333335in"
height="6.713542213473316in"}

![](media/image12.png){width="4.239583333333333in" height="6.40625in"}

![](media/image21.png){width="4.34375in" height="8.375in"}

> **CU-07: Ver Dashboard**

![](media/image28.png){width="4.895833333333333in"
height="8.322916666666666in"}

> **CU-08: Ver Micro-Lección**

![](media/image42.png){width="5.916666666666667in"
height="8.239583333333334in"}

> **CU-09: Marcar Vulnerabilidad Corregida**

![](media/image25.png){width="4.685444006999125in"
height="7.838542213473316in"}

> **CU-10: Recalcular Ranking**

![](media/image15.png){width="4.822916666666667in"
height="8.385416666666666in"}

> **CU-11: Ver Historial de Análisis**
>
> ![](media/image37.png){width="4.572916666666667in"
> height="8.333333333333334in"}
>
> **CU-12: Solicitar Reanálisis**
>
> ![](media/image23.png){width="4.52442147856518in"
> height="6.296875546806649in"}

### Diagrama de Secuencia 

> **DS-CU01: Registrarse**

![](media/image41.png){width="6.267716535433071in"
height="4.930555555555555in"}

> **DS-CU02: Iniciar Sesión**

![](media/image3.png){width="6.267716535433071in"
height="4.666666666666667in"}

> **DS-CU03: Descargar APK Personalizada**

![](media/image11.png){width="6.267716535433071in"
height="3.5555555555555554in"}

> **DS-CU04/05: Analizar Dispositivo y Enviar Reporte**

![](media/image22.png){width="7.854166666666667in"
height="4.020608048993876in"}

> **DS-CU06: Procesar Reporte y Calcular Score**

![](media/image8.png){width="6.267716535433071in"
height="6.152777777777778in"}

> **DS-CU07: Ver Dashboard**

![](media/image36.png){width="7.734375546806649in"
height="5.698430664916885in"}

> **DS-CU08: Ver Micro-Lección**

![](media/image39.png){width="7.136975065616798in"
height="4.161259842519685in"}

> **DS-CU09: Marcar Vulnerabilidad Corregida**

![](media/image17.png){width="7.124876421697288in"
height="5.247840113735783in"}

> **DS-CU10: Recalcular Ranking**

![](media/image13.png){width="7.218626421697288in"
height="4.26000656167979in"}

### Diagrama de Clases

[[Diagrama de
clases]{.underline}](https://mermaid.ai/d/7b3ac038-38cb-4498-a510-8404ffb50728)

![](media/image31.png){width="6.276042213473316in"
height="2.5437773403324586in"}

![](media/image4.png){width="7.594187445319335in"
height="2.827736220472441in"}

![](media/image30.png){width="6.910205599300087in"
height="3.369792213473316in"}

![](media/image5.png){width="2.6213484251968504in"
height="5.3975010936132986in"}

# **CONCLUSIONES**

- AnzenCore propone un enfoque innovador para la seguridad móvil: una
  APK temporal que analiza el dispositivo sin instalación permanente,
  complementada por una plataforma web educativa y gamificada.

- La arquitectura MVC en PHP garantiza separación de responsabilidades,
  facilitando el mantenimiento y las pruebas de software, lo cual es
  fundamental para el curso de Calidad y Pruebas de Software.

- El uso de Kotlin para la APK Android asegura compatibilidad con las
  últimas versiones del sistema operativo y acceso a las APIs de
  seguridad más modernas, con código más seguro y conciso que Java.

- La gamificación mediante el puzzle de vulnerabilidades y el sistema de
  ranking aborda el principal problema identificado: la falta de
  motivación del usuario para corregir problemas de seguridad.

- La privacidad by design, al no acceder a datos personales, diferencia
  a AnzenCore de las soluciones tradicionales y facilita su adopción.

# **RECOMENDACIONES**

- Implementar pruebas unitarias y de integración desde el inicio del
  desarrollo (TDD) para garantizar la calidad del sistema, especialmente
  en los módulos de cálculo de score y procesamiento de reportes.

- Realizar pruebas de penetración (pentesting) sobre la API REST para
  verificar la seguridad del endpoint de recepción de reportes antes del
  despliegue.

- Documentar los casos de prueba según el estándar IEEE 829, alineados
  con los requerimientos funcionales definidos en este documento.

- Considerar en iteraciones futuras la integración con bases de datos de
  vulnerabilidades CVE para enriquecer el análisis de apps instaladas.

- Evaluar la publicación en F-Droid (repositorio de apps Android de
  código abierto) para aumentar el alcance del proyecto.

# **BIBLIOGRAFÍA**

- Google LLC. (2024). Android Developer Documentation --- Security best
  practices.
  https://developer.android.com/privacy-and-security/security-tips

- C4 Model (2024). The C4 model for visualizing software architecture.
  Recuperado de:
  [[https://c4model.com/]{.underline}](https://c4model.com/)
