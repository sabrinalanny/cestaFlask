# Sets the base image for subsequent instructions
FROM python:3.7-slim
# Sets the working directory in the container  
WORKDIR /app
RUN apt-get update -y && apt-get install alien -y
RUN apt-get install -y python3-pip python3-dev

# Copies the files to the working directory
COPY . /app
# Copies the dependency files to the working directory
COPY requirements.txt requirements.txt
# Install dependencies
#RUN pip install -r requirements.txt

#baixando os drives da oracle
#ADD docker#ADD ./oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm  /opt

#convertendo os arquivos para .deb e removendo após a instalação
RUN alien -i  --scripts  ./oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm 
#&& rm ./instantclient19.5-basiclite.*

#Instalando os requerimentos da aplicação python e uma lib para conectar ao oracle e removendo o alien, pois não será mais utilizado
RUN pip install -r requirements.txt && apt-get install libaio1 libaio-dev -y && apt-get remove alien -y

#configurando as variáveis de ambiente dos drives da oracle
ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client(64)/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ENV ORACLE_HOME="/usr/lib/oracle/19.5/client(64)"
ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}+""

# Copies everything to the working directory
COPY . /app

EXPOSE 8000
# Command to run on container start    
ENTRYPOINT [ "python3" ] 
CMD [ "api/__init__.py" ]
#CMD ["sh","api/serve.sh"]