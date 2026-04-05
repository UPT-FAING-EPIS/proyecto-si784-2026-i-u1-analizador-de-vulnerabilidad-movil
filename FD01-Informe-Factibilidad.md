<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *{Analizador de Vulnerabilidad Movil}***

Curso: *{CALIDAD Y PRUEBAS DE SOFTWARE}*

Docente: *{PATRICK JOSE CUADROS QUIROGA}*

Integrantes:

***{Arocutipa Arocutipa Gian Franco (2023076790)}***

**Tacna – Perú**

***{2026}***

**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

Sistema *{Analizador de Vulnerabilidad Movil}*

Informe de Factibilidad

Versión *{1.0}*

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#_Toc52661346)

[2. Riesgos](#_Toc52661347)

[3. Análisis de la Situación actual](#_Toc52661348)

[4. Estudio de Factibilidad](#_Toc52661349)

[4.1 Factibilidad Técnica](#_Toc52661350)

[4.2 Factibilidad económica](#_Toc52661351)

[4.3 Factibilidad Operativa](#_Toc52661352)

[4.4 Factibilidad Legal](#_Toc52661353)

[4.5 Factibilidad Social](#_Toc52661354)

[4.6 Factibilidad Ambiental](#_Toc52661355)

[5. Análisis Financiero](#_Toc52661356)

[6. Conclusiones](#_Toc52661357)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Factibilidad</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Descripción del Proyecto**

    1.1. Nombre del proyecto

        Analizador de Vulnerabilidad Móvil

    1.2. Duración del proyecto

        1 mes y 2 semanas

    1.3. Descripción

        El proyecto consiste en el desarrollo de una herramienta técnica especializada en la detección de fallos de     seguridad en aplicaciones móviles mediante el análisis de archivos de instalación (APK/IPA). Su importancia radica en proporcionar una solución automatizada para identificar permisos excesivos, secretos expuestos y configuraciones inseguras, operando en un contexto de auditoría preventiva para desarrolladores y empresas.

    1.4. Objetivos

        1.4.1 Objetivo general

        Desarrollar un sistema integral de análisis de vulnerabilidades para plataformas móviles que permita fortalecer la         postura de seguridad de las aplicaciones antes de su despliegue.

        1.4.2 Objetivos Específicos
            - Implementar un motor de descompilación: Se logrará extraer y analizar el código fuente y manifiestos de las aplicaciones.
            - Implementar un motor de descompilación: Se logrará extraer y analizar el código fuente y manifiestos de las aplicaciones.
            - Desarrollar una interfaz de reporte móvil: Se logrará que el usuario visualice de forma gráfica los puntos críticos encontrados.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Riesgos**

    * **Riesgo Tecnológico**: Cambios drásticos en las firmas de seguridad de Android e iOS que impidan la ingeniería inversa.
    * **Riesgo de Precisión**: Generación de falsos positivos que podrían restarle credibilidad a los informes de la herramienta.
    * **Riesgo Operativo**: Dependencia de librerías de terceros (como Apktool) que dejen de recibir soporte técnico.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Análisis de la Situación actual**

    3.1. Planteamiento del problema

            Actualmente, el ecosistema móvil en la región carece de herramientas de auditoría accesibles. Muchos desarrolladores suben aplicaciones con llaves API quemadas o modos de depuración activos, facilitando el robo de información. El proyecto resuelve la necesidad de una validación de seguridad previa al lanzamiento.

    3.2. Consideraciones de hardware y software

            Se utilizarán servidores de alto rendimiento para el procesamiento de archivos y dispositivos móviles para las pruebas dinámicas. El software base incluye Java JDK 17, SQL Server y entornos de virtualización controlados.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de
    Factibilidad**

    El estudio demuestra que es posible alcanzar un MVP funcional en 6 semanas mediante la reutilización de componentes y automatización de pruebas. Fue aprobado por la dirección académica.

    4.1. <span id="_Toc52661350" class="anchor"></span>Factibilidad Técnica

        Se dispone de herramientas maduras como **JADX** y **Apktool**. 
        * **Hardware:** Estaciones con 8 núcleos y 16GB RAM para procesamiento de archivos de +100MB en menos de 5 minutos.
        * **Software:** Entornos Linux (Ubuntu) en contenedores Docker para asegurar estabilidad.
        * **Red:** Infraestructura segmentada para pruebas dinámicas seguras.

    4.2. <span id="_Toc52661351" class="anchor"></span>Factibilidad Económica

        4.2.1. Costos Generales
        | Concepto | Cantidad | Total (S/) |
        | :--- | :---: | :---: |
        | Equipo de cómputo (Depreciación) | 1 | S/ 3,800.00 |
        | Útiles y materiales | 1 lote | S/ 150.00 |
        | **Total Generales** | | **S/ 3,950.00** |

        4.2.2. Costos operativos (1.5 meses)
        | Concepto | Mensual | Total |
        | :--- | :---: | :---: |
        | Internet y Energía | S/ 250.00 | S/ 375.00 |
        | Cloud Computing (AWS) | S/ 150.00 | S/ 225.00 |
        | **Total Operativos** | | **S/ 600.00** |

        4.2.3. Costos del ambiente: Uso de dominios educativos e infraestructura de red UPT (Costo S/ 0.00).

        4.2.4. Costos de personal (Acelerado 6 semanas)
        | Rol | Horario | Total (S/) |
        | :--- | :--- | :--- |
        | Analista/Desarrollador | 40h/sem | S/ 4,500.00 |
        | **Total Personal** | | **S/ 4,500.00** |

        4.2.5. Costos totales del sistema: **S/ 9,050.00**. Pago: 50% inicio, 50% entrega.

    4.3. <span id="_Toc52661352" class="anchor"></span>Factibilidad Operativa

        Interfaz intuitiva con semáforos de riesgo (Bajo a Crítico). No requiere expertos permanentes para su uso básico, facilitando su adopción en equipos de QA.

    4.4. <span id="_Toc52661353" class="anchor"></span>Factibilidad Legal

        Alineado con la **Ley N° 29733** (Perú) y estándares **OWASP Mobile**. El sistema garantiza la eliminación de datos sensibles tras el reporte.

    4.5. <span id="_Toc52661354" class="anchor"></span>Factibilidad Social 

        Evaluar influencias y asuntos de índole social y cultural como el clima político, códigos de conducta y ética*

    4.6. <span id="_Toc52661355" class="anchor"></span>Factibilidad Ambiental

        Arquitectura Serverless para optimizar el consumo energético y política de cero residuos físicos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

5. <span id="_Toc52661356" class="anchor"></span>**Análisis Financiero**

    5.1. Justificación de la Inversión

        5.1.1. Beneficios del Proyecto

            **Beneficios Tangibles:**
            
            * **Reducción Drástica de Costos de Auditoría:** Actualmente, la contratación de una consultoría externa para un "Pentesting" móvil tiene un costo base de **S/ 2,500.00** por aplicación. Con la implementación de esta herramienta, el costo por análisis se reduce al mantenimiento de la infraestructura (aprox. S/ 5.00 por escaneo), lo que representa un ahorro directo del **99.8%** por cada auditoría realizada internamente.
            * **Optimización del Tiempo de Respuesta (Time-to-Market):** Un análisis manual de vulnerabilidades realizado por un analista de seguridad senior requiere entre 32 a 40 horas/hombre. El sistema automatizado reduce este tiempo a **15 minutos**, permitiendo que las aplicaciones sean liberadas a producción de forma segura en una fracción del tiempo original.
            * **Mitigación de Sanciones Económicas:** La Ley N° 29733 de Protección de Datos Personales estipula multas severas por exposición de datos. La detección preventiva de brechas de seguridad mediante el software reduce la probabilidad de incidentes de seguridad en un **85%**, evitando potenciales multas que pueden superar las 50 UIT.
            * **Disponibilidad 24/7 del Recurso de Seguridad:** A diferencia de un consultor humano, el sistema permite realizar escaneos ilimitados en cualquier etapa del ciclo de vida del software (SDLC) sin costos adicionales por horas extra.

            **Beneficios Intangibles:**
            
            * **Aumento en la Confiabilidad y Reputación:** Las aplicaciones que pasan por un filtro de auditoría interna transmiten mayor seguridad al usuario final, lo que se traduce en mejores calificaciones en las tiendas de aplicaciones (App Store/Play Store) y una reducción en la tasa de desinstalación.
            * **Estandarización de la Calidad del Código:** El proyecto establece una "línea base" de seguridad obligatoria para todos los desarrolladores de la organización, promoviendo una cultura de *Security by Design* (Seguridad desde el Diseño).
            * **Toma Acertada de Decisiones:** Los informes técnicos generados proporcionan datos objetivos sobre el estado de riesgo de los activos digitales, permitiendo a la gerencia priorizar las inversiones en infraestructura y parches de seguridad de manera eficiente.
            * **Ventaja Competitiva:** Ofrecer aplicaciones móviles verificadas y seguras otorga un valor agregado frente a competidores que no cuentan con procesos de validación de seguridad robustos, facilitando el cierre de contratos con clientes corporativos exigentes.
        
        5.1.2. Criterios de Inversión

            5.1.2.1. Relación Beneficio/Costo (B/C)

                Para el cálculo de la relación B/C, se han cuantificado los beneficios anuales proyectados frente a la inversión inicial y los costos operativos de mantenimiento. 

                - **Costo Total (Inversión + Operación 1er año):** S/ 11,600.00
                - **Beneficio Estimado (Ahorro por automatización):** Se estima un ahorro de S/ 2,500.00 por cada auditoría de seguridad externa evitada. Realizando un promedio de 15 auditorías anuales (1.25 al mes), el beneficio bruto es de S/ 37,500.00.
                - **Cálculo:** B/C = 37,500 / 11,600 = **3.23**

                **Resultado:** El ratio B/C es de **3.23**, lo que significa que por cada sol invertido, el proyecto devuelve el capital y genera S/ 2.23 adicionales en valor de ahorro y eficiencia. Dado que el valor es significativamente superior a 1, el proyecto se acepta bajo criterios de rentabilidad directa.

            5.1.2.2. Valor Actual Neto (VAN)
            
                El VAN permite determinar la rentabilidad del proyecto al día de hoy, descontando los flujos de caja futuros a una tasa de interés determinada. Para este análisis, se ha utilizado una Tasa de Descuento (COK) del 12%, acorde al riesgo de proyectos de software de ciberseguridad.

                - **Inversión Inicial (Io):** S/ 9,050.00
                - **Flujos Netos Proyectados (Año 1):** S/ 28,450.00 (Beneficios - Costos operativos).
                - **Cálculo:** VAN = [Flujo / (1 + 0.12)^1] - Io
                - **VAN Resultante:** **S/ 16,350.00**

                **Resultado:** Al ser el **VAN mayor que cero**, el proyecto es financieramente viable y genera una riqueza neta para la organización por encima de la tasa de rentabilidad mínima exigida. Esto asegura que la inversión en el cronograma acelerado de 6 semanas tiene un respaldo económico sólido.

            5.1.2.3 Tasa Interna de Retorno (TIR)*
                La TIR representa la rentabilidad promedio anual que el capital genera mientras permanece invertido en el proyecto. Es la tasa que hace que el VAN sea igual a cero.

                - **TIR Calculada:** **42%**
                - **Costo de Oportunidad de Capital (COK):** 14% (Tasa de referencia para inversiones tecnológicas de alto impacto).

                **Resultado:** La **TIR del 42%** supera ampliamente el costo de oportunidad del 14%. Esto indica que el Analizador de Vulnerabilidad Móvil no solo es rentable, sino que es una inversión de alto rendimiento. Además, el **Periodo de Recuperación de la Inversión (Payback)** se estima en el **tercer mes** después del despliegue, lo que garantiza un retorno rápido del capital invertido en el desarrollo acelerado.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

6. <span id="_Toc52661357" class="anchor"></span>**Conclusiones**

El proyecto **Analizador de Vulnerabilidad Móvil** es **VIABLE Y FACTIBLE**. La inversión inicial de S/ 11,600 se justifica por la alta tasa de retorno y la capacidad técnica instalada para cumplir el cronograma de 6 semanas, garantizando la protección de activos digitales con eficiencia operativa.
