pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app3'
        DOCKER_TAG = 'latest'
        DOCKER_IMAGE_NAME = "${DOCKER_IMAGE}:${DOCKER_TAG}"
    }

    stages {
        stage('Getting Git Repo') {
            steps {
                git branch: 'main', credentialsId: 'mycredentials', url: 'https://github.com/kartikeyametikoti/java_project'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('my-python-app3:latest')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('my-python-app3:latest').run('-d -p 1500:5000')
                }
            }
        }
    }
}
