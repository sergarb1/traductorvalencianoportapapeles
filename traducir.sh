ruta=`pwd`
curl -F "MAX_FILE_SIZE1=10000000" -F "ua_memories=true" -F "terminology_file=0" -F "cuadrotexto=$1" -F "marcar=0" -F "direccion=spa-cat_valencia_uni" https://apertium.ua.es/tradtexto.php

