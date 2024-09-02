pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app'
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
                    docker.build('my-python-app:latest')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('my-python-app:latest').run('-d -p 2000:5000')
                }
            }
        }
    }
}
