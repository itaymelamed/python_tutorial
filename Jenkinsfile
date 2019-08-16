pipeline {
  agent none
  stages {
    stage('Run docker') {
        agent {
            kubernetes {
                defaultContainer 'jnlp'
                yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: "jnlp"
    image: "jenkins/jnlp-slave:alpine"
    volumeMounts:
    - name: "workspace-volume"
      mountPath: "/home/jenkins/agent"
      readOnly: false
    - name: "reports"
      mountPath: "/reports"
      readOnly: false
  - name: python
    image: python:alpine
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
    - name: "workspace-volume"
      mountPath: "/home/jenkins/agent"
      readOnly: false
    - name: "reports"
      mountPath: "/reports"
      readOnly: false
  - name: docker
    image: docker
    command: ['cat']
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
    - name: "workspace-volume"
      mountPath: "/home/jenkins/agent"
      readOnly: false
    - name: "reports"
      mountPath: "/reports"
      readOnly: false
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
  - name: "workspace-volume"
    emptyDir: {}
  - name: "reports"
    emptyDir: {}
"""
            }
        }
        steps {
            container('docker') {
                sh 'docker network create test'

                dir('web') {
                    sh 'docker build -t app .'
                }

                sh 'docker run -d --name web --network test app'
            }
            container('python') {
                dir('tests') {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest --junitxml=reports/report.xml'
                }
            }
        }
        post {
            always {
                sh 'docker rm -f app'
                sh 'docker network rm test'
            }
        }
    }
  }
  post {
    always {
        junit 'reports/report.xml'
    }
  }
}
