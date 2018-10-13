pipeline {
    agent none
    stages {

        stage("Deploy") {
            agent any
            steps {
                echo "${env.BRANCH_NAME}"
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
                    junit 'tests/reports/reports.xml'
                }
            }
        }

        stage('Clean') {
            agent any
            steps {
                echo 'removing app container'
            }
            post {
                always {
                    sh 'docker rm -f app'
                }
            }
        }
    }
}