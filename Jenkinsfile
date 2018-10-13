pipeline {
    agent none
    stages {

        stage('Deploy') {
            agent any
            dir('web/') {
                steps {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            dir('tests/') {
                agent {
                    dockerfile true
                }
                steps {
                    sh 'pytest --junit-xml=reports/reports.xml --html=html/index.html'
                }
                post {
                    always {
                        junit 'reports/reports.xml'
                    }
                }
            }
        }
    }
}