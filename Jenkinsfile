pipeline {
    agent any
    
    environment {
        PATH = "C:/WINDOWS/SYSTEM32;C:/Users/antho/AppData/Local/Programs/Python/Python310;C:/Program Files/Docker/Docker/resources/bin"
    }
    
    stages {    
        stage('Testing app') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install Flask'
                bat 'python -m pip install requests'
                bat 'python -m pip install numpy'
                bat 'python -m pip install keras'
                bat 'python -m pip install tensorflow'
                bat 'python test_main.py'
            }
        }
        
        stage('Docker deploy') {
            steps {
                bat 'docker build -t -p 8080:5000 my-app .'
                bat 'docker run -d -p  my-app'
            }
        }
    }
}
