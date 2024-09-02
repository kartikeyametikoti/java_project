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

        stage('Docker Image Build') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}")
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    def myImage = docker.image('my-python-app:latest')
                    myImage.pull()  // Ensure the image is pulled
                    myImage.run('-d -p 5000:5000')
                }
            }
        }
    }
}
