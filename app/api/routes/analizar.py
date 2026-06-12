from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from app.api.schemas.analysis import AnalisisResponse
from app.api.services.analysis_service import AnalysisService


router = APIRouter(prefix="/api", tags=["analizar"])

TIPOS_VALIDOS = {"apk", "codigo_fuente", "url"}


def get_analysis_service():
    return AnalysisService()


@router.post("/analizar", response_model=AnalisisResponse)
async def analizar(
    tipo_analisis: str = Form(...),
    archivo: UploadFile | None = File(None),
    url: str | None = Form(None),
    service: AnalysisService = Depends(get_analysis_service),
):
    tipo = tipo_analisis.strip().lower()
    if tipo not in TIPOS_VALIDOS:
        raise HTTPException(
            status_code=400,
            detail=f"tipo_analisis debe ser uno de: {', '.join(sorted(TIPOS_VALIDOS))}.",
        )

    try:
        if tipo in {"apk", "codigo_fuente"}:
            if archivo is None:
                raise HTTPException(
                    status_code=400,
                    detail="Debes adjuntar 'archivo' para tipo_analisis 'apk' o 'codigo_fuente'.",
                )
            file_bytes = await archivo.read()
            if not file_bytes:
                raise HTTPException(status_code=400, detail="El archivo esta vacio.")

            if tipo == "apk":
                return service.analizar_apk(file_bytes, archivo.filename)
            return service.analizar_codigo_fuente(file_bytes, archivo.filename)

        if not url:
            raise HTTPException(status_code=400, detail="Debes indicar 'url' para tipo_analisis 'url'.")
        return service.analizar_url(url)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Error interno al analizar la aplicacion.") from exc
