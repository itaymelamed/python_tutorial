Jenkinsfile (Declarative Pipeline)
pipeline {
    agent none
    stages {

        stage('Build') {
            agent {
                docker {
                    image 'python:3.7.0'
                }
            }
            steps {
                sh 'python -v'
            }
        }

        stage('Test') {
            agent {
                docker  {
                    image 'python:latest'
                }
            }
            steps {
                sh 'pip install pytest'
                sh 'pytest --junit-xml=reports/reports.xml'
            }
            post {
                always {
                    junit 'reports/reports.xml'
                }
            }
        }
    }
}