FROM python:3.9

# Define as variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    DJANGO_ENV=production \
    DJANGO_SECRET_KEY=your_secret_key_here \
    POSTGRES_DB=mydatabase \
    POSTGRES_USER=myuser \
    POSTGRES_PASSWORD=mypassword \
    POSTGRES_HOST=db \
    POSTGRES_PORT=5432

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código-fonte do projeto
COPY . .

# Executa as migrações do Django
RUN python manage.py migrate

# Define o comando para iniciar o servidor
CMD python manage.py runserver 0.0.0.0:8000
