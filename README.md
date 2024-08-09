# udemy-courses
All Udemy Courses Repo

---

## 🔩 Requirements

- Python
- FastAPI
- Docker
- Postgres

<br> 

## 🟢 Initiate
To start using or developing, install the necessary libraries using the commands:


* Create venv
    ```
    python -m venv .venv
    ```

* Install libs
    ```
    pip install -r .\requirements.txt
    ```

* Initialize venv
    ```
    .\.venv\Scripts\activate
    ```


<br> 

## ⚙️ Env Parameters

To initiate API service, the archive `.env` must be fill, like below:

[.env](/.env)
```
APP_CONTAINER_NAME=api_app                                         # [string] App conatiner name
FASTAPI_APP=main:app                                               # [string] Main route
FASTAPI_HOST=0.0.0.0                                               # [string] IP address
FASTAPI_PORT=8080                                                  # [int] Port number
FASTAPI_LOG_LEVEL=info                                             # [string] Log level fastapi parameter
FASTAPI_RELOAD=false                                               # [bool] Reloaded app fastapi parameter
FASTAPI_WORKERS=4                                                  # [int] Workers fastapi parameter
POSTGRES_DRIVERNAME=postgresql+asyncpg                             # [string] Database drivername 
POSTGRES_USER=postgres                                             # [string] Database username
POSTGRES_PASSWORD=postgres                                         # [string] Database user password
POSTGRES_HOST=api_db                                               # [string] Database address
POSTGRES_PORT=5432                                                 # [int] Database port number
POSTGRES_NAME=postgres                                             # [string] Database name
```

<br> 

## 🏃🏼 Run Uvicorn

- To run uvicorn, only execute [main.py](./src/main.py)
    ```
    py ./src/main.py
    ```
    ```
    python3 ./src/main.py
    ```
    ```
    python ./src/main.py
    ```


<br> 

## ⚠️ Important

- Make sure all dependencies are installed correctly.

<br> 

## 🤝 Colaborators

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/jo%C3%A3o-pedro-dias-caparroz-2b19a1161/" title="Linkedin Profile Icon">
        <img src="https://media.licdn.com/dms/image/C4D03AQHVyVT6CT6TFQ/profile-displayphoto-shrink_800_800/0/1595939105632?e=1724889600&v=beta&t=_pjNFXdW8VeM4IR5RhY9cgZ0NsAakg6EBEssgodCpwk" width="100px;" alt="Foto"/><br>
        <sub>
          <b>João Pedro Dias Caparroz</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<br>