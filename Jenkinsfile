pipeline {
    agent none
    stages {

        stage('Build') {
            agent {
                docker {
                    image 'python:latest'
                }
            }
            steps {
                sh 'python -v'
            }
        }

        stage('Test') {
            agent {
                dockerfile true
            }
            steps {
                sh 'pytest --junit-xml=reports/reports.xml --html=reports/index.html'
            }
            post {
                always {
                    junit 'reports/reports.xml'
                    publishHTML target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'index.html',
                        reportName: 'RCov Report'
                      ]
                }
            }
        }
    }
}