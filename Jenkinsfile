pipeline {
    agent {
        kubernetes {
        defaultContainer 'jnlp'
        yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker
    command: ['cat']
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
  stages {
    stage('Run docker') {
        steps {
            sh 'docker ps' 
            container('docker') {
                sh 'ls'
            }
        }
    }
  }
}
