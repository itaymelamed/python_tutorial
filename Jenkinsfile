pipeline {
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
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
  - name: "workspace-volume"
    emptyDir: {}
"""
    }
  }
  stages {
    stage('Run docker') {
        steps {
            container('docker') {
                sh 'ls'
                sh 'mkdir /home/jenkins/agent/test'
            }
            sh 'ls'
            sh 'ls /home/jenkins/agent/test'
        }
    }
  }
}
