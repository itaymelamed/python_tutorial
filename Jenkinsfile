pipeline {
    agent none
    stages {

        stage('Deploy') {
            agent any
            steps {
                dir('web/') {
                    sh 'docker build -t app .'
                    sh 'docker run -d -p --name app 5000:5000 app'
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
                    sh 'docker rm -f app'

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