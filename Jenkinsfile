pipeline {
    agent none
    stages {

        stage('Deploy') {
            agent any
            steps {
                dir('web/') {
                    sh 'docker build -t app .'
                    sh 'docker run -d -p 5000:5000 --name app app'
                }
            }
        }

        stage('Test') {
            agent {
                dockerfile {
                    args '--link app'
                }
            }
            steps {
                dir('tests/') {
                    sh 'pytest --junit-xml=reports/reports.xml --html=html/index.html'
                }
            }

            post {
                always {
                    junit 'reports/reports.xml'
                    sh 'docker rm -f app'
                }
            }
        }
    }
}