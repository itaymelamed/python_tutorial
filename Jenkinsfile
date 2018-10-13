Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.7.0' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install pytest'
                sh 'pytest --junit-xml=reports/reports.xml'
            }
        }
    }
}
