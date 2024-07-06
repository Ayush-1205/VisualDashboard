# Dashboard
**Step 1:** Create MySQL Table
Open MySQL Workbench and connect to your MySQL server.
Create the database and table 

**Step 2:** Load JSON Data into MySQL
Use the** datatosql.py **python script to load data from jsondata.json into the MySQL table
Do change in the python script according to your database name and password

**Step 3:** Set Up Django Backend
In Project's Settings.py add database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
   
}

in installed apps add  **'corsheaders'**

in middleware add** 'corsheaders.middleware.CorsMiddleware',
     'django.middleware.common.CommonMiddleware',**

**CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # React app URL
]**

**Step4:** For frontend create Home.js which gives the following output
![Screenshot 2024-07-06 171445](https://github.com/Ayush-1205/VisualDashboard/assets/101936254/40aab9ee-f0f1-4c59-9c53-089df2a87b92)


**Step5:** Make all the bargraphs and piecharts and the remaining pages which will look like this:
![Screenshot 2024-07-06 172410](https://github.com/Ayush-1205/VisualDashboard/assets/101936254/77dc257e-c3a2-453b-9aeb-f9bc5ccc5670)


![Screenshot 2024-07-06 172654](https://github.com/Ayush-1205/VisualDashboard/assets/101936254/e3fa3013-6fe2-44c6-81a7-a82f40cac9c6)

Home will take you to all the Pages having their own Bargraphs and Piecharts also the data is coming form the Backend Api's ( http://127.0.0.1:8000/api/data).
**Assign** is the **virtual environment** which contains all the libraries and their version required to run this project.



