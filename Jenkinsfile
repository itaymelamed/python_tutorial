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
            container('python') {
                sh 'python --version'
            }
        }
    }
  }
}
