pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        stage('Allure') {
            steps {
                allure results: [[path: 'allure-results']]
            }
        }
    }
}
