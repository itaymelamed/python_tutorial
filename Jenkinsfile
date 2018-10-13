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
                docker  {
                    image 'python:latest'
                }
            }
            steps {
                sh 'pip install pytest'
                sh 'pytest --junit-xml=reports/reports.xml --html=reports/html/index.html'
            }
            post {
                always {
                    junit 'reports/reports.xml'
                    publishHTML target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: true,
                        reportDir: 'reprts/html',
                        reportFiles: 'index.html',
                        reportName: 'RCov Report'
                      ]
                }
            }
        }
    }
}