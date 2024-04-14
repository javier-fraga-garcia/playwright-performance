# Web Performance Playwright

Script para auditar la performance web utilizando como **Playwright**. Se carga la página y se accede a la API de `NavigationTiming` del navegador. Lo resultados se procesan con **Pydantic** y se exportan a un archivo `.csv`.

## Instalación

1. Clonar el repositorio
    ```bash
    git clone https://github.com/javier-fraga-garcia/playwright-performance
    ```
2. [OPCIONAL] Crear un entorno virtual y activarlo
    ```bash
    py -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux
    source venv/bin/activate
    ```
3. Instalar las dependencias
    ```bash
    pip install -r requirments.txt
    ```

## Uso

La herramienta de comandos se ha creado usando **Typer** con lo cual se puede acceder al sistema de ayuda con el comando `python3 main.py --help` (Linux) o `py main.py --help` (Windows). Esto desplegará la información sobre los argumentos del script y las posibles `flags`.

## Ejemplo

El siguiente comando permitiría realizar la auditoría para un archivo `urls.txt` situado en la raiz del directorio y almacenar los resultados en un `.csv` en la carpeta `data` dentro del directorio. Además, se envía la `flag` `--resource-type image` para bloquear la carga de imágenes.

```bash
python3 main.py ./urls.txt ./data/results.csv --resource-type image
```
