<h1 align="left">Scraper  -Web Site(Motorcycles)</h1>

###

[Sitio Web de Notificación](https://mi-repositorio.sharepoint.com/sites/mi-repositorio](https://aerobic-copilot-449214-n9.uc.r.appspot.com/)


<br clear="both">

<h4 align="left">Este proyecto permite realizar la extracción de información desde el sitio web Carroya - Motos(https://www.carroya.com/motos) . Los datos obtenidos son limpiados y almacenados en un archivo CSV, que posteriormente se guarda en un bucket de Google Cloud Storage. Además, cuenta con una interfaz en HTML y JavaScript que se encarga de generar un scrapeo cada vez que el usuario lo desee, así mediante WhatsApp se entrega una notificación de que proceso ha finalizado , junto a un archivo csv que el usuario puede descargar.<br><br>El proyecto está compuesto por los siguientes componentes:<br><br>1) Diagrama funcional<br>2)Scraping de Carroya.com<br>3)Procesamiento y limpieza de datos<br>4)Almacenamiento en Google Cloud<br>5)Notificación por WhatsApp<br>6) Deploy</h4>

###

<br clear="both">

<h3 align="left">1)Diagrama Funcional</h3>

###

<div align="center">
  <img height="200" src="images/DiagramaFuncional.png"  />
</div>

###

<br clear="both">

<h3 align="left">2) Scraping de Carroya.com</h3>

###

<br clear="both">

<h4 align="left">-Code: "utils/scraper.py"<br><br>-Realizar una petición mediante el método XHR (XMLHttpRequest) en un request<br><br>-El Response obtenido es un JSON con los datos de consulta.</h4>

###

<br clear="both">

<h3 align="left">3) Procesamiento y limpieza de datos</h3>

###

<br clear="both">

<h4 align="left">-Code: "utils/cleaner.py"<br><br>-Realizar una petición mediante el método XHR (XMLHttpRequest) en un request<br><br>-El Response obtenido es un JSON con los datos de consulta.</h4>

###

<br clear="both">

<h3 align="left">4) Almacenamiento en Google Cloud Storage</h3>

###

<br clear="both">

<h4 align="left">-Code: "utils/cleaner.py"<br><br>-Se encarga de conectar con Google Cloud Storage.<br><br>-Sube el archivo CSV generado a un bucket específico.</h4>

###

<br clear="both">

<h3 align="left">5) Notificación por WhatsApp</h3>

###

<br clear="both">

<h4 align="left">-Code: "utils/notifier.py" - "templates/index.html" - "static/script.js" - "static/styles.css"<br><br>-Cuenta con un frontend en HTML y JavaScript.<br><br>-Envío de notificaciones mediante la implementación de la libreria Twilio<br><br>-Envía la notificación vía WhatsApp al usuario cuando el proceso ha finalizado.</h4>

###

<br clear="both">

<h3 align="left">6) Deploy</h3>

###

<br clear="both">

<h4 align="left">6.1) En local<br><br>6.1.1) Instalación<br>-python -m venv env<br><br><br>6.1.2) Ejecución<br>-Ejecutar ".\env\Scripts\activate"<br>-Ejecutar "main.py"<br>-Para desactivar el ambiente virtual, ejecutar "deactivate"<br><br>Nota: En "main.py" descomentar las lineas 46 y 47, comentar las lineas 48 y 49.<br><br>6.2) En Google Cloud<br><br>6.2.1) Ejecución<br>-Ejecutar "gcloud auth login"<br>-Configurar el proyecto , ejecutando "gcloud config set project [ID DEL PROYECTO]" <br>-Acceder a la carpeta en la cual se encuentra el proyecto a ejecutar, cd "[RUTA PROYECTO]<br>-Ejecutar "gcloud app deploy"<br><br>Nota: En "main.py" comentar las lineas 46 y 47, descomentar las lineas 48 y 49.</h4>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="40" alt="googlecloud logo"  />
</div>

###
