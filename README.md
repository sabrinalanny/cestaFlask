
Fazer o download e colocar na raiz do projeto
https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm ./instantclient19.5-basiclite.rpm

docker build --build-arg DB_USER=cm --build-arg DB_PASSWORD=cm --build-arg DB_HOST=dbclone.bpark.com.br --build-arg DB_PORT=1521 --build-arg DB_SERVICE=desenv -t flask-rest-api .


