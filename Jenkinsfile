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
            sh 'ls' 
            container('docker') {
                sh 'docker ls'
                sh 'docker network create test'
                sh 'docker run -d --name nginx1 --network test nginx'
                sh 'docker run -d --name nginx2 --network test nginx'
                sh 'docker exec -i nginx1 apt update'
                sh 'docker exec -i nginx1 apt install curl -y'
                sh 'docker exec -i nginx1 curl nginx2'
                sh 'docker rm -f nginx1 nginx2'
                sh 'docker network rm test'
            }
        }
    }
  }
}
