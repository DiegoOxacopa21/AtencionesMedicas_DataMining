# 01_negocio - Entendimiento del Negocio

## Propósito
Documentar los objetivos de negocio, preguntas clave y definición de éxito del proyecto de data mining.

## Contenido esperado
- Definición de objetivos de negocio
- KPIs y métricas de éxito
- Stakeholders identificados
- Restricciones y supuestos

## Archivos relevantes
- `README.md` (este archivo)
- `objetivos.md`
- ` KPIs.md`


------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------

## TEMA:
    falta de recursos en centros hospitalarios

## CONTRASTE CON LA REALIDAD:
    es frecuente las noticias relacionadas a que ciertos hospitales no cuentan con los insumos necesarios

    Enlace a noticias relacionadas:
        - https://www.bing.com/ck/a?!&&p=6fef775028fd607eac071cf51a8bbd160adf6b64a1eebf63670aadac4fe377eaJmltdHM9MTc3NzA3NTIwMA&ptn=3&ver=2&hsh=4&fclid=2efe0ce5-3d39-602b-365e-1a283c2c61fb&psq=falta+de+recursos+en+hospitales&u=a1aHR0cHM6Ly9wZXJ1MjEucGUvcGVydS9ob3NwaXRhbGVzLWRlbC1taW5zYS1lbmZyZW50YW4tY3Jpc2lzLXBvci1mYWx0YS1kZS1yZWN1cnNvcy8
    
        - https://www.bing.com/ck/a?!&&p=6475873fbf071f5f1d37dc6bb4ca0313364170733bbbc8f78a26ef45c55b3db5JmltdHM9MTc3NzA3NTIwMA&ptn=3&ver=2&hsh=4&fclid=2efe0ce5-3d39-602b-365e-1a283c2c61fb&psq=falta+de+recursos+en+hospitales&u=a1aHR0cHM6Ly9sYXJlcHVibGljYS5wZS9zb2NpZWRhZC8yMDI1LzA4LzA3L21hcy1kZWwtNTAtZGUtY2VudHJvcy1kZS1zYWx1ZC1wcmltYXJpb3MtZW4tcGVydS1uby1vcGVyYW4tYmllbi15LWxpbWEtYWNhcGFyYS1sb3MtcmVjdXJzb3MtbWVkaWNvcy1udHBlLTUwODI0Mg

        - https://www.bing.com/ck/a?!&&p=d5cbb720d934d95f114ecc094648cda9f7d4672c8eafccc260b9a3af282a5042JmltdHM9MTc3NzA3NTIwMA&ptn=3&ver=2&hsh=4&fclid=2efe0ce5-3d39-602b-365e-1a283c2c61fb&psq=falta+de+recursos+en+hospitales&u=a1aHR0cHM6Ly93d3cuYW1lcmljYXR2LmNvbS5wZS9ub3RpY2lhcy9hY3R1YWxpZGFkL2NyaXNpcy1zaXN0ZW1hLXNhbHVkLWhvc3BpdGFsZXMtYWwtYm9yZGUtY29sYXBzby1uNTE3NTc0

## OBJETIVO:
    Identificar centros/establecimientos "sobrecargados" de acuerdo a la cantidad de atenciones realizadas, cantidad total de poblacion local y clasificacion de establecimiento

## UTILIDAD:
    Un promedio regular de atenciones en los establecimientos, sirve para poder identificar establecimientos que esten sobrecargados y asi poder tomar medidas

## VARIABLES QUE AFECTAN EL ESTANDAR:
    - cantidad de poblacion local
    - cantidad de atenciones realizadas
    - nivel de establecimiento



ejem: se estima un regular de 5000 atenciones para el hospital de ilo. Esa cantidad variaria si la poblacion fuera mayor... para un hospital de lima se estima un regular de 10 000 atenciones... Ahora la cantidad de atenciones regulares de un establecimiento depende de su nivel/clasificacion... una posta sera 1 000 y para un hospital sera 3 000