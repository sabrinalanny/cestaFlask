FROM python:3.7-slim

RUN apt-get update -y 

#Criando os argumento que serão passados no processo de build
#ARG DB_USER
#ARG DB_PASSWORD
#ARG DB_HOST
#ARG DB_PORT
#ARG DB_SERVICE

# Definindo as variáveis de ambiente com os argumentos
#ENV DB_USER=${DB_USER}
#ENV DB_PASSWORD=${DB_PASSWORD}
#ENV DB_HOST=${DB_HOST}
#ENV DB_PORT=${DB_PORT}
#ENV DB_SERVICE=${DB_SERVICE}

#RUN apt-get update && apt-get install -y libaio1 curl unzip && \
#  cd /tmp && \
#  curl -o instantclient-basiclite.zip https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip -SL && \
#  unzip instantclient-basiclite.zip && \
#  mv instantclient*/ /usr/lib/instantclient && \
#  rm instantclient-basiclite.zip && \
#  ln -s /usr/lib/instantclient/libclntsh.so.19.1 /usr/lib/libclntsh.so && \
#  ln -s /usr/lib/instantclient/libocci.so.19.1 /usr/lib/libocci.so && \
#  ln -s /usr/lib/instantclient/libociicus.so /usr/lib/libociicus.so && \
#  ln -s /usr/lib/instantclient/libnnz19.so /usr/lib/libnnz19.so && \
#  ln -s /usr/lib/libnsl.so.2 /usr/lib/libnsl.so.1 && \
#  ln -s /lib/libc.so.6 /usr/lib/libresolv.so.2 && \
#  ln -s /lib64/ld-linux-x86-64.so.2 /usr/lib/ld-linux-x86-64.so.2


#ENV ORACLE_BASE /usr/lib/instantclient
#ENV LD_LIBRARY_PATH /usr/lib/instantclient
#ENV TNS_ADMIN /usr/lib/instantclient
#ENV ORACLE_HOME /usr/lib/instantclient

WORKDIR /app
RUN apt-get install -y python3-pip python3-dev

COPY . /app
RUN pip install -r requirements.txt 

EXPOSE 8000

ENTRYPOINT [ "python3" ] 
CMD [ "manage.py" ]
