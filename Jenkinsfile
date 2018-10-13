pipeline {
    agent none
    stages {

        stage('Deploy') {
            agent any
            steps {
                dir('web/') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            agent {
                dockerfile true
            }
            steps {
                dir('tests/') {
                    sh 'pytest --junit-xml=reports/reports.xml --html=html/index.html'
                }
            }
            post {
                always {
                    junit 'reports/reports.xml'
                }
            }
        }
    }
}