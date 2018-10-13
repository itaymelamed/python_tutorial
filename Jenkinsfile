pipeline {
    agent none
    stages {
        stage ("Clean up") {
            agent any
            steps {
                sh 'docker ps -q -f name=app | xargs docker rm -f'
            }
        }
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
    }
}