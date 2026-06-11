# Recruitment-portal

## Project Structure
1. `job_auth`:  
    User managements, Separation and profile managements. Hapa utaasign user kulingana na nafasi zao. Mfano: ADMIN, CANDIDATE, VIEWER

1. `job_applications`:  
    Hii ni modules kwa ajili ya kumanage jobs na applications zake zote. CRUDS zote za Jobs na Application zitafanyika hapa.


## Database Configurations: For my case I'm using Mysql
## ----- STEP 1: CREATE THE DATABASE CONFIGURATIONS IN settings.py ------------
`DATABASES = {                                  `
`    'default': {                               `
`        'ENGINE': 'django.db.backends.mysql',   `
`        'NAME': 'job_recruitment_db',           `
`        'USER': 'PSRS_26_1022_1234',            `
`        'PASSWORD': '********',                  `
`        'HOST': 'localhost',                     `
`        'PORT': '3306',                           `
`    }                                             `
`}                                                 `

## ----- STEP 2: CREATE THE DATABASE IN MYSQL ------------
In Terminal type
`mysql -u PSRS_26_1022_1234 -p` then, enter password
`password: ***********`

CREATE THE DATABASE
`CREATE DATABASE job_recruitment_db  `    ## job_recruitment_db Is Database name


SHOW IF THE DATABASE CREATED
`SHOW DATABASES; `

CONNECT TO DATABASE
`USE job_recruitment_db;`

LIST TABLES
`SHOW TABLES; `

SHOW THE TABLE COLUMNS
`DESCRIBE User_profile;`   ## User_profile Is Table name

OTHER HELPFULL COMMANDS
## --- create the user ---------------
`CREATE USER 'username' @ 'localhost' IDENTIFIED BY 'password';    `
`Example: CREATE USER 'PSRS_26_1022_1234'@'localhost' IDENTIFIED BY ******; `

## ---- Grants Privileges to User ----------
`GRANT ALL PRIVILEGES ON 'database_name'.* TO 'username''@localhost' ; `
`Example: GRANT ALL PRIVILEGES ON job_recruitment_db.* TO  'PSRS_26_1022_1234' @'localhost' ; `


## ----- STEP 3: MAKING MIGRATIONS ------------
`python manage.py makemigrations`
`python manage.py migrate`


## ----- STEP 4: RUNNING THE PROJECTS ------------
`python manage.py runserver` ## by default the project will run at the 8000 port
`python manage.py runserver 0.0.0.0:1234` ## Running at the custom port, port ni namnba yako ya mwisho ya mtihani